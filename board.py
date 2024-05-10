from tkinter import Tk, Frame

window = Tk()
window.geometry('600x600+300+30')
window.title('Othello Game')

for i in range(8):
    for j in range(8):
        fr = Frame(window, width='75', height='75', bg='green', highlightbackground='black', highlightthickness=2)
        fr.grid(row=i, column=j)

window.mainloop()
