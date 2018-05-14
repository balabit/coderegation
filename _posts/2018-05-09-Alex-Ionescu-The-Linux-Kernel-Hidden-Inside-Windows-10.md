---
speaker: Alex Ionescu
topic: The Linux Kernel Hidden Inside Windows 10
video: https://www.youtube.com/watch?v=36Ykla27FIo
issue: 155
---

Initially known as "Project Astoria" and delivered in beta builds of Windows 10 Threshold 2 for Mobile, Microsoft implemented a full blown Linux 3.4 kernel in the core of the Windows operating system, including full support for VFS, BSD Sockets, ptrace, and a bonafide ELF loader. After a short cancellation, it's back and improved in Windows 10 Anniversary Update ("Redstone"), under the guise of Bash Shell interoperability. This new kernel and related components can run 100% native, unmodified Linux binaries, meaning that NT can now execute Linux system calls, schedule thread groups, fork processes, and access the VDSO!

As it's implemented using a full-blown, built-in, loaded-by-default, Ring 0 driver with kernel privileges, this not a mere wrapper library or user-mode system call converter like the POSIX subsystem of yore. The very thought of an alternate virtual file system layer, networking stack, memory and process management logic, and complicated ELF parser and loader in the kernel should tantalize exploit writers - why choose from the attack surface of a single kernel, when there's now two?

But it's not just about the attack surface - what effects does this have on security software? Do these frankenLinux processes show up in Procmon or other security drivers? Do they have PEBs and TEBs? Is there even an EPROCESS? And can a Windows machine, and the kernel, now be attacked by Linux/Android malware? How are Linux system calls implemented and intercepted?

As usual, we'll take a look at the internals of this entirely new paradigm shift in the Windows OS, and touch the boundaries of the undocumented and unsupported to discover interesting design flaws and abusable assumptions, which lead to a wealth of new security challenges on Windows 10 Anniversary Update ("Redstone") machines.
