# #part 1
# def trebuchet(truc):
#     result=''
#     for i in truc:
#         if i.isdigit():
#             result += i
#             break
#     for j in reversed(truc):
#         if j.isdigit():
#             result += j
#             break
#     return result


# with open ("dataDay1.txt", "r") as f:
#     result = 0
#     for ligne in f:
#         result += int(trebuchet(ligne))
#     print(result)

#part 2
data = {"one":1,"two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9 }

def trebuchet(truc):
    result1=''
    result2=''
    digit1=""
    digit2=""
    for i in truc:
        digit1 += i
        for key in data.keys():
            if key in digit1:
                result1 += str(data[key])
                break
        if result1 != '':
            break

    for j in reversed(truc):
        digit2 = j+digit2
        for key in data.keys():
            if key in digit2:
                result2 += str(data[key])
                break
        if result2 != '':
            break
    return result1+result2

with open ("dataDay1.txt", "r") as f:
     result = 0
     for ligne in f:
         result += int(trebuchet(ligne))
     print(result)