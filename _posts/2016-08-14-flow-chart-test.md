---
layout: post
title:  "flow test"
category: [compile]
tags: [g++, linking, linux]
---

```flow
st=>start: Start:>http://alfred-sun.github.io
io=>inputoutput: verification
op=>operation: Your Operation
cond=>condition: Yes or No?
sub=>subroutine: Your Subroutine
e=>end:>https://github.com/adrai/flowchart.js

st->io->op->cond
cond(yes)->e
cond(no)->sub->io
```
