'''
Cursor grab script
Written by: Matt Sybeldon

This script is used as part of configuration so the user doesn't have to fiddle with numbers to get their 3DS screen.
Pretty simple.
'''

from ctypes import windll, Structure, c_ulong, byref

class point(Structure):
    _fields_ = [("x", c_ulong), ("y", c_ulong)]

def return_position():
    pt = point()
    windll.user32.GetCursorPos(byref(pt))
    return{"x": pt.x, "y": pt.y}