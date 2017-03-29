---
speaker: Kevlin Henney
topic: Functional C++
video: https://vimeo.com/131640207
issue: 44
---

Functional C++? As opposed to what - dysfunctional? Well, kind of, yeah. Sure, in C++ the principal unit of composition is called a function, but that doesn't mean it's a functional language. And the idea of restricting mutability of state gets a nod with const, but it's a nod not a hug. And the STL shows influences of functional programming, although it falls short of being compositional. And, yes, sure, C++11 has lambdas, but then again, these days, who doesn't? Lambda calculus was invented in the 1930s.

This talk looks at how to express functional programming ideas in (post)modern C++ in a way that can be considered idiomatic to C++, rather than trying to use the power of overloading and metaprogramming to pretend C++ is Haskell or Lisp. In short, immutability beyond const and into shared and persistent data structures, concurrency beyond threading and locks, and thinking about functions as transformations and units of composition rather than actions.

