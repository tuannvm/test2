spam = ['apples', 'banana', 'tofu', 'cats', 1]
def comma(list):
    result = None
    for i in range(len(list)):
        if i == (len(list) - 1):
            result = str(result) + str(list[i])
            break
        result = str(result) + str(list[i]) + ', '

    return result


print (comma(spam))