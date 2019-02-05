---
speaker: Kostis Sagonas
topic: Testing and Verifying Chain Repair Protocols using Concuerror
video: https://www.youtube.com/watch?v=WWBDUpmCUsI
issue: 180
---

Debugging concurrent programs is often quite hard. There is lament about how difficult it is to reproduce a known bug, a lot of guessing about the exact causes and often one has to settle with a fix that "may not completely solve the problem".

Concuerror is a tool designed to make the process of finding, reproducing and fixing such bugs easy: given any Erlang program as input, it explores all interleavings of the processes involved, focusing smartly on pairs of "racing" events and even popping hints about what the user can do to make the search more effective. If any process crashes, Concuerror will print a detailed log of the events that lead up to the crash and will also allow the developer to visually explore the interleaving.

You may have already seen one some video or tutorial on what Concuerror can do on some (small) programs. However, this tutorial will go deeper. After explaining what Concuerror can do for testing concurrent programs, we will also describe how one can use the tool to model, test and verify distributed protocols. Special emphasis will be given on what a user can do to use the tool most effectively.

More info on Concuerror: http://parapluu.github.io/Concuerror

