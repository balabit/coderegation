---
speaker: Matthew McCullough
topic: Advanced Git - Graphs, Hashes, and Compression, Oh My!
video: https://www.youtube.com/watch?v=ig5E8CcdM9g
issue: 143
---

The San Francisco Java User Group recently had the pleasure of inviting GitHub's Matthew McCullough back to give us a more advanced tour of this source code management tool. As evidenced by his riveting talk, Matthew's excellent command of the Git infrastructure speaks for itself:

Git is a version control system. We can look at it from that high level. Git is a content tracking system. Some teachers advise us to look at it from that lowered elevation. But I will take you to the very bottom. The floor. The code. The algorithms. The directed acyclic graph of hashed bit sequences made efficient through LZW compression and deferred garbage collection determined by node reachability via hash relationships.

'But why?', you may ask. 'Why go this deep?' Git is a tool that works so well for so many. It mystically corrects anticipated "merge" conflicts. It's "where did code come from" results from "blame" are impressive. The ability to re-write history through "rebase" is awesome. The globally unique identifier nature of a hash-produced ref is revolutionary.

Uber-geeks are magic-slayers. We want and need to know precisely how things work. Like a hard 50 push-up workout, this study will make working with Git at the daily developer level a fraction of the effort — like a mere ten push-ups. Let's dig into the guts of Git.
