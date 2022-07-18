# __init__.py - arrange call of functions dispite packeges structure



from utility.useful.functions import nice_function
from utility.dummy.functions import not_bad

__all__ = ['nice_function', 'not_bad'] # List modules and packeges which import if 'import *'


#   Package sructure example:
    #   utility
    #         | - useful  -   functions.py -   nice_function
    #         | - dummy   -   functions.py -   not_bad
#
#
# Could be called like:
""" 
from utility import nice_function, not_bad

nice_function()
not_bad() 

or 

from utility import *

nice_function()
not_bad() 
"""
