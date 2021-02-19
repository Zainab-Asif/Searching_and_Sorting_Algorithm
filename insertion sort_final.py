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

#insertion sort algorithm

start=time.time()
size = len(data)

for i in range (size):
     for j in range (size - 1):
          if data[j] > data[j+1]:
               temp = data[j+1]
               data[j+1] = data[j]
               data[j] = temp
               while data[j] < data[j-1]:
                    temp = data[j-1]
                    data[j-1] = data[j]
                    data[j] = temp
                    j-=1
                    if j == 0:
                         break

elapsedTime=(time.time()-start)
print ("elapsed time(sec):",elapsedTime)

#for k in range (size):
     #print(data[k])


     
          
