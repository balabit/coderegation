---
speaker: Yunong Xiao
topic: Slaying Monoliths with Docker and Node.js, a Netflix Original
video: https://www.youtube.com/watch?v=B90OabhYJpA
issue: 61
---

At Netflix, our data access platform is at the heart of nearly every request from our subscribers. It enables our innovative UIs to efficiently communicate with our bevy of backend services while growing our subscriber base to 75 million members. As a result of this scale, this monolithic platform requires ever increasing resources to run and maintain, both in terms of hardware (32 vCPUs per instance) and developer productivity (try running that on your laptop!). As we continue to grow and expand our subscriber base globally (#netflixeverywhere), we need to fundamentally change the monolithic design of our platform.

In this talk, I will discuss the new container based data access platform that’s replacing the monolith. See how the architecture of this cross cutting project allows us to build isolated microservices with Node.js and Docker. Examine the tools and infrastructure we’re building across our stack that enable engineers to effortlessly build, debug, test and their code on this platform anywhere -- whether it’s locally on your laptop, or remotely in the cloud -- all made possible thanks to Docker.


