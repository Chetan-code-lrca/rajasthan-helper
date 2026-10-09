'use strict';
const assert = require('node:assert/strict');
const { JSDOM, VirtualConsole } = require('jsdom');

const url = 'http://127.0.0.1:4173/';
const errors = [];
let copiedText = '';
let openedUrl = '';
let lastDownload = null;
let registeredWorkerURL = null;
let sharedPayload = null;
const virtualConsole = new VirtualConsole();
virtualConsole.on('jsdomError', error => errors.push(error.message));

function routeNightTotal(d) { return Array.from(d.querySelectorAll('[data-nights]')).reduce((sum,input)=>sum+Number(input.value||0),0); }

async function main() {
  const dom = await JSDOM.fromURL(url, {
    resources: 'usable',
    runScripts: 'dangerously',
    pretendToBeVisual: true,
    virtualConsole,
    beforeParse(window) {
      try { window.localStorage.clear(); } catch (error) {}
      Object.defineProperty(window.navigator, 'serviceWorker', { configurable: true, value: { register: async url => { registeredWorkerURL = url; return {}; } } });
      Object.defineProperty(window.navigator, 'clipboard', { configurable: true, value: { writeText: async text => { copiedText = text; } } });
      window.URL.createObjectURL = () => 'blob:rajasthan-test';
      window.URL.revokeObjectURL = () => {};
      window.open = target => { openedUrl = target; return {}; };
      window.HTMLAnchorElement.prototype.click = function () { lastDownload = { href: this.href, name: this.download }; };
    }
  });
  const w = dom.window;
  const d = w.document;
  const pause = ms => new Promise(resolve => w.setTimeout(resolve, ms));
  if (d.readyState !== 'complete') await new Promise(resolve => w.addEventListener('load', resolve, { once: true }));
  await pause(30);

  assert.equal(d.querySelectorAll('#destinations .place').length, 12, 'destination cards should render');
  assert.match(d.querySelector('.source-card').textContent, /Official links last checked: 09 Oct 2026/, 'source card should show a visible last-checked date');
  assert.equal(Array.from(d.querySelectorAll('.source-card a')).some(link => link.href === 'https://www.tourism.rajasthan.gov.in/tourist-destinations.html'), true, 'source card should include the official destination directory');
  assert.equal(registeredWorkerURL, './sw.js', 'offline service worker should register');
  d.querySelector('[data-filter="Heritage"]').click();
  assert.equal(d.querySelectorAll('#destinations .place').length, 7, 'heritage filter should narrow destination list');
  d.querySelector('[data-filter="All"]').click();
  const search = d.getElementById('search');
  search.value = 'jodh';
  search.dispatchEvent(new w.Event('input', { bubbles: true }));
  assert.equal(d.querySelectorAll('#destinations .place').length, 1, 'search should filter destinations');
  search.value = '';
  search.dispatchEvent(new w.Event('input', { bubbles: true }));
  d.querySelector('[data-add="Pushkar"]').click();
  assert.equal(d.querySelectorAll('#route li strong').length, 1, 'adding a supported destination should work');
  d.querySelector('[data-remove="0"]').click();
  assert.equal(d.querySelectorAll('#route li strong').length, 0, 'removing a stop should work');

  d.querySelector('[data-add="Jodhpur"]').click();
  d.querySelector('[data-add="Jaisalmer"]').click();
  await pause(20);
  assert.equal(d.querySelectorAll('#route li strong').length, 2, 'adding stops should update route');
  assert.equal(d.querySelector('[data-nights="Jodhpur"]').value, '2', 'city night defaults should appear in the route editor');
  assert.equal(d.querySelector('[data-nights="Jaisalmer"]').value, '2', 'each route stop should have a night count');
  for (const city of ['Jodhpur','Jaisalmer']) {
    const nights=d.querySelector('[data-nights="'+city+'"]');
    nights.value='1'; nights.dispatchEvent(new w.Event('change',{bubbles:true}));
  }
  assert.match(d.getElementById('itinerarySummary').textContent, /2 planned nights \/ 2 expected/, 'overnight totals should reconcile with duration');
  assert.equal(JSON.parse(w.localStorage.getItem('rajasthan-routes')).nightsByStop.Jodhpur, 1, 'night allocations should persist locally');
  d.querySelector('[data-up="1"]').click();
  assert.match(d.getElementById('route').textContent, /1\. Jaisalmer.*2\. Jodhpur/, 'move-up control should reorder stops');
  d.querySelector('[data-up="1"]').click();
  assert.match(d.getElementById('route').textContent, /1\. Jodhpur.*2\. Jaisalmer/, 'route can be reordered back');
  assert.equal(d.getElementById('routeKm').textContent, '286 km', 'known published route distance should be shown');
  assert.equal(d.querySelectorAll('#timeline .itinerary-day').length, 3, 'selected route should create daily outline');
  assert.ok(JSON.parse(w.localStorage.getItem('rajasthan-routes')).route.includes('Jaisalmer'), 'draft should persist locally');
  assert.match(d.querySelectorAll('#timeline .itinerary-day')[2].textContent, /Jaisalmer/, 'last destination should have a day for exploring, not only arrival');

  d.getElementById('days').value = '4';
  d.getElementById('days').dispatchEvent(new w.Event('input', { bubbles: true }));
  d.getElementById('people').value = '3';
  d.getElementById('people').dispatchEvent(new w.Event('input', { bubbles: true }));
  d.getElementById('daily').value = '2500';
  d.getElementById('daily').dispatchEvent(new w.Event('input', { bubbles: true }));
  assert.equal(d.getElementById('total').textContent, '₹30,000', 'budget arithmetic should multiply days, travellers and per-person spend');
  assert.match(d.getElementById('budgetAmounts').textContent, /₹875/, 'budget breakdown should calculate accommodation share');

  d.getElementById('clear').click();
  d.getElementById('days').value = '7';
  d.getElementById('days').dispatchEvent(new w.Event('input', { bubbles: true }));
  for (const city of ['Jaipur', 'Pushkar', 'Jodhpur', 'Jaisalmer']) d.querySelector('[data-add="' + city + '"]').click();
  const jodhpurNights=d.querySelector('[data-nights="Jodhpur"]');
  jodhpurNights.value='1'; jodhpurNights.dispatchEvent(new w.Event('change',{bubbles:true}));
  assert.equal(routeNightTotal(d),6,'four-stop route nights should be editable to fit a seven-day trip');
  const startDate = d.getElementById('startDate'), endDate = d.getElementById('endDate');
  startDate.value = '2026-11-10'; startDate.dispatchEvent(new w.Event('change', { bubbles: true }));
  endDate.value = '2026-11-16'; endDate.dispatchEvent(new w.Event('change', { bubbles: true }));
  await pause(20);
  assert.equal(d.querySelectorAll('#route li strong').length, 4, 'all four selected destinations should remain in the route after date edits');
  assert.equal(d.getElementById('days').value, '7', 'date range should calculate inclusive trip length');
  assert.equal(d.getElementById('days').readOnly, true, 'duration should be date-derived when both dates are set');
  assert.match(d.getElementById('dateNotice').textContent, /Season prompt/, 'selected month should add a seasonal prompt');
  assert.match(d.querySelector('#timeline .day-tag').textContent, /10 Nov/, 'first itinerary day should show its calendar date');
  assert.match(d.querySelectorAll('#timeline .day-tag')[6].textContent, /16 Nov/, 'last itinerary day should match the selected end date');
  endDate.value = '2026-11-09'; endDate.dispatchEvent(new w.Event('change', { bubbles: true }));
  assert.equal(d.getElementById('dateNotice').dataset.state, 'error', 'end date before start date should be rejected');
  endDate.value = '2026-11-16'; endDate.dispatchEvent(new w.Event('change', { bubbles: true }));
  await pause(20);
  const plannedDays = Array.from(d.querySelectorAll('#timeline .itinerary-day h3')).map(el => el.textContent.trim());
  assert.equal(plannedDays.length, 7, 'seven-day four-stop plan should render seven days');
  assert.match(plannedDays[0], /Arrive in Jaipur/, 'first day should start in the first city');
  assert.equal(plannedDays[1], 'Jaipur', 'a two-night first stop should have a full exploration day');
  assert.match(plannedDays[2], /Jaipur → Pushkar/, 'transfer day should follow the first stop nights');
  assert.match(plannedDays[3], /Pushkar → Jodhpur/, 'next transfer should follow Pushkar overnight');
  assert.match(plannedDays[4], /Jodhpur → Jaisalmer/, 'transfer sequence should follow the configured nights');
  assert.equal(plannedDays[5], 'Jaisalmer', 'final destination should have exploration time after arrival');
  assert.equal(plannedDays[6], 'Jaisalmer', 'final destination should retain the second night and departure day');
  d.getElementById('itineraryCopy').click();
  await pause(20);
  assert.match(copiedText, /Day 7.*Jaisalmer/, 'day-by-day copy should place the final destination in clipboard text');
  assert.match(copiedText, /Nights per stop:.*Jodhpur.*1 night/, 'day-by-day copy should include editable overnight allocation');
  const checklist0 = d.querySelector('[data-check="0"]'); checklist0.checked = true; checklist0.dispatchEvent(new w.Event('change', { bubbles: true }));
  assert.equal(JSON.parse(w.localStorage.getItem('rr-checks'))[0], true, 'checklist state should persist locally');


  d.getElementById('mapsRouteBtn').click();
  assert.match(openedUrl, /google\.com\/maps\/dir\/\?api=1/, 'route should open a Google Maps directions URL');
  d.getElementById('downloadBtn').click();
  assert.equal(lastDownload && lastDownload.name, 'rajasthan-trip-plan.txt', 'save text plan should download a plain-text trip');
  d.getElementById('shareBtn').click();
  await pause(10);
  assert.match(copiedText, /127\.0\.0\.1:4173\/$/, 'share control should copy a usable planner URL when native sharing is unavailable');
  Object.defineProperty(w.navigator, 'share', { configurable: true, value: async payload => { sharedPayload = payload; } });
  d.getElementById('shareBtn').click(); await pause(10);
  assert.equal(sharedPayload.url, w.location.href, 'native share should receive the current planner URL');
  d.getElementById('exportDraft').click();
  assert.equal(lastDownload && lastDownload.name, 'rajasthan-trip-backup.json', 'export should download a JSON backup');
  d.getElementById('copy').click();
  await pause(10);
  assert.match(copiedText, /Jodhpur.*Jaisalmer/, 'copy action should include current route');

  const backup = { version: 1, route: ['Jaipur', 'Udaipur'], nightsByStop: { Jaipur: 1, Udaipur: 3 }, days: 5, startDate: '2027-01-02', endDate: '2027-01-06', people: 2, daily: 3000, checks: { 0: true }, lens: 'family' };
  const fileInput = d.getElementById('importDraftFile');
  Object.defineProperty(fileInput, 'files', { configurable: true, value: [{ text: async () => JSON.stringify(backup) }] });
  fileInput.dispatchEvent(new w.Event('change', { bubbles: true }));
  await pause(30);
  assert.equal(d.querySelectorAll('#route li strong').length, 2, 'import should restore route stops');
  assert.match(d.getElementById('route').textContent, /Jaipur.*Udaipur/, 'import should restore the saved route order');
  assert.match(d.getElementById('itinerarySummary').textContent, /Fast-paced draft|Budget estimate/, 'itinerary summary should explain the imported plan');
  assert.equal(d.getElementById('days').value, '5', 'import should restore trip duration');
  assert.equal(d.querySelector('[data-nights="Jaipur"]').value, '1', 'backup should restore nights for Jaipur');
  assert.equal(d.querySelector('[data-nights="Udaipur"]').value, '3', 'backup should restore nights for Udaipur');
  assert.equal(d.getElementById('startDate').value, '2027-01-02', 'backup should restore the start date');
  assert.equal(d.getElementById('endDate').value, '2027-01-06', 'backup should restore the end date');
  assert.match(d.querySelector('#timeline .day-tag').textContent, /2 Jan/, 'imported itinerary should display restored dates');
  assert.ok(d.querySelector('[data-lens="family"]').classList.contains('active'), 'import should refresh selected travel lens');
  assert.equal(d.querySelector('[data-check="0"]').checked, true, 'import should restore checklist state');
  d.getElementById('clearChecks').click();
  assert.equal(d.querySelector('[data-check="0"]').checked, false, 'clear checklist control should reset checked items');

  const runtimeErrors = errors.filter(message => !/Not implemented: window\.scrollTo/.test(message));
  assert.deepEqual(runtimeErrors, [], 'page scripts should not emit jsdom runtime errors');
  console.log('PASS: destinations render, category filters and search work.');
  console.log('PASS: stops update route, distance and daily itinerary.');
  console.log('PASS: date range calculation, validation, weekday labels and seasonal prompts work.');
  console.log('PASS: nights per stop update the itinerary, reconcile totals and persist through backups.');
  console.log('PASS: budget totals and category breakdown update.');
  console.log('PASS: Maps, copy, export and import controls execute.');
  console.log('PASS: imported route, settings, travel lens and checklist are restored.');
  dom.window.close();
}

main().catch(error => { console.error(error); process.exitCode = 1; });