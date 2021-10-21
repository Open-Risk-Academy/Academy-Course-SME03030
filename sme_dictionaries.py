from xlrd import open_workbook
import pprint
import re

# open the workbook for reading
wb = open_workbook('SME Template-ECB Version 20 Taxonomy.xls')

# link to the currency table sheet
currency_sheet = wb.sheets()[3]

# initialize a dictionary
currency_table = {}

# read the data from the spreadsheet and add to the dictionary
for row in range(5,currency_sheet.nrows):
    code = currency_sheet.cell(row,1).value
    currency = currency_sheet.cell(row,2).value
    currency_table[code] = currency


# link to the sector table sheet
sector_sheet = wb.sheets()[4]

# initialize a dictionary
sector_table = {}

# read the data from the spreadsheet and add to the dictionary
for row in range(5,sector_sheet.nrows):
    code = sector_sheet.cell(row,1).value
    sector = sector_sheet.cell(row,2).value
    sector_table[code] = sector

# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(sector_table)


# link to the taxonomy table sheet
data_sheet = wb.sheets()[1]

# initialize a dictionary
data_table = {}

# read the data from the spreadsheet and add to the dictionary
for row in range(5,data_sheet.nrows):
    field_id = data_sheet.cell(row,1).value
    field_name = data_sheet.cell(row,4).value
    # print(field_id, field_id[:2])
    for element in ["AS","BS","CS"]:
        if element == field_id[:2]:
            # print(m, element, field_id[:2])
            # print(element, field_id, field_name)
            data_table[field_id] = field_name
    
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data_table)    