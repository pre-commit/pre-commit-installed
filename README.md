pre-commit-installed
====================

runs `pre-commit install` on installation (terrible hack)


### what even?

One of the strong design decisions of pre-commit is that each action is
opted into.  There's a common query / complaint that "hey pre-commit should
just install when I install it!".  This monstrosity implements that.

You should probably not use this, it's mostly a proof of concept.  pip tries
pretty hard to make this difficult (as it should!).  Running arbitrary code
in `setup.py` is not a good idea.
