---
speaker: Austin Bingham
topic: Mutation Testing in Python
video: https://www.youtube.com/watch?v=jwB3Nn4hR1o
issue: 86
---

Mutation testing is a technique for systematically mutating source code in order to validate test suites. It makes small changes to a program’s source code and then runs a test suite; if the test suite ever succeeds on mutated code then a flag is raised. I’ll begin this talk with a description of the theory behind mutation testing, and then I’ll move into an analysis of Cosmic Ray, a tool for mutation testing in Python. While some of the details of this talk will necessarily be Python-specific, the concepts and lessons are broadly applicable and should be interesting to anyone involved in producing software.

