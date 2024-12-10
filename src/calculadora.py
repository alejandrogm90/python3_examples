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

import tkinter as tk


class Calculator(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.pack(expand=tk.YES, fill=tk.BOTH)
        self.master.title('Calculadora')
        self.master.iconname("cal1")
        display = tk.StringVar()
        tk.Entry(self, relief=tk.SUNKEN, textvariable=display).pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)
        for key in ("123", "456", "789", "0."):
            key_number = Calculator.frame(self, tk.TOP)
            for char in key:
                Calculator.button(key_number, tk.LEFT, char, lambda w=display, s=' %s ' % char: w.set(w.get() + s))
        ops_frame = Calculator.frame(self, tk.TOP)
        for char in "+-*/=":
            if char == '=':
                btn = Calculator.button(ops_frame, tk.LEFT, char)
                btn.bind('<ButtonRelease-1>', lambda e, s=self, w=display: s.calc(w), '+')
            else:
                btn = Calculator.button(ops_frame, tk.LEFT, char, lambda w=display, c=char: w.set(f'{w.get()} {c} '))
        clear_frame = Calculator.frame(self, tk.BOTTOM)
        Calculator.button(clear_frame, tk.LEFT, 'Clr', lambda w=display: w.set(''))

    @staticmethod
    def frame(root, side):
        w = tk.Frame(root)
        w.pack(side=side, expand=tk.YES, fill=tk.BOTH)
        return w

    @staticmethod
    def button(root, side, text, command=None):
        w = tk.Button(root, text=text, command=command)
        w.pack(side=side, expand=tk.YES, fill=tk.BOTH)
        return w

    @staticmethod
    def calc(display):
        try:
            display.set(eval(display.get()))
        except ValueError:
            display.set("ERROR")


if __name__ == '__main__':
    Calculator().mainloop()
