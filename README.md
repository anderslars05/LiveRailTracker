# LiveRailTracker

🧱 Recommended Tech Stack
🌐 Backend

Django – main framework

Django REST Framework – API endpoints

Celery + Redis – background tasks for fetching live rail data (every few seconds)

PostgreSQL – best DB for geospatial & relational train data

Channels – WebSockets for live train movement updates

GeoDjango – for map overlays, routes, signal diagrams

🗺️ Mapping

Leaflet.js – main map viewer (simple, fast)

Mapbox/OpenLayers – option for more complex railway overlays

OpenRailwayMap data – for track layout + signalling

🚆 Live Train Tracking Logic

Depending on the country, possible data sources:

For UK:

Darwin – realtime arrivals/departures

TD feed – signalling berths / train describer

TRUST – running data & delays

Network Rail Open Data – timetable, routes, locations

You’ll need background tasks + WebSockets to stream this into the UI.

🧩 Architecture Overview
Users <--> Django (views + templates)
       <--> Django REST API
       <--> WebSockets (live train updates)
Celery workers:
    - Fetch data constantly
    - Parse rail feeds
    - Update database
    - Push live updates
PostgreSQL <--> Django ORM
Redis <--> Celery + WebSocket channels
Leaflet.js maps <--> custom overlays (tracks/signals)


This setup can handle:

Thousands of trains

Live signal movements

Historical playback

Live maps with overlays

User-generated alerts/pinning/watching trains