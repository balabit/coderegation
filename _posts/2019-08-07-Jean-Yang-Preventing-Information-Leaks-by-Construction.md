---
speaker: Jean Yang
topic: Preventing Information Leaks by Construction
video: https://www.youtube.com/watch?v=Y6lHNoWC7M8
issue: 185
---

The high-profile attacks and data-breaches of the last few years demonstrate the importance of securing software. While there are ever more tools that can analyze systems for vulnerabilities, these do not help the programmer write secure code in the first place. To prevent security from becoming a bottleneck–and to prevent expensive security mistakes from becoming increasingly probable–we need to make it easier to write provably secure software.

My work on policy-agnostic programming addresses the issue of unintentional information leaks by factoring out the implementation of information flow security from other functionality. In this paradigm, programmers specify policies about how sensitive data may be used directly with the data, instead of as conditional checks across a program. In this talk, I present dynamic and static approaches for policy-agnostic programming, show how to extend these approaches to support database-backed web applications, and discuss how the policy-agnostic approach can help us secure legacy code written in existing languages.

