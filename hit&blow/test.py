import tkinter as tk

def validate_input(P):
    if P.isdigit():
        if int(P) > 10:
            return "10"
        else:
            return P
    return ""

root = tk.Tk()
root.geometry('200x100')

vcmd = root.register(validate_input)

spinbox = tk.Spinbox(root, from_=1, to=10, validate="key", validatecommand=(vcmd, "%P"))
spinbox.pack(pady=20)

root.mainloop()
