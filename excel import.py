import xlrd
loc = ('C:\\Users\\ZAINAB\\Desktop\\DS project\\Book1.xlsx')
wb = xlrd.open_workbook (loc)
sheet = wb.sheet_by_index(0)

data=[]
i = 0
for i in range (sheet.nrows):
     data.append(sheet.cell_value(i,0))
     i+=1

print(data)
     
          
