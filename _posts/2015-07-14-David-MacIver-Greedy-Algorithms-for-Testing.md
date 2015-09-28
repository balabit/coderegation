---
speaker: David MacIver
topic: Greedy Algorithms for Testing
video: https://skillsmatter.com/skillscasts/6461-greedy-algorithms-for-testing
---

Testing libraries like Quickcheck generate random data to break tests, then greedily apply a simplification function to prune them down to more legible examples.

This approach works well for small examples and fast tests, but as you move out of that area it starts to break down. In this talk I show how simple alternations to the greedy algorithm and some clever choices of simplification can drastically improve performance and example quality at the same time.
