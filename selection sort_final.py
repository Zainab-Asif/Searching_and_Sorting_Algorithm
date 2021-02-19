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

#selection sort algorithm
start=time.time()

size = len(data)

for i in range (size-1):
     min_position = i
     for j in range (i,size):
          if data[j] < data[min_position]:
               min_position = j

     temp = data[i]
     data[i] = data[min_position]
     data[min_position] = temp

elapsedTime=(time.time()-start)
print ("elapsed time(sec):",elapsedTime)

#for k in range(size):
    # print(data[k])
