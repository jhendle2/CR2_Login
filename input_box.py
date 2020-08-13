import tkinter as tk
from tkinter import ttk
import spreadsheet_maker as sm
import email_manager as em
import datetime

print("!! Started CR2-Engineer Logger")

def main():
    window = tk.Tk()
    window.title("CR2 Sign In")
    window.minsize(500, 250)

    def login_is_pressed():
        engineer = name.get().capitalize()
        print("\tLogged Engineer: ", engineer)
        workbook = sm.init_workbook_from_date()
        sm.add_engineer(workbook, engineer)
        em.send_login_email(engineer, datetime.datetime.now().strftime("%H:%M:%S"))

    def problem_is_pressed():
        error = problem.get()
        print("\tProblem Reported: ", error)
        em.send_error_email(error, datetime.datetime.now().strftime("%H:%M:%S"))

    blank = ttk.Label(window, text="\nCR2 Login and Problem Reporting Tool\n    Please do not close this window!\n")
    blank.grid(column=1, row=0)

    label = ttk.Label(window, text="Enter Your Name")
    label.grid(column=1, row=1)

    name = tk.StringVar()
    name_entered = ttk.Entry(window, width=15, textvariable=name)
    name_entered.grid(column=1, row=2)

    blank2 = ttk.Label(window, text="\t")
    blank2.grid(column=0, row=4)

    label = ttk.Label(window, text="Report a CR2 Problem")
    label.grid(column=1, row=5)

    problem = tk.StringVar()
    problem_entered = ttk.Entry(window, width=45, textvariable=problem)
    problem_entered.grid(column=1, row=6)

    login_button = ttk.Button(window, text="Sign In", command=login_is_pressed)
    login_button.grid(column=1, row=3)

    problem_button = ttk.Button(window, text="Report Problem", command=problem_is_pressed)
    problem_button.grid(column=1, row=7)

    window.mainloop()
    print("!! User tried to close CR2_Login !!")
    main()
    print("Stop trying to close me :(")


main()
print("All done.")
