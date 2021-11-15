# Bash-like brace expansion for Python #

![Tests](https://github.com/howamith/brace-expand/actions/workflows/tests.yml/badge.svg)

A Python implementation of
[Bash's Brace Expansion](https://man7.org/linux/man-pages/man1/bash.1.html#EXPANSION).

## Examples ##

The `brace_expand` function returns a list of strings generated from an
expression.

```python
>>> from brace_expand import brace_expand

# Comma separation.
>>> brace_expand("1,2,3,4")
["1", "2", "3", "4"]

# Integer range.
>>> brace_expand("1..4")
["1", "2", "3", "4"]

# Sequence.
>>> brace_expand("python{2.7,3.8}")
["python2.7", "python 3.8"]

# Nested Sequence.
>>> brace_expand("python{2.{5..7},3.{6,8,9}}")
["python2.5", "python2.6", "python2.7", "python3.6", "python3.8", "python3.9"]
```
