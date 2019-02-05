---
speaker: Austin Bingham
topic: Python refactoring with Rope and Traad
video: https://www.youtube.com/watch?v=NvV5OrVk24c
issue: 163
---

Rope is a powerful Python refactoring library. Traad (Norwegian for "thread") is a tool which makes it simpler to integrate rope into IDEs via a simple HTTP API. In this session we'll look at how traad and rope work together and how traad integrates with at least one popular editor.

Python is a modern, dynamic language which is growing in popularity, but tool support for it is sometime lacking or only available in specific environments. For refactoring and other common IDE functions, however, the powerful open-source rope library provides a set of tools which are designed to be integrated into almost any programming environment. Rope supports most common refactorings, such as renaming and method extraction, but also more Python-specific refactorings, such as import organization. Rope’s underlying code analysis engine also allows it to do things like locating method definitions and generating auto-completion suggestions.

While rope is designed to be used from many environments, it’s not always easy or ideal to integrate rope directly into other programs. Traad (Norwegian for “thread”) is another open-source project that addresses this problem by wrapping rope into a simple client-server model so that client programs (IDEs, editors, etc.) can perform refactorings without needing to embed rope directly. This simplifies dependencies, makes clients more robust in the face of errors, eases traad client development, and even allows clients to do things like switch between Python 2 and 3 refactoring in the same session.

In this session we’ll look at how rope operates, and we’ll see how traad wraps it to provide an easier integration interface. The audience will get enough information to start using rope themselves, either directly or via traad, and they’ll see how to use traad for integrating rope into their own environments. More generally, we’ll look at why client-server refactoring tools might be preferable to the more standard approach of direct embedding.

