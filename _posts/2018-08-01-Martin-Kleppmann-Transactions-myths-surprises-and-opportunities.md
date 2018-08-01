---
speaker: Martin Kleppmann
topic: Transactions - myths, surprises and opportunities
video: https://www.youtube.com/watch?v=5ZjhNTM8XU8
issue: 149
---

Back in the 1970s, the earliest databases had transactions. Then NoSQL abolished them. And now, perhaps, they are making a comeback... but reinvented.

The purpose of transactions is to make application code simpler, by reducing the amount of failure handling you need to do yourself. However, they have also gained a reputation for being slow and unscalable. With the traditional implementation of serializability (2-phase locking), that reputation was somewhat deserved.

In the last few years, there has been a resurgence of interest in transaction algorithms that perform well and scale well. This talk answers some of the biggest questions about the bright new landscape of transactions:

What does ACID actually mean? What race conditions can you get with weak isolation (such as "read committed" and "repeatable read"), and how does this affect your application?
What are the strongest guarantees we can achieve, while maintaining high availability and high performance at scale?
How do the new generation of algorithms for distributed, highly-available transactions work?
Linearizability, session guarantees, "consistency" and the much-misunderstood CAP theorem -- what's really going on here?
When you move beyond a single database, e.g. doing stream processing, what are your options for maintaining transactional guarantees?

Martin Kleppmann is a software engineer and entrepreneur, and author of the O'Reilly book Designing Data-Intensive Applications (http://dataintensive.net), which analyses the data infrastructure and architecture used by internet companies. He previously co-founded a startup, Rapportive, which was acquired by LinkedIn in 2012. He is a committer on Apache Samza, and his technical blog is at http://martin.kleppmann.com.

