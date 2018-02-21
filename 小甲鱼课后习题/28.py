f = open('C:/Program Files/Python37/My Scripts/28.txt', 'w')
f.write('I\nLove\nPython')
f = open('C:/Program Files/Python37/My Scripts/28.txt', 'r')
for each in f:
    print(each)
f.close()
print('\nThe End.')
