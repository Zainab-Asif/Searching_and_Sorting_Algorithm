import timeit
codeToTest="""
a=9
"""
elapsedTime=timeit.timeit(codeToTest,number=100)/100

print(elapsedTime)
