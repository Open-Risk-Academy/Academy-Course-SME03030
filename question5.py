# (c) 2021 - 2023 Open Risk (https://www.openriskmanagement.com)

import random

import xlwt


def create_obligors():
    obligors = []
    for i in range(10):
        country_list = [1, 2, 3, 4, 5]
        sector_list = [1, 2, 3, 4, 5]
        obligors.append(
            {
                'obligor_id': str(i),
                'country': random.choice(country_list),
                'sector': random.choice(sector_list),
                'rating': random.random(),
                'financials': {
                    'Turnover of Obligor': random.random(),
                    'Equity': random.random(),
                    'Total Liabilities': random.random(),
                    'Short Term Debt': random.random(),
                    'Commercial Liabilities': random.random(),
                    'Long Term Debt': random.random(),
                    'Financial Expenses': random.random(),
                    'EBITDA': random.random(),
                    'EBIT': random.random(),
                    'Net Profit': random.random(),
                    'Employees': random.random(),
                    'Currency': 'EUR',
                    'Date': '2007-12-5',
                }
            }
        )
    return obligors


def save_obligors(obligors, sheetname, workbook):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Obligor Data')

    ws.write(0, 0, 'Obligor ID')
    ws.write(1, 0, 'Obligor PD')
    for i in range(size(obligors)):
        ws.write(0, i + 1, obligors[i]['obligor_id'])
        ws.write(1, i + 1, obligors[i]['rating'])

    wb.save('SME_Data.xls')


if __name__ == '__main__':
    sheetname = 'Obligor Data'
    workbook = 'SME_Data.xls'

    obligors = create_obligors()
    save_obligors(obligors, sheetname, workbook)
