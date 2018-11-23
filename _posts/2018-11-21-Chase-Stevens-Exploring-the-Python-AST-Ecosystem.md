---
speaker: Chase Stevens
topic: Exploring the Python AST Ecosystem
video: https://www.youtube.com/watch?v=Yq3wTWkoaYY
issue: 179
---

Materials are available at https://github.com/hchasestevens/europython-2018

This session will introduce attendees to Python's rich ecosystem of abstract syntax tree tooling and libraries, with an emphasis on practical applications in static analysis and metaprogramming. Attendees should be fully comfortable with Python syntax and semantics, but familiarity with the ast module itself will not be necessary.

The talk will begin with a conceptual overview of ASTs, including a brief look at Python's built-in introspection capabilities. It will introduce tools for AST visualization (astor, showast, python-ast-explorer), creation (asttools, meta), and transformation to source code (codegen).

How the AST can be used for static analysis will be covered; this will include discussion of Python's built-in facilities (NodeVisitor) as well as of the 3rd party tools astsearch, astpath, and bellybutton. The talk will demonstrate the advantages and limits of these tools in comparison to other static analysis tooling (pylint, mypy); particular attention will be paid to how these tools can be incorporated into attendees' workflows and existing codebases and projects.

Tooling for Python AST manipulation and metaprogramming will be the final topic covered, focusing on the use of the NodeTransformer built-in. The talk will cover practical applications and examples of metaprogramming, such as metaprogramming for DSLS (pony, xpyth), runtime code manipulation (patterns, yield-from), and others (e.g. assertion rewriting in pytest).

While the talk will touch only briefly on each of the applications discussed, by the end of the session attendees should have a firm grasp of the kinds of problems the AST can be used to solve, what existing AST tooling can accomplish, and what resources are available for the development of their own AST tools.

