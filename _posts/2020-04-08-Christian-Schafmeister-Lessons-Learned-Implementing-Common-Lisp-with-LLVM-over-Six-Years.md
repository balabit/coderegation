---
speaker: Christian Schafmeister
topic: Lessons Learned Implementing Common Lisp with LLVM over Six Years
video: https://www.youtube.com/watch?v=mbdXeRBbgDM
issue: 209
---

I will present the lessons learned while using LLVM to efficiently implement a complex memory managed, dynamic programming language within which everything can be redefined on the fly. I will present Clasp, a new Common Lisp compiler and programming environment that uses LLVM as its back-end and that interoperates smoothly with C++/C. Clasp is written in both C++ and Common Lisp. The Clasp compiler is written in Common Lisp and makes extensive use of the LLVM C++ API and the ORC JIT to generate native code both ahead of time and just in time. Among its unique features, Clasp uses a compacting garbage collector to manage memory, incorporates multithreading, uses C++ compatible exception handling to achieve stack unwinding and an incorporates an advanced compiler written in Common Lisp to achieve performance that approaches that of C++. Clasp is being developed as a high-performance scientific and general purpose programming language that makes use of available C++ libraries.

Discussion
----------
There is some really impressive stuff discussed in this talk! We were a bit surprised at first about the choice of Lisp, as one would think that a SciPy/NumPy/Pandas/etc. based stack would be an easy to learn and powerful general purpose scientific toolchain (or more generally, a C/C++ and Python based stack can be really powerful for a wide variety of problems where performance and a convenient high-level programming language are needed), but the arguments were convincing about the complexities and the performance penalties that Python introduces.

