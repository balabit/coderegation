---
speaker: Bjarne Stroustrup
topic: Writing Good C++14
video: https://www.youtube.com/watch?v=1OEu9C51K2A
---

How do we use C++14 to make our code better, rather than just different? How do we do so on a grand scale, rather than just for exceptional programmers? We need guidelines to help us progress from older styles, such as “C with Classes”, C, “pure OO”, etc. We need articulated rules to save us from each having to discover them for ourselves. Ideally, they should be machine-checkable, yet adjustable to serve specific needs.

In this talk, I describe a style of guidelines that can be deployed to help most C++ programmers. There could not be a single complete set of rules for everybody, but we are developing a set of rules for most C++ use. This core can be augmented with rules for specific application domains such as embedded systems and systems with stringent security requirements. The rules are prescriptive rather than merely sets of prohibitions, and about much more than code layout. I describe what the rules currently cover (e.g., interfaces, functions, resource management, and pointers). I describe tools and a few simple classes that can be used to support the guidelines.

The core guidelines and a guideline support library reference implementation will be open source projects freely available on all major platforms (initially, GCC, Clang, and Microsoft).

[Presentation Slides, PDFs, Source Code and other presenter materials are available](https://github.com/isocpp/CppCoreGuidelines/blob/master/talks/Stroustrup%20-%20CppCon%202015%20keynote.pdf)

