from tkinter import *

root = Tk()
root.title("Scrollable Window")
root.geometry("400x400")

canvas = Canvas(root)
canvas.pack(side=LEFT, fill=BOTH, expand=True)
canvas.rowconfigure(0, weight=1)
canvas.columnconfigure(0, weight=1)

scrollbar = Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=scrollbar.set)


canvas.config(bg="red")

frame = Frame(canvas)
frame.config(bg="blue")
frame.pack(fill=BOTH, expand=True)
canvas.create_window((0, 0), window=frame, anchor="nw", tags="frame")

for i in range(100):
    label = Label(canvas, text = "hey").grid(row = i, column = 0)

frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()