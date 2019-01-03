---
speaker: Trammell Hudson
topic: Modchips of the State
video: https://www.youtube.com/watch?v=C7H3V7tkxeA
issue: 184
---

Hardware implants and supply chain attacks have been in the news recently, but how feasible are they and what can we do about them?

We don't know how much of the Bloomberg story about hardware implants installed in Supermicro servers shipped to Apple and Amazon is true, nor do we know the story behind the story and the reasons for the vehement denials by all the parties involved.

However, a technical assessment of details of the described implants reveals that a supply chain attack on the hardware is definitely possible, that the capabilities of the BMC can be used to bypass OS protections, and that there are means to access the BMC that would not necessarily generate readily identified network traffic.

In this talk we'll examine the design of a proof of concept SPI bus hardware implant that has similar capabilities to those described in the Bloomberg/Supermicro article as well as some countermeasures that we can use to try to detect these "modchips" and increase our trust in our systems.
