import tkinter as tk                               #asdfghjk,mrhfwkgvkwhbfjbflfjnwlefjqlijebflijblijwbleiefjilwjfiwjf
import os
import pandas as pd
from typing import List
TABLE = os.path.join(os.path.dirname(__file__), 'periodic_table.csv')

class Table:
    def __init__(self, root):
        tk.Frame(root)
        self.dataframe = pd.read_csv(TABLE)
        self.dataframe = self.dataframe.convert_dtypes(convert_integer = True)
        self.homegrid = tk.Frame(root)
        self.name = tk.Label(master = self.homegrid, text = 'Periodic Table of Elements', font = ('Arial', 50, 'bold underline'))
        self.name.pack()
        self.element_buttons: List[tk.Button] = []
        self.maingrid = tk.Frame(self.homegrid)
        self.seriesgrid = tk.Frame(self.homegrid)
        self.keygrid = tk.Frame(root)
        self.infogrid = tk.Frame(root)
        self.searchvar = tk.StringVar()
        self.searchbar = tk.Entry(master = self.homegrid, textvariable = self.searchvar).pack(pady = (5, 10))
        self.searchvar.trace_add(mode = 'write', callback = self.search)
                                                                                        #colours
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
        column8offset = 0
        for i, element in self.dataframe.iterrows():
            print(f'{element.AtomicNumber}, {element.Subperiod_UA}')
        for i, element in self.dataframe.iterrows():
            if element.Group_UA == 8:
                displaycolumn = 8 + column8offset
                column8offset += 1
            else:
                displaycolumn = element.Group_UA
                column8offset = 0
            if element.AtomicNumber >= 58 and element.AtomicNumber <= 71:
                self.element_buttons.append(tk.Button(master = self.seriesgrid, text = element.Symbol, height = 2, width = 6, bg = self.colours[element.Type], fg = 'white', highlightthickness = 5, command = lambda index=i: self.element_press(index)))
                self.element_buttons[-1].grid(row = 0, column = element.AtomicNumber - 57)
            elif element.AtomicNumber >= 90 and element.AtomicNumber <= 103:
                self.element_buttons.append(tk.Button(master = self.seriesgrid, text = element.Symbol, height = 2, width = 6, bg = self.colours[element.Type], fg = 'white', highlightthickness = 5, command = lambda index=i: self.element_press(index)))
                self.element_buttons[-1].grid(row = 1, column = element.AtomicNumber - 89)
            else:
                self.element_buttons.append(tk.Button(master = self.maingrid, text = element.Symbol, height = 2, width = 6, bg = self.colours[element.Type], fg = 'white', highlightthickness = 5, command = lambda index=i: self.element_press(index)))
                self.element_buttons[-1].grid(row = int(element.Subperiod_UA) + 1, column = int(displaycolumn) + 2)
        row = 0
        for key, value in self.colours.items():
            tk.Label(master = self.keygrid, height = 1, width = 2, bg = value, ).grid(row = row, column = 0, pady = (0, 20))
            tk.Label(master = self.keygrid, text = '- ' + key).grid(row = row, column = 1, pady = (0, 20))
            row += 1
        tk.Label(master = self.maingrid, width = 85, text = 'ГРУПИ ЕЛЕМЕНТІВ', borderwidth = 1, relief = 'solid').grid(row = 0, column = 2, columnspan = 11)
        tk.Label(master = self.maingrid, width = 56, height = 35, text = 'ПЕРІОД', image = tk.PhotoImage(), compound = tk.CENTER, borderwidth = 1, relief = 'solid').grid(row = 0, column = 0, rowspan = 2)
        tk.Label(master = self.maingrid, width = 21, height = 35, text = 'РЯД', image = tk.PhotoImage(), compound = tk.CENTER, borderwidth = 1, relief = 'solid').grid(row = 0, column = 1, rowspan = 2)
        tk.Label(master = self.maingrid, height = 1, width = 8, text = 'I', borderwidth = 1, relief = 'solid').grid(row = 1, column = 3)
        tk.Label(master = self.maingrid, height = 1, width = 8, text = 'II', borderwidth = 1, relief = 'solid').grid(row = 1, column = 4)
        tk.Label(master = self.maingrid, height = 1, width = 8, text = 'III', borderwidth = 1, relief = 'solid').grid(row = 1, column = 5)
        tk.Label(master = self.maingrid, height = 1, width = 8, text = 'IV', borderwidth = 1, relief = 'solid').grid(row = 1, column = 6)
        tk.Label(master = self.maingrid, height = 1, width = 8, text = 'V', borderwidth = 1, relief = 'solid').grid(row = 1, column = 7)
        tk.Label(master = self.maingrid, height = 1, width = 8, text = 'VI', borderwidth = 1, relief = 'solid').grid(row = 1, column = 8)
        tk.Label(master = self.maingrid, height = 1, width = 8, text = 'VII', borderwidth = 1, relief = 'solid').grid(row = 1, column = 9)
        tk.Label(master = self.maingrid, height = 1, width = 25, text = 'VIII', borderwidth = 1, relief = 'solid').grid(row = 1, column = 10, columnspan = 3)

        tk.Label(master = self.maingrid, width = 8, height = 3, text = '1', borderwidth = 1, relief = 'solid').grid(row = 2, column = 0)
        tk.Label(master = self.maingrid, width = 8, height = 3, text = '2', borderwidth = 1, relief = 'solid').grid(row = 3, column = 0)
        tk.Label(master = self.maingrid, width = 8, height = 3, text = '3', borderwidth = 1, relief = 'solid').grid(row = 4, column = 0)
        tk.Label(master = self.maingrid, width = 56, height = 94, text = '4', image = tk.PhotoImage(), compound = tk.CENTER, borderwidth = 1, relief = 'solid').grid(row = 5, column = 0, rowspan = 2)
        tk.Label(master = self.maingrid, width = 56, height = 94, text = '5', image = tk.PhotoImage(), compound = tk.CENTER, borderwidth = 1, relief = 'solid').grid(row = 7, column = 0, rowspan = 2)
        tk.Label(master = self.maingrid, width = 56, height = 94, text = '6', image = tk.PhotoImage(), compound = tk.CENTER, borderwidth = 1, relief = 'solid').grid(row = 9, column = 0, rowspan = 2)
        tk.Label(master = self.maingrid, width = 56, height = 94, text = '7', image = tk.PhotoImage(), compound = tk.CENTER, borderwidth = 1, relief = 'solid').grid(row = 11, column = 0, rowspan = 2)

        for i in range(1, 12):
            tk.Label(master = self.maingrid, width = 3, height = 3, text = f'{i}', borderwidth = 1, relief = 'solid').grid(row = i + 1, column = 1)

        self.maingrid.pack()
        self.seriesgrid.pack(pady = (20, 30))
        self.keygrid.pack(side = tk.LEFT)
        self.homegrid.pack(side = tk.LEFT)
        self.infogrid.pack(side = tk.RIGHT)

    def remove_highlight(self):
        for i, element in self.dataframe.iterrows():
            self.element_buttons[i].config(bg = self.colours[element.Type])

    def element_press(self, index):
        self.remove_highlight()
        self.element_buttons[index].config(bg = 'yellow', highlightcolor = 'yellow')
        row = 0
        for key, value in self.dataframe.loc[index, :].items():
            tk.Label(master = self.infogrid, text = key).grid(column = 0, row = row)
            tb = tk.Text(master = self.infogrid, height = 1, width = 30)
            tb.insert(1.0, value)
            tb.config(state = 'disabled')
            tb.grid(column = 1, row = row)
            row += 1    

    def search(self, *args):
        searchelement = self.searchvar.get()
        if not searchelement:
            self.remove_highlight()
            return
        if searchelement.isdecimal():
            df2 = self.dataframe[self.dataframe.AtomicNumber == int(searchelement)]
        else:
            df2 = self.dataframe[self.dataframe.Element.str.contains('^' + searchelement, case = False, regex = True) |
                                 self.dataframe.Symbol.str.contains('^' + searchelement, case = False, regex = True)]
        elementfound = df2.index.to_list()
        if len(elementfound) != 1:
            for vidgets in self.infogrid.winfo_children():
                vidgets.destroy()
            self.remove_highlight()
            for index in elementfound:
                self.element_buttons[index].config(bg = 'yellow', highlightcolor = 'yellow')
        else:
            self.element_press(elementfound[0])



if __name__ == '__main__':
    window = tk.Tk()
    table = Table(window)
    window.mainloop()