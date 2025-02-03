# @gudakesh07 ➜ /workspaces/Python-Basics/01_basics (main) $ python
# Python 3.12.1 (main, Dec 12 2024, 22:30:56) [GCC 9.4.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> print("chai ")
# chai 
# >>> 2+2
# 4
# >>> "chai" * 4 
# 'chaichaichaichai'
# >>> import os
# >>> os.getcwd
# <built-in function getcwd>
# >>> os.getcwd()
# '/workspaces/Python-Basics/01_basics'
# >>> for c in "chai"P:
#   File "<stdin>", line 1
#     for c in "chai"P:
#                    ^
# SyntaxError: invalid syntax
# >>> for c in "chai":
# ...     print(c)
# ... 
# c
# h
# a
# i
# >>> import cs
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ModuleNotFoundError: No module named 'cs'
# >>> import sys
# >>> sys.platform
# 'linux'
# >>> import test
# Hello World
# lemon tea
# >>> test.chai("mint chai")
# mint chai
# >>> test.chai.chai_one
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'function' object has no attribute 'chai_one'
# >>> import test
# >>> test.chai.chai_one
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'function' object has no attribute 'chai_one'
# >>> from importlib import reload
# >>> reload(test)
# Hello World
# lemon tea
# <module 'test' from '/workspaces/Python-Basics/01_basics/test.py'>
# >>> cls
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'cls' is not defined
# >>> test.chai_one
# 'lemon tea'
# >>> test.chai_three
# 'masala chai