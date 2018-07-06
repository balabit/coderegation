---
speaker: Malte Ubl
topic: Designing very large JavaScript applications
video: https://www.youtube.com/watch?v=ZZmUwXEiPm4
issue: 166
---

Over the last years a modular approach to programming in JS gained a huge following and with the advent of virtual DOM building isomorphic JavaScript application for the web became dramatically more approachable; yet, we are still largely deploying monolithic application blobs that know how to render the settings page of our single page apps before accepting user input on the homepage.

My talk will explore 2 primary themes:

- How to build highly sophisticated web apps that load a constant amount of JS to make the first page the user sees interactive; where constant means, even if you have 100s of engineers write code for your app for a year, the size will still be the same.
- How to throughout the lifecycle of your application never load a single line of JS that is not currently needed.

As part of this exploration I will introduce 3 novel concepts: lazy decoration, asynchronous dependency injection and reverse dependencies in module systems.

Come see my talk if you enjoy nerding out on over-engineering problems, or want to build the next YouTube or Twitter.

The talk is also available in a [written form on Medium](https://medium.com/@cramforce/designing-very-large-javascript-applications-6e013a3291a3).
