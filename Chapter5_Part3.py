smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 5]:
    if  smallest == None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print('After', smallest)
