---
speaker: Emery Berger
topic: Performance Matters
video: https://www.youtube.com/watch?v=r-TLSBdHe1A
issue: 206
---


Performance clearly matters to users. For example, the most common software update on the AppStore is "Bug fixes and performance enhancements." Now that Moore's Law has ended, programmers have to work hard to get high performance for their applications. But why is performance hard to deliver?

I will first explain why current approaches to evaluating and optimizing performance don't work, especially on modern hardware and for modern applications. I then present two systems that address these challenges. Stabilizer is a tool that enables statistically sound performance evaluation, making it possible to understand the impact of optimizations and conclude things like the fact that the -O2 and -O3 optimization levels are indistinguishable from noise (sadly true).

Since compiler optimizations have run out of steam, we need better profiling support, especially for modern concurrent, multi-threaded applications. Coz is a new "causal profiler" that lets programmers optimize for throughput or latency, and which pinpoints and accurately predicts the impact of optimizations. Coz's approach unlocks previously unknown optimization opportunities. Guided by Coz, we improved the performance of Memcached (9%), SQLite (25%), and accelerated six other applications by as much as 68%; in most cases, this involved modifying less than 10 lines of code and took under half an hour (without any prior understanding of the programs!). Coz now ships as part of standard Linux distros (apt install coz-profiler).

