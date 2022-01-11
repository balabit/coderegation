---
speaker: Matthew Podwysowski
topic: Asynchronous JavaScript at Netflix
video: https://www.youtube.com/watch?v=a8W5VVGO-jA
issue: 85
---

What’s does a mouse drag event have in common with an Array of numbers?
The answer to this question may surprise you: they are both collections.

This key insight holds the key to dramatically simplifying asynchronous programming in JavaScript. In this talk you will learn how you can use the familiar JavaScript Array methods to create surprisingly expressive asynchronous programs.

Using just a few functions, you will learn how to do the following:

 * Declaratively build complex events out of simple events (ex. drag n’ drop)
 * Coordinate and sequence multiple Ajax requests
 * Reactively update UI’s in response to data changes
 * Eliminate memory leaks caused by neglecting to unsubscribe from events
 * Gracefully propagate and handle asynchronous exception

In this talk we’ll be exploring the Reactive Extensions (RxJS) library, which allows us to treat events as collections. You’ll learn about how Netflix uses Rx on the client and the server, allowing us to build end-to-end reactive systems. We’ll also contrast Rx with Promises, another popular approach to building asynchronous programs in JavaScript.

