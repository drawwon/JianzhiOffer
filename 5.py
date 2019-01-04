def replaceBlank(string):
    # return string.replace(' ','%20')
    result = ''
    for i in string:
        if i==' ':
            result+='%20'
        else:
            result+=i
    return result

if __name__ == '__main__':
    print(replaceBlank("we are family"))