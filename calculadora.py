#!/usr/bin/env python3
#
#
#       Copyright 2022 Alejandro Gomez
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.

from tkinter import *

def frame(root, side):
    w = Frame(root)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w

def button(root, side, text, command=None):
    w = Button(root, text=text, command=command)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w

class Calculator(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Calculadora')
        self.master.iconname("cal1")
        display = StringVar()
        Entry(self, relief=SUNKEN, textvariable=display).pack(side=TOP, expand=YES, fill=BOTH)
        for key in ("123", "456", "789", "0."):
            keyF = frame(self, TOP)
            for char in key:
                button(keyF, LEFT, char, lambda w=display, s=' %s '%char: w.set(w.get()+s))
        opsF = frame(self, TOP)
        for char in "+-*/=":
            if char == '=':
                btn = button(opsF, LEFT, char)
                btn.bind('<ButtonRelease-1>',lambda e, s=self, w=display: s.calc(w), '+')
            else:
                btn = button(opsF, LEFT, char,
                lambda w=display, c=char: w.set(w.get()+' '+c+' '))
        clearF = frame(self, BOTTOM)
        button(clearF, LEFT, 'Clr', lambda w=display: w.set(''))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except ValueError:
            display.set("ERROR")

if __name__ == '__main__':
    Calculator().mainloop()
