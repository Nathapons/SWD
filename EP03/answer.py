num_list = []
# Get number list from user
while True:
    str_num = input('Enter your int number ')
    try:
        num = int(str_num)
        num_list.append(num)
    except ValueError:
        break

ans_index = 0
ans_max = num_list[ans_index]
for num in num_list:
    index = num_list.index(num)
    if num > ans_max:
        ans_index = index
        ans_max = num

print(num_list)
print(f'ลำดับที่มีค่ามากที่สุดของ {ans_max} คือ index = {ans_index}')