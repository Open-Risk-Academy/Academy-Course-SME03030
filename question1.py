from xlrd import open_workbook

# open the workbook for reading
wb = open_workbook('SME Template-ECB Version 20.xls')

# link to the desired sheet
assets_sheet = wb.sheets()[2]

# read certain rows
for row in range(4, assets_sheet.nrows):
    number = assets_sheet.cell(row, 1).value
    priority = assets_sheet.cell(row, 2).value
    name = assets_sheet.cell(row, 4).value
    # print(str(number), str(priority), str(name))

mystery_value = wb.sheets()[4].cell(5, 1).value
print(mystery_value)
