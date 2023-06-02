import tkinter as tk
import os
import pandas as pd
from typing import List
TABLE = os.path.join(os.path.dirname(__file__), 'periodic_table.csv')
# file = open(TABLE, 'r')
# for line in file.readlines():
#     print(line)

class Table:
    def __init__(self, root):
        tk.Frame(root)
        self.dataframe = pd.read_csv(TABLE)
        self.dataframe = self.dataframe.convert_dtypes(convert_integer = True)
        self.name = tk.Label(master = root, text = 'Periodic Table of Elements', font = ('Arial', 50, 'bold underline'))
        self.name.pack()
        self.element_buttons: List[tk.Button] = []
        self.maingrid = tk.Frame(root)
        self.seriesgrid = tk.Frame(root)
        self.keygrid = tk.Frame(root)
        self.colours = {'Alkali Metal': '#560D42', 
                        'Alkaline Earth Metal': '#820263',
                        'Metal': 'blue',
                        'Transition Metal': '#D90368',
                        'Transactinide': '#291720',
                        'Metalloid': '#203B36',
                        'Nonmetal': '#E83036',
                        'Noble Gas': '#F75C03',
                        'Halogen': 'red',
                        'Lanthanide': '#04A777',
                        'Actinide': '#175F4C'
                        }
        for i, element in self.dataframe.iterrows():
            if element.AtomicNumber >= 57 and element.AtomicNumber <= 71:
                self.element_buttons.append(tk.Button(master = self.seriesgrid, text = element.Symbol, height = 3, width = 6, bg = self.colours[element.Type], fg = 'white', highlightthickness = 5, command = lambda index=i: self.element_press(index)))
                self.element_buttons[-1].grid(row = 0, column = element.AtomicNumber - 57)
            elif element.AtomicNumber >= 89 and element.AtomicNumber <= 103:
                self.element_buttons.append(tk.Button(master = self.seriesgrid, text = element.Symbol, height = 3, width = 6, bg = self.colours[element.Type], fg = 'white', highlightthickness = 5, command = lambda index=i: self.element_press(index)))
                self.element_buttons[-1].grid(row = 1, column = element.AtomicNumber - 89)
            else:
                self.element_buttons.append(tk.Button(master = self.maingrid, text = element.Symbol, height = 3, width = 6, bg = self.colours[element.Type], fg = 'white', highlightthickness = 5, command = lambda index=i: self.element_press(index)))
                self.element_buttons[-1].grid(row = int(element.Period) - 1, column = int(element.Group) - 1)
        column = 0
        for key, value in self.colours.items():
            tk.Label(master = self.keygrid, height = 1, width = 2, bg = value, ).grid(row = 0, column = column)
            tk.Label(master = self.keygrid, text = '- ' + key).grid(row = 0, column = column + 1, padx = (0, 20))
            column += 2
        self.maingrid.pack()
        self.seriesgrid.pack(pady = (20, 30))
        self.keygrid.pack()

    def element_press(self, index):
        for i, element in self.dataframe.iterrows():
            self.element_buttons[i].config(bg = self.colours[element.Type])
        self.element_buttons[index].config(bg = 'yellow', highlightcolor = 'yellow')
if __name__ == '__main__':
    window = tk.Tk()
    table = Table(window)
    window.mainloop()