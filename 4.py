def getNumFromArray(l, num):
    if not l:
        return False
    row = 0
    column = len(l[0])-1
    while row < len(l) and column >= 0:
       if num > l[row][column]:
           row += 1
       elif num < l[row][column]:
           column -= 1
       else:
           return True
    return False

if __name__ == '__main__':
    print(getNumFromArray([[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]],2))

