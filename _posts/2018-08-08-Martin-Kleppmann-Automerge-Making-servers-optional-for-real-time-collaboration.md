---
speaker: Martin Kleppmann
topic: Automerge - Making servers optional for real-time collaboration
video: https://www.youtube.com/watch?v=PHz17gwiOc8
issue: 169
---

Once upon a time, we used software that ran on our own computers, that worked offline, and that stored its data in files on the local disk. Then we decided to put it all in the cloud. We gained some great features: real-time collaboration, like in Google Docs, for example. But we also lost control of our own data, and became dependent on far-away servers to allow us to access the data that we created.

Automerge is part of an effort to get the best of both worlds. It is a JavaScript library for building real-time collaborative applications. However, apps built with Automerge also work offline, storing data locally, and synchronise their data with collaborators whenever a network is available. And although you can use it with servers, you don’t have to: synchronisation also works peer-to-peer, or via any network you choose.

In this talk we will explore how Automerge deals with different users independently modifying shared data in a collaborative application (hint: by merging the changes... automatically!), how it achieves consistency in highly distributed settings, and where it is heading in the future.

