import datetime
from os import path
import openpyxl


def gen_workbook_filename():
    today = datetime.date.today()
    current_date = today.strftime("%m-%d-%Y")
    return "log-%s.xlsx" % current_date


def does_workbook_exist(current_date):
    workbook_filename = gen_workbook_filename()
    status = path.exists(workbook_filename)
    print("\t%s exists: %r" % (workbook_filename, status))
    return status


def save_workbook(wb, filename):
    wb.save("logs/"+filename)


def init_workbook(filename):
    wb = ""
    try:
        wb = openpyxl.load_workbook("logs/"+filename)
        print("! Found workbook \"%s\"" % filename)
    except FileNotFoundError:
        print("? No workbook \"%s\", creating..." % filename)
        wb = openpyxl.Workbook()
        save_workbook(wb, filename)

    print("! Successfully Initialized \"%s\"" % filename)
    return wb


def init_workbook_from_date():
    name = gen_workbook_filename()
    workbook = init_workbook(name)
    return workbook


def add_engineer(wb, engineer_name):
    time = datetime.datetime.now().strftime("%H:%M:%S")
    filename = gen_workbook_filename()
    ws = wb.active
    ws.append([time, engineer_name])
    save_workbook(wb, filename)
    print("\tIn %s, appended %s @ %s" % (filename, engineer_name, time))


# add_engineer(workbook, name, "John")
# add_engineer(workbook, name, "Paul")
# add_engineer(workbook, name, "George")
# add_engineer(workbook, name, "Ringo")
# print("All done.")