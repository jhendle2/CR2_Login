import tkinter as tk
from tkinter import ttk
import spreadsheet_maker as sm


def main():
    window = tk.Tk()
    window.title("CR2 Sign In")
    window.minsize(200, 100)

    print("!! Started CR2-Engineer Logger")

    def button_is_pressed():
        engineer = name.get().capitalize()
        print("\tLogged Engineer: ", engineer)
        workbook = sm.init_workbook_from_date()
        sm.add_engineer(workbook, engineer)

    blank = ttk.Label(window, text="\t")
    blank.grid(column=0, row=0)

    label = ttk.Label(window, text="Enter Your Name")
    label.grid(column=1, row=1)

    name = tk.StringVar()
    name_entered = ttk.Entry(window, width=15, textvariable=name)
    name_entered.grid(column=1, row=2)

    button = ttk.Button(window, text="Sign In", command=button_is_pressed)
    button.grid(column=1, row=3)

    window.mainloop()
    main()
    print("Stop trying to close me")


main()
print("All done.")
