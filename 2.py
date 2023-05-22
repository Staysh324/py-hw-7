def printOperationTable(operation, num_rows, num_columns): 
   print(*[i+1 for i in range(num_columns)], end = '\t') 
   print()
   for i in range(2, num_rows+1): 
      print (*[i if j == 1 else operation(j,i) for j in range(1, num_columns+1)], end = '\t')
      print()


num_rows = int(input("введите число строк: "))
num_columns = int(input("введите количество столбцов: "))
printOperationTable(lambda x,y: x**y, num_rows, num_columns)