from math import factorial

todays_gifts = 0
total_gifts = 0
for i in range(1, 1025):
    todays_gifts += i
    total_gifts += todays_gifts
print(todays_gifts, total_gifts)
