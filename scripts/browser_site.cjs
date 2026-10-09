'use strict';
const assert = require('node:assert/strict');
const { chromium } = require('playwright');

const APP_URL = 'http://127.0.0.1:4173/';
const ROOT_URL = 'http://127.0.0.1:4174/#planner';

async function main() {
  const browser = await chromium.launch({ headless: true });
  const pageErrors = [];
  try {
    const context = await browser.newContext({
      viewport: { width: 1366, height: 900 },
      permissions: ['clipboard-read', 'clipboard-write'],
      acceptDownloads: true
    });
    const page = await context.newPage();
    page.on('pageerror', error => pageErrors.push(error.message));
    page.on('console', message => {
      if (message.type() === 'error') pageErrors.push('console: ' + message.text());
    });

    const response = await page.goto(APP_URL, { waitUntil: 'networkidle' });
    assert.ok(response && response.ok(), 'app document should respond successfully');
    assert.equal(await page.title(), 'Rajasthan Routes — Travel Companion');
    assert.equal(await page.locator('#destinations .place').count(), 12, 'all destination cards render');
    assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth), 'desktop layout should not overflow horizontally');

    await page.locator('[data-filter="Heritage"]').click();
    assert.equal(await page.locator('#destinations .place').count(), 7, 'heritage category filters');
    await page.locator('[data-filter="All"]').click();
    await page.locator('#search').fill('jodh');
    assert.equal(await page.locator('#destinations .place').count(), 1, 'destination search filters');
    await page.locator('#search').fill('');

    for (const city of ['Jaipur', 'Pushkar', 'Jodhpur', 'Jaisalmer']) {
      await page.locator('[data-add="' + city + '"]').click();
    }
    assert.equal(await page.locator('[data-nights="Jodhpur"]').inputValue(), '2', 'city night defaults render');
    await page.locator('[data-nights="Jodhpur"]').fill('1');
    await page.locator('[data-nights="Jodhpur"]').dispatchEvent('change');
    await page.locator('#startDate').fill('2026-11-10');
    await page.locator('#startDate').dispatchEvent('change');
    await page.locator('#endDate').fill('2026-11-16');
    await page.locator('#endDate').dispatchEvent('change');
    assert.match(await page.locator('#itinerarySummary').innerText(), /6 planned nights \/ 6 expected/, 'overnight allocation should reconcile with a seven-day trip');
    assert.equal(await page.locator('#days').inputValue(), '7', 'inclusive start/end dates determine trip length');
    assert.match(await page.locator('#dateNotice').innerText(), /Season prompt/, 'month-aware prompt appears');
    assert.equal(await page.locator('#timeline .itinerary-day').count(), 7, 'date-based itinerary has one card per day');
    assert.match(await page.locator('#timeline .day-tag').first().innerText(), /10 Nov/, 'itinerary labels first calendar date');
    assert.match(await page.locator('#timeline .day-tag').last().innerText(), /16 Nov/, 'itinerary labels last calendar date');
    assert.match(await page.locator('#itinerarySummary').innerText(), /Dates:/, 'summary includes selected dates');

    await page.locator('#people').fill('3');
    await page.locator('#daily').fill('2500');
    assert.equal(await page.locator('#total').innerText(), '₹52,500', 'budget updates after date-derived duration and traveller changes');
    await page.locator('[data-up="3"]').click();
    assert.match(await page.locator('#route').innerText(), /3\. Jaisalmer.*4\. Jodhpur/s, 'reorder control moves a stop');
    await page.locator('[data-up="3"]').click();
    const mapsPopupPromise = context.waitForEvent('page');
    await page.locator('#mapsRouteBtn').click();
    const mapsPopup = await mapsPopupPromise;
    await mapsPopup.waitForURL(url => url.hostname === 'www.google.com' && url.pathname === '/maps/dir/' && url.searchParams.get('api') === '1', { timeout: 10000 });
    const mapsUrl = new URL(mapsPopup.url());
    assert.equal(mapsUrl.hostname, 'www.google.com', 'Maps control opens Google Maps');
    assert.equal(mapsUrl.pathname, '/maps/dir/', 'Maps control opens directions rather than search');
    assert.equal(mapsUrl.searchParams.get('api'), '1', 'Maps URL uses the directions API parameters');
    await mapsPopup.close();

    const copied = await page.evaluate(async () => {
      await navigator.clipboard.writeText('browser clipboard check');
      return navigator.clipboard.readText();
    });
    assert.equal(copied, 'browser clipboard check', 'browser clipboard permissions work');
    await page.locator('#itineraryCopy').click();
    await page.waitForFunction(async () => (await navigator.clipboard.readText()).includes('Nights per stop:'), { timeout: 5000 });
    const copiedTrip = await page.evaluate(() => navigator.clipboard.readText());
    assert.match(copiedTrip, /Nights per stop:.*Jodhpur.*1 night/, 'copied itinerary includes night allocations');

    const [backupDownload] = await Promise.all([
      page.waitForEvent('download'),
      page.locator('#exportDraft').click()
    ]);
    assert.equal(backupDownload.suggestedFilename(), 'rajasthan-trip-backup.json', 'backup export downloads a JSON file');

    const backup = {
      version: 1,
      route: ['Jaipur', 'Udaipur'],
      nightsByStop: { Jaipur: 1, Udaipur: 3 },
      days: 5,
      startDate: '2027-01-02',
      endDate: '2027-01-06',
      people: 2,
      daily: 3000,
      checks: { 0: true },
      lens: 'family'
    };
    await page.locator('#importDraftFile').setInputFiles({
      name: 'rajasthan-trip-backup.json',
      mimeType: 'application/json',
      buffer: Buffer.from(JSON.stringify(backup))
    });
    await page.waitForFunction(() => document.querySelector('#startDate').value === '2027-01-02', { timeout: 5000 });
    assert.equal(await page.locator('#startDate').inputValue(), '2027-01-02', 'import restores start date');
    assert.equal(await page.locator('#endDate').inputValue(), '2027-01-06', 'import restores end date');
    assert.equal(await page.locator('#days').inputValue(), '5', 'import restores derived trip length');
    assert.equal(await page.locator('[data-nights="Jaipur"]').inputValue(), '1', 'import restores Jaipur nights');
    assert.equal(await page.locator('[data-nights="Udaipur"]').inputValue(), '3', 'import restores Udaipur nights');
    assert.match(await page.locator('#itinerarySummary').innerText(), /4 planned nights \/ 4 expected/, 'imported overnight allocation matches its date range');
    assert.equal(await page.locator('[data-lens="family"]').getAttribute('class').then(v => v.includes('active')), true, 'import restores travel style');
    assert.equal(await page.locator('[data-check="0"]').isChecked(), true, 'import restores checklist');

    // Force the offline shell to be controlled, then reload without network.
    await page.reload({ waitUntil: 'networkidle' });
    await page.waitForFunction(() => 'serviceWorker' in navigator && navigator.serviceWorker.controller !== null, { timeout: 10000 });
    const serviceWorkerScope = await page.evaluate(() => navigator.serviceWorker.controller.scriptURL);
    assert.match(serviceWorkerScope, /sw\.js$/, 'service worker controls the page');
    await context.setOffline(true);
    await page.reload({ waitUntil: 'domcontentloaded', timeout: 10000 });
    assert.equal(await page.title(), 'Rajasthan Routes — Travel Companion', 'app shell reopens offline after first successful load');
    assert.equal(await page.locator('#destinations .place').count(), 12, 'destinations remain usable offline');
    await context.setOffline(false);

    // Real mobile viewport: check for overflow and core controls.
    const mobileContext = await browser.newContext({
      viewport: { width: 390, height: 844 },
      deviceScaleFactor: 1,
      isMobile: true,
      hasTouch: true,
      acceptDownloads: true
    });
    const mobile = await mobileContext.newPage();
    mobile.on('pageerror', error => pageErrors.push('mobile: ' + error.message));
    await mobile.goto(APP_URL, { waitUntil: 'networkidle' });
    assert.equal(await mobile.locator('#destinations .place').count(), 12, 'mobile renders destination cards');
    assert.ok(await mobile.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth), 'mobile layout should not overflow horizontally');
    await mobile.locator('#planner').scrollIntoViewIfNeeded();
    assert.ok(await mobile.locator('#startDate').isVisible(), 'mobile date field remains visible');
    await mobile.locator('[data-add="Jaipur"]').click();
    assert.equal(await mobile.locator('#route li strong').count(), 1, 'route editing works on mobile');
    assert.ok(await mobile.locator('[data-nights="Jaipur"]').isVisible(), 'mobile exposes the nights control');
    await mobile.locator('[data-nights="Jaipur"]').fill('1');
    await mobile.locator('[data-nights="Jaipur"]').dispatchEvent('change');
    assert.match(await mobile.locator('#itinerarySummary').innerText(), /1 planned night/, 'mobile night change updates the itinerary');
    assert.ok(await mobile.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth), 'editing nights should not cause mobile horizontal overflow');

    // The exact repository root should forward #planner to /site/#planner.
    const rootPage = await context.newPage();
    await rootPage.goto(ROOT_URL, { waitUntil: 'domcontentloaded' });
    await rootPage.waitForURL('**/site/#planner', { timeout: 10000 });
    assert.equal(new URL(rootPage.url()).hash, '#planner', 'root redirect preserves the planner anchor');

    assert.deepEqual(pageErrors, [], 'no uncaught browser console/page errors');
    console.log('PASS: Chromium desktop filters, route editing, date calculation and itinerary labels.');
    console.log('PASS: budget, reorder, browser clipboard, JSON backup export/import.');
    console.log('PASS: overnight allocation totals align with trip dates and persist across import/export.');
    console.log('PASS: service worker controls the page and cached app reopens offline.');
    console.log('PASS: mobile 390px viewport has no horizontal overflow; core route controls work.');
    console.log('PASS: repository root redirects to /site/#planner and preserves the anchor.');
    await mobileContext.close();
    await context.close();
  } finally {
    await browser.close();
  }
}

main().catch(error => {
  console.error(error);
  process.exitCode = 1;
});
