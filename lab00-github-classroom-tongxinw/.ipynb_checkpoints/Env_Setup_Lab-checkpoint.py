# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.2.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Lab 0: GitHub Classroom
# In this lab you'll set up the tools that you will need for this course on your computer so that you can work on projects and labs efficiently throughout the semester. If you run into any trouble, pleasse do not hesitate to reach out to the TAs!

# %% [markdown]
# ### Binary Search for Root finding
# You can use the principle of binary search in conjunction with the intermediate value theorem of Calculus to find the roots of any continuous function.  Below is some code that a student wrote to perform this task.  
#
# Can you find the issues?

# %%
import math


def find_root(f, L, H, tol):
    """
    Returns a root of f in the interval (L, H) up to tolerance tol.
    """
    x = (L + H) / 2
    while abs(L - H) > tol:
        x = (L + H) / 2
        if f(L) * f(H) < 0:
            H = x
        else:
            L = x
    return x


find_root(lambda x: math.sin(x) + .5, -5, 5, 1e-10)

# %%
# This is not the right answer :(
math.sin(-1.2500000000727596) + .5

# %% [markdown]
# ### Task 1: Describe the problems
#
# Your answer here

# %% [markdown]
# ### Task 2: Provide a corrected version of the code

# %%
# Your code here

# %% [markdown]
# ## Congradulations and welcome to Data1050!
# Be sure to `git add/commit/push` when you are done.
