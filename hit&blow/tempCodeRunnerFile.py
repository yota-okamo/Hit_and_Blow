import tkinter as tk

def validate_input(event=None):
    value = spinbox.get()
    try:
        int_value = int(value)
        if int_value > 10:
            spinbox.delete(0, tk.END)
            spinbox.insert(0, "10")
    except ValueError:
        spinbox.delete(0, tk.END)
        spinbox.insert(0, "1")

root = tk.Tk()
root.geometry('200x100')

spinbox = tk.Spinbox(root, from_=1, to=10)
spinbox.pack(pady=20)

spinbox.bind("<Return>", validate_input)

root.mainloop()
