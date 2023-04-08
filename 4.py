# Input: 5 -> 5 1 6 5 9
# Output: 1_1 9_4

count_wm = int(input('--> '))
min_wm = int(input('wm--> '))
max_wm = min_wm

min_wm_i = 0
max_wm_i = 0
for i in range(1, count_wm):
    wm = int(input('wm--> '))
    if wm > max_wm:
        max_wm = wm
        max_wm_i = i
    if wm < min_wm:
        min_wm = wm
        min_wm_i = i

print(max_wm, max_wm_i, min_wm, min_wm_i)