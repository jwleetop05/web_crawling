import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
ws.append(['a','b','c','d'])

wb.save("test.xlsx")