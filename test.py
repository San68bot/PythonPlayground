def addition(num1, num2):
    return num1 + num2

def dis(num1, num2):
    return int(num1 * (num2 / 100.0))

def curzon(num):
    return ((2 ** num) + 1) % ((2 * num) + 1) == 0

def upload_count(dates, month):
    count = 0
    for date in dates:
        if date.split(" ")[0] == month:
             count += 1
    return count

def number_split(num):
    if num % 2 == 0:
        return [num/2, num/2]
    else:
        return [num/2, num/2+1]

test = input("Enter a number: ")
print(test)