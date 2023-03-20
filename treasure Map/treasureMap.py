row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

map = [row1, row2, row3]


print(f'{row1}\n{row2}\n{row3}\n')

rowAndColumn = input("Enter the row and coloum you want to map")
posRow = rowAndColumn[0]
posColumn = rowAndColumn[1]

map[int(posRow) -1 ][int(posColumn )-1 ] =  "*"

print(f'{row1}\n{row2}\n{row3}\n')

rowAndColumn = input("Enter the row and coloum you want to map")
posRow = rowAndColumn[0]
posColumn = rowAndColumn[1]

map[int(posRow) -1 ][int(posColumn )-1 ] =  "*"

print(f'{row1}\n{row2}\n{row3}\n')

rowAndColumn = input("Enter the row and coloum you want to map")
posRow = rowAndColumn[0]
posColumn = rowAndColumn[1]

map[int(posRow) -1 ][int(posColumn )-1 ] =  "*"

print(f'{row1}\n{row2}\n{row3}\n')