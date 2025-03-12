# # >> > print("Hello wrold")
# # Hello wrold
# # >> > cls
# # Traceback(most recent call last):
# #   File "<stdin>", line 1, in <module >
# # NameError: name 'cls' is not defined
# # >> > 2+2
# # 4
# # >> > 22332323*89
# # 1987576747
# # >> > "chai" * 4
# # 'chaichaichaichai'
# # >> > score = 101
# # >> > print("score")
# # score
# # >> > tea
# # Traceback(most recent call last):
# #   File "<stdin>", line 1, in <module >
# # NameError: name 'tea' is not defined
# >> > import os
# >> > os.getcwd()
# '/workspaces/Python-Basics/01_basics'
# >> > tea = "chai"
# >> > for c in tea:
# ... print(c)
# File "<stdin>", line 2
# print(c)
# ^
# IndentationError: expected an indented block after 'for' statement on line 1
# >> > for c in "chai":
# ... print(c)
# ...
# c
# h
# a
# i
# >> > import sys
# >> > sys.platform
# 'linux'
# >> > ls
# Traceback(most recent call last):
#   File "<stdin>", line 1, in <module >
# NameError: name 'ls' is not defined. Did you mean: 'os'?
# >> > import hello_chai
# chai aur python
# lemon tea
# >> > hello_chai.chai("mint chai")
# mint chai
# >> > hello_chai.chai_one
# Traceback(most recent call last):
#   File "<stdin>", line 1, in <module >
# AttributeError: module 'hello_chai' has no attribute 'chai_one'
# >> > from importlib import reload
# >> > reload(hello_chai)
# chai aur python
# lemon tea
# <module 'hello_chai' from '/workspaces/Python-Basics/01_basics/hello_chai.py' >
# >> > hello_chai.chai_one
# 'masala tea'
