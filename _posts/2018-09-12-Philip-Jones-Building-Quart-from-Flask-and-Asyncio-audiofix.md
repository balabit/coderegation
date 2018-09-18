---
speaker: Philip Jones
topic: Building Quart from Flask and Asyncio audiofix
video: https://www.youtube.com/watch?v=EgpQcLy1kf0
issue: 173
---

Flask is a great web mirco-framework, that is best utilised with event-loop concurrency. Sadly with Flask the event-loop framework can’t be asyncio, although some extensions (Flask-Aiohttp) have tried. Quart is the solution as it shares the Flask API and is based on asyncio. In addition Quart goes beyond Flask adding HTTP/2 and websockets.

This talk will outline why event-loop concurrency is a good choice for web servers, why asyncio is a good choice and then give an overview of Quart, demonstrating features that go beyond the Flask framework.

