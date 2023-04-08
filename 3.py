# num_days = int(input('Num days --> '))
# days_list = []

# range(5) -> [0, 1, 2, 3, 4]
# range(5, 10) -> [5, 6, 7, 8, 9]
# range (1, 11, 2) -> [1, 3, 5, 7, 9]

# for i in range(num_days):
#     day = int(input('Day--> '))
#     days_list.append(day)

# print(days_list)
# max_len = 0
# temp_count = 0
# for temp in days_list:
#     if temp > 0:
#         temp_count +=1
#     else:
#         if temp_count > max_len:
#             max_len = temp_count
#         temp_count = 0
# print(max_len)

max_len = 0
temp_count = 0
num_days = int(input('Num days--> '))
for i in range(num_days):
    temp = int(input(f'Day_{i}--> '))
    if temp > 0:
        temp_count += 1
    else:
        temp_count = 0
    if temp_count > max_len:
        max_len = temp_count

print(max_len)