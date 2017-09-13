---
speaker: Wojciech Turek
topic: Erlang-based Desynchronised Urban Traffic Simulation for High-Performance Computing Systems
video: https://www.youtube.com/watch?v=SewI3BK64wg
issue: 117
---

The problem of micro-scale urban traffic simulation of large environments poses a great opportunity for utilisation of HPC systems. Parallel implementation of this kind of computation, where complex, data-intensive processing has to be synchronised, is not straightforward. The simulation presented in this paper is based on a concept of controlled desynchronisation of the computations, which does not violate the model. The implementation in Erlang language uses Erlang distribution mechanisms for building and managing the computing cluster. Conducted experiments show linear scalability of the method up to 19200 computing cores.

