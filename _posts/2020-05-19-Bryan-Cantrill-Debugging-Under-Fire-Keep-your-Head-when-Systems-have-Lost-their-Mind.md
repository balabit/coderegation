---
speaker: Bryan Cantrill
topic: Debugging Under Fire - Keep your Head when Systems have Lost their Mind
video: https://www.youtube.com/watch?v=30jNsCVLpAE
issue: 225
---

As software is increasingly developed to be deployed as part of a service, the manifestations of defects have changed: the effects of broken software are increasingly unlikely to be felt by merely one user, but many (or even all) -- with concomitant commercial consequences. Debugging service outages puts everyone in an uncomfortable spot: operators must learn how to deal with the uncertainties of broken snowflakes, while developers must adapt their debugging techniques to the constraints of a production environment. And in all but the most immature systems, service outage denotes cascading failure: there is not one bug but several -- often in different components that are interacting in unforeseen ways.
These technical complexities coupled with the high visibility of a downed service can lead to stress, confusion and (in the worst cases), panic.

In this talk, we will address debugging during an outage, looking at not only specific technical challenges (and techniques to address them), but also the psychology, team dynamics and organizational challenges of debugging under fire.

