# nested loops = the inner loops will finish all of it's iterations before
#                  finishing one iteraion of "outer loop"
rows = int(input("How many rows: "))
columns = int(input("How many columns: "))
symbol = input("Enter a symbol to use : ")

for i in range(rows):
    for j in range(columns):
         print(symbol, end="")
    print("1")



