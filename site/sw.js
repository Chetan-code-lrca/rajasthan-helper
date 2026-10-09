const CACHE="rajasthan-routes-v12";
const ASSETS=["./","./index.html","./404.html","./manifest.webmanifest","./icon.svg","./trip-intelligence.css","./trip-intelligence.js","./itinerary.css","./itinerary.js"];
self.addEventListener("install",event=>{
  event.waitUntil(caches.open(CACHE).then(cache=>cache.addAll(ASSETS)).then(()=>self.skipWaiting()));
});
self.addEventListener("activate",event=>{
  event.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(key=>key!==CACHE).map(key=>caches.delete(key)))).then(()=>self.clients.claim()));
});
self.addEventListener("fetch",event=>{
  if(event.request.method!=="GET"||new URL(event.request.url).origin!==self.location.origin)return;
  event.respondWith(caches.match(event.request).then(cached=>{
    if(cached)return cached;
    return fetch(event.request).then(response=>{
      if(response.ok&&response.type==="basic"){
        const copy=response.clone();
        caches.open(CACHE).then(cache=>cache.put(event.request,copy));
      }
      return response;
    }).catch(()=>{
      if(event.request.mode==="navigate")return caches.match("./");
      return new Response("Offline: this resource is not cached yet.",{status:503,headers:{"Content-Type":"text/plain; charset=utf-8"}});
    });
  }));
});
