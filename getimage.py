import sys
import requests


def main():
    myurl = input('enter a url: ')
    response = requests.get(myurl).text
    lines = srcparse(response)
    linklist = linkparse(lines)
    print(linklist)


def srcparse(string):
    result = []
    li = string.split('\n')
    for i in li:
        if i.find(".png") != -1 or i.find(".jpg") != -1 or i.find(".bmp") != -1:
            result.append(i)
    return result


def linkparse(li):
    result = []
    for i in li:
        start = 0
        end = 0
        a = i.find(".png")
        b = i.find(".jpg")
        c = i.find(".bmp")
        if a != -1:
            end = a + 4
        if b != -1:
            end = b + 4
        if c != -1:
            end = c + 4
        if i.find('=') != -1:
            for ch in reversed(range(0, end)):
                if i[ch] == '=':
                    start = ch + 1
        elif i.find('(') != -1:
            start = i.find('(') + 1
        else:
            print('AAAAAAAA')
        if a != -1 or b != -1 or c != -1:
            result.append(removeref(i[start:end]))
        else:
            print('error')
    return result


def removeref(string):  # gets rid of // reference to site files
    result = string
    if string.find('//') != 0:
        k = string.find('//')
        result = string[k + 2:len(string)]
    return result


if __name__ == '__main__':
    main()
