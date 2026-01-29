import csv
from openpyxl import Workbook

def excel_method(keyword,data):
    wb = Workbook()
    ws = wb.active
    wb.remove(ws)
    for i,j in data.items():
        new_ws = wb.create_sheet(f'page {i}')
        new_ws.append(['Title','Link'])
        for a in j:
            new_ws.append([a['title'],a['link']])
    wb.save(f'excel_saving/{keyword}_news.xlsx')
    print('EXCEL FORMAT Saving Successful')

def csv_method(keyword,data):
    for i,j in data.items():
        file_name = f'csv_saving/{i} page {keyword}_news.csv'
        with open(file_name,'w',encoding='utf-8',newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(['Title','Link'])
            for a in j:
                csv_writer.writerow([a['title'],a['link']])
        print(f'{file_name} Saving Successful')
