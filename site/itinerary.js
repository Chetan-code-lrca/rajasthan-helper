(function(){
const PLACES={
"Jaipur":{stay:2,zone:"East / central",items:["Amber Fort or City Palace","Old-city walk and a local market","Early dinner and rest"]},
"Udaipur":{stay:2,zone:"South",items:["City Palace or old city","Lake Pichola area","Unhurried lakeside evening"]},
"Jodhpur":{stay:2,zone:"West",items:["Mehrangarh Fort","Blue City lanes or stepwells","Old-city food and market time"]},
"Jaisalmer":{stay:2,zone:"Far west",items:["Jaisalmer Fort","Havelis and old-town lanes","Desert activity if booked and conditions allow"]},
"Chittorgarh":{stay:1,zone:"South-east",items:["Chittorgarh Fort","Historic viewpoints and monuments","Flexible evening / early night"]},
"Mount Abu":{stay:2,zone:"South-west",items:["Nakki Lake area","Aravalli viewpoints","Check temple opening rules before planning visit"]},
"Ranthambore":{stay:2,zone:"South-east",items:["Pre-booked safari only if confirmed","Ranthambore Fort or a rest block","Keep plans flexible around official safari slots"]},
"Bundi":{stay:1,zone:"South-east",items:["Garh Palace area","Stepwells and old-town walk","Slow evening"]},
"Pushkar":{stay:1,zone:"Central",items:["Pushkar Lake surroundings","Brahma Temple area, observe local etiquette","Bazaar walk and rest"]},
"Ajmer":{stay:1,zone:"Central",items:["Ajmer Sharif area, observe visitor guidance","Ana Sagar Lake","Local food and rest"]},
"Bikaner":{stay:1,zone:"North-west",items:["Junagarh Fort","Old-city sights","Flexible afternoon"]},
"Alwar":{stay:1,zone:"North-east",items:["City sights and local heritage","Check current access for nearby sites","Keep the evening open"]}
};
const $=id=>document.getElementById(id);
function getRoute(){return Array.from(document.querySelectorAll("#route li strong")).map(x=>x.textContent.replace(/^\d+\.\s*/,"").trim()).filter(n=>PLACES[n])}
function getDays(){const n=Number($("days")&&$("days").value)||3;return Math.max(1,Math.min(30,n))}
function getPeople(){const n=Number($("people")&&$("people").value)||1;return Math.max(1,Math.min(20,n))}
function safeName(n){return String(n).replace(/[&<>"]/g,ch=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[ch]))}
function parseDateValue(value){if(!/^[0-9]{4}-[0-9]{2}-[0-9]{2}$/.test(value||""))return null;const parts=value.split("-").map(Number);const date=new Date(parts[0],parts[1]-1,parts[2],12);return date.getFullYear()===parts[0]&&date.getMonth()===parts[1]-1&&date.getDate()===parts[2]?date:null}
function formatPlanDate(offset){const start=parseDateValue($("startDate")&&$("startDate").value);if(!start)return "";const date=new Date(start.getFullYear(),start.getMonth(),start.getDate()+offset,12);return date.toLocaleDateString("en-IN",{weekday:"short",day:"numeric",month:"short"})}
function fullDate(value){const date=parseDateValue(value);return date?date.toLocaleDateString("en-IN",{day:"numeric",month:"short",year:"numeric"}):""}
function makePlan(){
 const route=getRoute(),selectedDays=getDays(),people=getPeople(),daily=Number($("daily")&&$("daily").value)||0;
 const startDate=parseDateValue($("startDate")&&$("startDate").value),endDate=parseDateValue($("endDate")&&$("endDate").value);
 const container=$("timeline"),summary=$("itinerarySummary");
 if(!route.length){summary.textContent="Add one or more destinations above to generate a day-by-day draft.";container.innerHTML='<div class="itinerary-day"><div class="day-tag">Ready</div><div><h3>Your first route is waiting</h3><p>Add Jaipur, Jodhpur, Udaipur or another stop in the destination notebook to get a plan here.</p></div></div>';return}
 const nightInputs=Array.from(document.querySelectorAll("[data-nights]"));
 const nightsByCity={};
 route.forEach(name=>{const input=nightInputs.find(el=>el.dataset.nights===name);nightsByCity[name]=Math.max(0,Math.min(14,Number(input&&input.value)||0))});
 const plannedNights=route.reduce((sum,name)=>sum+nightsByCity[name],0);
 const expectedNights=startDate&&endDate
   ?Math.max(0,Math.round((Date.UTC(endDate.getFullYear(),endDate.getMonth(),endDate.getDate())-Date.UTC(startDate.getFullYear(),startDate.getMonth(),startDate.getDate()))/86400000))
   :Math.max(0,selectedDays-1);
 const minimumComfortableDays=route.length===1?1:(2*route.length);
 const advice=selectedDays<route.length
   ?"Fast-paced: there are fewer selected days than stops. The itinerary adds a minimum day per stop; increase the trip length or remove stops."
   :(selectedDays<minimumComfortableDays
     ?"Fast-paced draft: "+minimumComfortableDays+" days is a calmer starting point for this many stops because transfer days need time too."
     :"Review the overnight allocations against your actual transport bookings.");
 const daysPerStop=route.map(name=>Math.max(1,nightsByCity[name]));
 if(route.length===1){
   daysPerStop[0]=Math.max(1,nightsByCity[route[0]]+1);
 }else if(plannedNights>0){
   daysPerStop[daysPerStop.length-1]+=1;
 }
 const allocatedDays=daysPerStop.reduce((sum,n)=>sum+n,0);
 const days=Math.max(selectedDays,allocatedDays,route.length);
 if(days>allocatedDays)daysPerStop[daysPerStop.length-1]+=days-allocatedDays;
 const allocation=[];
 daysPerStop.forEach((count,idx)=>{for(let n=0;n<count;n++)allocation.push(idx)});
 while(allocation.length<days)allocation.push(route.length-1);
 allocation.length=days;
 const dateSummary=startDate?" Dates: "+fullDate($("startDate").value)+(endDate?" – "+fullDate($("endDate").value):" (end date not set)")+".":"";
 const nightAdvice=plannedNights===expectedNights
   ?"Overnight plan matches the "+expectedNights+" expected night"+(expectedNights===1?"":"s")+"."
   :plannedNights>expectedNights
     ?"Overnight plan is "+(plannedNights-expectedNights)+" night"+(plannedNights-expectedNights===1?"":"s")+" longer than the trip window. Reduce nights or extend the dates before booking."
     :"Overnight plan is short by "+(expectedNights-plannedNights)+" night"+(expectedNights-plannedNights===1?"":"s")+". Allocate the remaining nights to a stop before booking.";
 const overrun=startDate&&endDate&&days>selectedDays
   ?" The generated outline runs beyond the selected end date. Shorten the overnight plan or extend your trip dates."
   :"";
 summary.textContent=route.length+" stop"+(route.length===1?"":"s")+" · "+days+" itinerary day"+(days===1?"":"s")+" · "+plannedNights+" planned night"+(plannedNights===1?"":"s")+" / "+expectedNights+" expected. Budget estimate: ₹"+Math.round(selectedDays*people*daily).toLocaleString("en-IN")+". "+advice+" "+nightAdvice+dateSummary+overrun;
 let html="",last=-1;
 for(let i=0;i<days;i++){
  const idx=allocation[i],place=route[idx],data=PLACES[place]||{zone:"Rajasthan",items:["Choose one local highlight","Leave time for food and rest","Check opening hours before visiting"]};
  const changing=i>0&&idx!==last;
  let morning,afternoon,evening,headline,meta;
  if(i===0){headline="Arrive in "+place;meta=data.zone+" · arrival day";morning="Arrival, transfer to stay and check-in";afternoon="Easy first look: "+data.items[0];evening="Nearby dinner and rest; don't overbook";}
  else if(changing){const previous=route[last];headline=previous+" → "+place;meta="Transfer day · "+data.zone;morning="Travel to "+place+"; verify the current route and departure";afternoon="Check in, hydrate and choose one nearby sight";evening="Keep this evening flexible";}
  else {headline=place;meta=data.zone+" · explore at a slower pace";morning=data.items[0];afternoon=data.items[1]||"Choose one local highlight";evening=data.items[2]||"Free time, food and rest";}
  if(i>0&&!changing&&i===days-1){morning=data.items[0];afternoon=data.items[1]||"Local exploration";evening="Pack and prepare for onward travel";}
  const datedLabel=formatPlanDate(i);const dateTag=datedLabel?'<span>'+safeName(datedLabel)+'</span>':"";html+='<article class="itinerary-day"><div class="day-tag">Day '+(i+1)+dateTag+'</div><div><h3>'+safeName(headline)+'</h3><p>'+safeName(meta)+(changing?' · transfer kept light':'')+'</p><div class="day-stops"><div class="day-stop"><strong>Morning</strong><span>'+safeName(morning)+'</span></div><div class="day-stop"><strong>Afternoon</strong><span>'+safeName(afternoon)+'</span></div><div class="day-stop"><strong>Evening</strong><span>'+safeName(evening)+'</span></div></div></div></article>';
  last=idx;
 }
 container.innerHTML=html;
}
async function copyPlan(){
 const route=getRoute(),days=getDays(),people=getPeople(),daily=Number($("daily")&&$("daily").value)||0;
 const lines=["Rajasthan Routes — trip draft","Route: "+route.join(" → "),"Nights per stop: "+route.map(name=>{const input=Array.from(document.querySelectorAll("[data-nights]")).find(el=>el.dataset.nights===name);return name+" — "+(input?input.value:"0")+" night(s)"}).join(", "), "Start date: "+($("startDate").value||"Not set"), "End date: "+($("endDate").value||"Not set"),"Selected days: "+days,"Travellers: "+people,"Budget estimate: ₹"+Math.round(days*people*daily).toLocaleString("en-IN"),""];
 for(const el of document.querySelectorAll("#timeline .itinerary-day")){const parts=(el.innerText||el.textContent).split("\n").filter(Boolean);lines.push(parts.join(" | "))}
 const text=lines.join("\n"),button=$("itineraryCopy"),original=button.textContent;
 try{
   if(!navigator.clipboard||!navigator.clipboard.writeText)throw new Error("Clipboard unavailable");
   await navigator.clipboard.writeText(text);
   button.textContent="Plan copied";
 }catch(error){
   const blob=new Blob([text],{type:"text/plain;charset=utf-8"}),a=document.createElement("a");
   a.href=URL.createObjectURL(blob);a.download="rajasthan-day-by-day-plan.txt";document.body.appendChild(a);a.click();
   setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove()},500);
   button.textContent="Plan downloaded";
 }
 setTimeout(()=>{button.textContent=original},1800);
}
$("itineraryCopy").addEventListener("click",copyPlan);
["days","people","daily","startDate","endDate"].forEach(id=>{const el=$(id);if(el)el.addEventListener("input",makePlan)});window.addEventListener("rr:dates-changed",makePlan);window.addEventListener("rr:nights-changed",makePlan);
const routeNode=$("route");if(routeNode&&typeof MutationObserver!=="undefined")new MutationObserver(makePlan).observe(routeNode,{childList:true,subtree:true});
makePlan();
})();