---
speaker: Bryan Cantrill
topic: Zebras all the way down - The engineering challenges of the data path
video: https://www.youtube.com/watch?v=fE2KDzZaxvE
issue: 224
---

Much attention is rightfully devoted to the development and deployment of stateless services, but these services are not themselves devoid of persistent state; rather, they rely on other services to manage this state for them. This data path, however -- that stack of software that is emphatically not stateless, being responsible for distributed and/or persistent state -- is entirely different in its constraints and failure modes. This software takes years or even decades to get right, can be arduous to upgrade, and -- even in a post-cloud era -- lives and dies by the fickle whims of hardware and firmware. This talk will reflect on two decades of building the data path, from the dawn of storage networking through modern cloud storage services.

