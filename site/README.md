# Rajasthan Routes

A mobile-first, dependency-free travel companion built beside the original Rajasthan Helper CLI.

## What it helps with

- Search and filter destinations.
- Build, remove and reorder a route.
- Adjust trip dates, trip days, travellers and a planning budget.
- Calculate inclusive trip length from start/end dates, show calendar dates on the plan and provide broad seasonal reminders.
- Assign nights per destination, compare planned nights with the date window and flag under/over-allocation.
- Keep a draft in the current browser using local storage.
- Export/import a versioned JSON backup to move a draft between devices without an account.
- See a day-by-day skeleton that deliberately makes transfer days lighter.
- Check approximate distances for route pairs where the official Rajasthan Tourism pages publish a nearby-destination distance.
- Choose general travel tips for friends, family, couple or solo trips.
- Use a persistent pre-trip checklist.
- Open a route in Google Maps using origin, destination and waypoint parameters.
- Copy or save a simple text plan.
- Install the site as a web app and use its cached shell offline after the first successful load.

## Included destination starters

Jaipur, Udaipur, Ajmer, Jodhpur, Jaisalmer, Pushkar, Bikaner, Alwar, Chittorgarh, Mount Abu, Ranthambore and Bundi.

## Important boundary

This is a planning tool, not a booking engine or live travel-data service. Budget values are editable estimates. The route-distance panel is not a live road-distance or journey-time calculator. Nights per destination are user-editable planning values; the generated outline allocates days based on them and warns when the sum differs from the date window. The day-by-day schedule is still a starter template. Start/end dates determine inclusive duration and calendar labels, but they do not retrieve live weather, transport timetables, event calendars or availability. Seasonal prompts are broad reminders, not forecasts. Users should verify current transport schedules, accommodation prices, attraction hours, entry rules, weather and special-activity reservations before paying or travelling.

## Research basis

The planning guidance was reviewed against official Rajasthan sources on 8 October 2026:

- Rajasthan Tourism — Best Time to Visit: https://www.tourism.rajasthan.gov.in/best-time-to-visit.html
- Rajasthan Tourism — Tourist Destinations: https://www.tourism.rajasthan.gov.in/tourist-destinations.html
- Rajasthan Tourism — Jaipur: https://www.tourism.rajasthan.gov.in/jaipur.html
- Rajasthan Tourism — Pushkar: https://www.tourism.rajasthan.gov.in/pushkar.html
- Rajasthan Tourism — Jodhpur: https://www.tourism.rajasthan.gov.in/jodhpur.html
- Rajasthan Tourism — Jaisalmer: https://www.tourism.rajasthan.gov.in/jaisalmer.html
- Rajasthan Tourism — Udaipur: https://www.tourism.rajasthan.gov.in/udaipur.html
- Rajasthan Tourism — Chittorgarh: https://www.tourism.rajasthan.gov.in/chittorgarh.html
- Rajasthan Tourism — Bundi: https://www.tourism.rajasthan.gov.in/bundi.html
- Rajasthan Tourism — Ranthambore: https://www.tourism.rajasthan.gov.in/content/rajasthan-tourism/en/tourist-destinations/ranthambore.html
- RTDC — Travel Tips: https://rtdc.tourism.rajasthan.gov.in/Pages/TravelTips.aspx
- Rajasthan Tourism — Tourist Information Offices: https://www.tourism.rajasthan.gov.in/contact-us.html

Examples used in the UI include published nearby-destination distances such as Jaipur ↔ Pushkar (145 km), Pushkar ↔ Jodhpur (186 km), Jodhpur ↔ Jaisalmer (286 km), Jodhpur ↔ Udaipur (257 km) and Udaipur ↔ Chittorgarh (117 km). These values are planning context only and are not presented as live route calculations.

## Architecture

```text
site/
├── index.html
├── itinerary.css
├── itinerary.js
├── trip-intelligence.css
├── trip-intelligence.js
├── manifest.webmanifest
├── sw.js
├── icon.svg
└── 404.html
```

The main page keeps its base CSS/JS inline; the day-by-day planner and trip-intelligence features are in separate files. Static validation and DOM/Chromium test scripts live in `scripts/` at the repository root.

The original Python CLI under rajasthan_helper/ is intentionally outside this companion's changes.

## Publishing

Run `python scripts/validate_site.py` locally (Node.js must be installed) to check HTML IDs, local assets, inline JavaScript syntax, standalone JavaScript syntax and the manifest. GitHub Actions additionally runs jsdom interaction tests, Chromium desktop/mobile/offline tests, and a live public-URL check. GitHub Pages currently publishes the working branch root: the root `index.html` forwards visitors to `site/`, while the CI workflow validates the publication rather than deploying a second, competing artifact.