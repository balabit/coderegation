---
speaker: Daniel Gruss
topic: Microarchitectural Incontinence - You would leak too if you were so fast!
video: https://www.youtube.com/watch?v=cAWmNp3Ukqk
issue: 137
---

Modern computer systems are insanely fast. Crucial for performance improvements is the reduction of the structure size and the optimization of instructions even on a sub-cycle scale. Consequently, computer systems leak: DRAM cells leak their charge and CPUs leak their internal state. We will discuss examples of optimizations that might not be so optimal from a security perspective. These examples will include Rowhammer and several microarchitectural side-channel attacks. We will see how user data and even entire systems can be comprised through simple attacks from unprivileged programs. Such attacks are easy to write from scratch within a few hours with no prior experience in the field.

