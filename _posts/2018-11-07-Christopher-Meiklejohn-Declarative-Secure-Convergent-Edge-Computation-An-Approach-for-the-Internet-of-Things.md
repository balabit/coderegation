---
speaker: Christopher Meiklejohn
topic: Declarative, Secure, Convergent Edge Computation - An Approach for the Internet of Things
video: https://vimeo.com/191485103
issue: 178
---

Consistency is hard and coordination is expensive. As we move into the world of connected 'Internet of Things' style applications, or large-scale mobile applications, devices have less power, periods of limited connectivity, and operate over unreliable asynchronous networks. This poses a problem with shared state: how do we handle concurrent operations over shared state, while clients are offline, and ensure that values converge to a desirable result without making the system unavailable?

We look at a new programming model, called Lasp. This programming model combines distributed convergent data structures with a dataflow execution model designed for distribution over large-scale applications. This model supports arbitrary placement of processing

Note: this enables the user to author applications that can be distributed across data centers and pushed to the edge. In this talk, we will focus on the design of the language and show a series of sample applications.

