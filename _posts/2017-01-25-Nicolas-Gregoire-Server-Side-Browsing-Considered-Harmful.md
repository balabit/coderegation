---
speaker: Nicolas Gregoire
topic: Server-Side Browsing Considered Harmful
video: https://www.youtube.com/watch?v=8t5-A4ASTIU
issue: 30
---

SSRF vulnerabilities (aka CWE-918) allows attackers to submit arbitrary URL to vulnerable applications, and have the application (or one of its components) browse this URL. The talk describes my latest findings regarding this narrow field of AppSec. Of course, being under NDA during my penetration tests, I'll only covering bugs reported to bounties programs. That includes Yahoo, Facebook, Prezi, PayPal, Stripe, CoinBase, and more!

6 sections:

 * Goal: SSRF-like vulnerabilities in bounties programs
 * Vectors: WebHooks, export features, API explorers, ...
 * Targets: local, multicast and private destinations
 * Blacklists: the 20+ ways to express an IP address
 * Bugs: contexts, exploits, impacts and rewards
 * Toolbox: custom scripts and public resources

Highlights: I was able to compromise some large service providers and earned around 50,000$ for that. Several blacklists were bypassed using little-known quirks in the parsing of URL.

