import openpyxl

path = "C:/Users/Usuario/PycharmProjects/Selenium_with_Python/blank.xlsx"

workbook = openpyxl.load_workbook(path)
sheet = workbook.active

for r in range(1, 5):  # will write 4 only
    for c in range(1, 4):
        sheet.cell(row=r, column=c).value = "welcome"

workbook.save(path)
