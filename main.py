from openpyxl import Workbook

# 保存したい配列
data = [
    [1, 2, 3],
    ["a", "b", "c"],
    [4.5, 6.7, 8.9]
]

wb = Workbook()
ws = wb.active

for row in data:
    ws.append(row)

wb.save("output.xlsx")
