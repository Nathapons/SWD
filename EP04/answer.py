number = int(input('enter your number '))
result = 1

# Get Factory value
while number >= 1:
    result *= number
    # Loop command
    number -= 1

# Get count zero
str_result = str(result)
count_zero = 0
for i in range(len(str_result)-1, -1, -1):
    if str_result[i] == '0':
        count_zero += 1
    else:
        break

print(f'มีเลข 0 ต่อท้าย {count_zero} ตัว')