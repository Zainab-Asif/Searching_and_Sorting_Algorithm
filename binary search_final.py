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

#binary search algorithm
#List must be sorted.
#If not, use listname.sort()

def to_search (data,n):
     lb = 0
     ub = len(data)-1
     while lb <= ub:
          mid = (lb + ub) // 2
          if data[mid] == n:
               globals()['index'] = mid
               return True
          else:
               if data[mid] < n:
                    lb = mid + 1
               else:
                    ub = mid - 1
     return False

data.sort()
index = -1
n = float(input("Enter any Number: "))
start=time.time()
if to_search (data,n):
     print("Number Found at " , index)
     elapsedTime=(time.time()-start)

else:
     print("Number Not Found")
     elapsedTime=(time.time()-start)

print ("elapsed time(sec):",elapsedTime)




