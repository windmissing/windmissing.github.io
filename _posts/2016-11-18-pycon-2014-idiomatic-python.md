---
layout: post
title:  "【转】地道的Python - Python装X入门"
category: 编程语言
tags: [python]
---

#### Data Manipulation

 - Unpacking

```python
s = ('simon', 'shi', 066, 'simonshi@gmail.com')

# bad way
firstname = s[0]
lastname = s[1]
weight = s[2]
email = s[3]

# idiomatic way
firstname, lastname, weight, email = s
_, _, _, email = s # if only email is needed
```

 - Swap Values

```python
temp = a
a = b
b = temp

# idiomatic way, using tuple packing & unpacking
a, b = b, a
a, b = (b, a)
```

 - Concatenating Strings

```python
fruits = ['cherry', 'coconut', 'blueberry', 'kiwi']

# bad
s = fruits[0]
for i in fruits[1:]:
s += ', ' + f
# idiomatic
print ', '.join(fruits)
```

 - looping

```python
colors = ['red', 'green', 'blue', 'yellow']

# Looping over a collection
# bad
for i in range(len(colors)):
print colors[i]
# idiomatic
for color in colors:
print color

# Looping backwards
for color in reversed(colors):
print color
for color in colors[::-1]:
print color

# Looping with indices
# bad
for i in range(len(colors)):
print i, '-->', colors[i]
# idiomatic
for i, color in enumerate(colors):
print i, '-->', color

# Looping over a dictionary
codes = {'Xian': '29', 'Beijing':'10', 'Shanghai':'21'}
# bad
for k in codes:
print k, '-->', codes[k]
# recommended
for k, v in codes.items():
print k, '-->', v
for k, v in codes.iteritems():
print k, '-->', v
```

 - defaultdict

```python
names = ['james', 'peter', 'simon', 'jack', 'john', 'lawrence']
# expected result
{8: ['lawrence'], 4: ['jack', 'john'], 5: ['james', 'peter', 'simon']}
# old way
groups = {}
for name in names:
key = len(name)
if key not in groups:
groups[key] = []
groups[key].append(name)
# use ‘setdefault’ with default value prepared
groups = {}
for name in names:
groups.setdefault(len(name), []).append(name)
# use ‘defaultdict’
from collections import defaultdict
groups = defaultdict(list)
for name in names:
groups[len(name)].append(name)
```


转载注明出处：PyCon2014杭州站 Shi Yuanmin@Nokia coach network
