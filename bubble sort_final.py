#data import

import xlrd
import time
loc = ('C:\\Users\\ZAINAB\\Desktop\\DS project\\Book1.xlsx')
wb = xlrd.open_workbook (loc)
sheet = wb.sheet_by_index(0)

data=[]
i = 0
for i in range (sheet.nrows):
     data.append(sheet.cell_value(i,0))
     i+=1

#bubble sort algorithm

start=time.time()
size = len(data)
for x in range (size):
     for y in range (size - 1):
          if data[y] > data[y+1]:
               temp = data[y]
               data[y] = data[y+1]
               data[y+1] = temp

elapsedTime=(time.time()-start)
print ("elapsed time(sec):",elapsedTime)


#for z in range (size):
 #    print(data[z])
