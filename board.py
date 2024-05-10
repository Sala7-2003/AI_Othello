from tkinter import Tk, Frame, Label

window = Tk()
window.geometry('800x700')
window.maxsize(900,900)# Adjust the window size as needed
window.title('Othello Game')

# Create the "You" and "Computer" labels
you_label = Label(window, text='You', font=('Arial', 14))
you_label.grid(row=0, column=0, padx=30, pady=20)

computer_label = Label(window, text='Computer', font=('Arial', 14))
computer_label.grid(row=1, column=0, padx=20, pady=20)

# Create the 8x8 board
for i in range(8):
    for j in range(8):
        fr = Frame(window, width='60', height='60', bg='green', highlightbackground='black', highlightthickness=2)
        fr.grid(row=i+2, column=4+j, padx=0, pady=0)

window.mainloop()
