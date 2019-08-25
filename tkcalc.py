from tkinter import Tk, Button, Entry, END
import math


class calc:
    def getandreplace(self):
        # reemplaza x con * y ÷ con /
        self.expression = self.e.get()
        self.newtext = self.expression.replace('÷', '/')
        self.newtext = self.newtext.replace('x', '*')

    def equals(self):
        # Cuando presionas el boton =
        self.getandreplace()
        try:
            # evalua la expresion usando la funcion eval
            self.value = eval(self.newtext)
        except SyntaxError:
            self.e.delete(0, END)
            self.e.insert(0, 'Entrada inválida')
        else:
            self.e.delete(0, END)
            self.e.insert(0, self.value)

    def squareroot(self):
        # Raíz cuadrada
        self.getandreplace()
        try:
            # evalua la expresion usando la funcion eval
            self.value = eval(self.newtext)
        except SyntaxError:
            self.e.delete(0, END)
            self.e.insert(0, 'Entrada inválida')
        else:
            self.sqrtval = math.sqrt(self.value)
            self.e.delete(0, END)
            self.e.insert(0, self.sqrtval)

    def square(self):
        # Elevar al cuadrado
        self.getandreplace()
        try:
            # evalua la expresion usando la funcion eval
            self.value = eval(self.newtext)
        except SyntaxError:
            self.e.delete(0, END)
            self.e.insert(0, 'Entrada inválida')
        else:
            self.sqval = math.pow(self.value, 2)
            self.e.delete(0, END)
            self.e.insert(0, self.sqval)

    def clearall(self):
        # Limpia el cuadro de texto
        self.e.delete(0, END)

    def clear1(self):
        # elimina lo ultimo ingresado al cuadro de texto
        self.txt = self.e.get()[:-1]
        self.e.delete(0, END)
        self.e.insert(0, self.txt)

    def action(self, argi):
        # El valor del boton presionado es añadido al final del cuadro de texto
        self.e.insert(END, argi)

    def __init__(self, master):
        # Método constructor
        master.title('Caluladora')
        master.geometry()
        self.e = Entry(master)
        self.e.grid(row=0, column=0, columnspan=6, pady=3)
        self.e.focus_set()  # Pone el focus en el cuadro de texto

        # Botones
        Button(master, text="=", width=10, command=lambda: self.equals()).grid(
            row=4, column=4, columnspan=2)
        Button(master, text='AC', width=3, command=lambda: self.clearall(
            )).grid(row=1, column=4)
        Button(master, text='C', width=3, command=lambda: self.clear1()).grid(
            row=1, column=5)
        Button(master, text="+", width=3, command=lambda: self.action(
            '+')).grid(row=4, column=3)
        Button(master, text="x", width=3, command=lambda: self.action(
            'x')).grid(row=2, column=3)
        Button(master, text="-", width=3, command=lambda: self.action(
            '-')).grid(row=3, column=3)
        Button(master, text="÷", width=3, command=lambda: self.action(
            '÷')).grid(row=1, column=3)
        Button(master, text="%", width=3, command=lambda: self.action(
            '%')).grid(row=4, column=2)
        Button(master, text="7", width=3, command=lambda: self.action(
            7)).grid(row=1, column=0)
        Button(master, text="8", width=3, command=lambda: self.action(
            8)).grid(row=1, column=1)
        Button(master, text="9", width=3, command=lambda: self.action(
            9)).grid(row=1, column=2)
        Button(master, text="4", width=3, command=lambda: self.action(
            4)).grid(row=2, column=0)
        Button(master, text="5", width=3, command=lambda: self.action(
            5)).grid(row=2, column=1)
        Button(master, text="6", width=3, command=lambda: self.action(
            6)).grid(row=2, column=2)
        Button(master, text="1", width=3, command=lambda: self.action(
            1)).grid(row=3, column=0)
        Button(master, text="2", width=3, command=lambda: self.action(
            2)).grid(row=3, column=1)
        Button(master, text="3", width=3, command=lambda: self.action(
            3)).grid(row=3, column=2)
        Button(master, text="0", width=3, command=lambda: self.action(
            0)).grid(row=4, column=0)
        Button(master, text=".", width=3, command=lambda: self.action(
            '.')).grid(row=4, column=1)
        Button(master, text="(", width=3, command=lambda: self.action(
            '(')).grid(row=2, column=4)
        Button(master, text=")", width=3, command=lambda: self.action(
            ')')).grid(row=2, column=5)
        Button(master, text="√", width=3, command=lambda: self.squareroot(
            )).grid(row=3, column=4)
        Button(master, text="x²", width=3, command=lambda: self.square(
            )).grid(row=3, column=5)


# Main
root = Tk()
obj = calc(root)  # objeto instanciado
root.mainloop()
