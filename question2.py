# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 17:31:38 2015

@author: philippos
"""

from xlrd import open_workbook

# open the workbook for reading
wb = open_workbook('SME Template-ECB Version 20 Taxonomy.xls')

# link to the desired sheet
assets_sheet = wb.sheets()[1]

# read certain rows
print('<table>')
for row in range(4, assets_sheet.nrows):
    number = assets_sheet.cell(row, 1).value
    name = assets_sheet.cell(row, 4).value
    definition = assets_sheet.cell(row, 6).value
    notes = assets_sheet.cell(row, 9).value
    print(
        '<tr>' + '\n'
                 '<td>' + str(number) + ' </td>' + '\n' +
        '<td>' + str(name) + ' </td>' + '\n' +
        # '<td>' + str(definition) + ' </td>' +
        '<td>' + str(notes) + ' </td>' + '\n' + '</tr>' + '\n')

print('</table>')
