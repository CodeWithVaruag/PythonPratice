import sys
import ctypes


var1=1011121314151617181
print(id(var1))
var2= id(var1)
print(ctypes.cast(var2,ctypes.py_object).value)



