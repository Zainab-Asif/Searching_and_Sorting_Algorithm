#data import

import xlrd
import timeit
import time

loc = ('C:\\Users\\ZAINAB\\Desktop\\DS project\\Book1.xlsx')
wb = xlrd.open_workbook (loc)
sheet = wb.sheet_by_index(0)

data=[]
i = 0
for i in range (sheet.nrows):
     data.append(sheet.cell_value(i,0))
     i+=1
     
#linear search algorithm
#execution time


def to_search(data,n):
    i = 0
    while i < len(data):
        if data[i] == n:
            globals() ['index'] = i
            return True
        i = i + 1
    return False

index = -1
n = float(input("Enter any Number: "))
start=time.time()
if to_search(data,n):
    print("Number Found at " , index)
    elapsedTime=(time.time()-start)
else:
    print("Number Not Found")
    elapsedTime=(time.time()-start)

print ("elapsed time(sec):",elapsedTime)

