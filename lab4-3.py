"""
Question 3
Edit Q2 to allow the user to choose
a) how many odd numbers they want to sum (starting from 0)
b) how many odd numbers they want to sum (starting from a number of their choice)
"""

n = int(input("how many odd numbers they want to sum:"))
sum = 0
for counter in range(n):
    print(counter*2+1)
    odd_number = counter*2+1
    sum += odd_number
print(sum)