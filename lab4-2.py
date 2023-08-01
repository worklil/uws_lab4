"""
Create a fully commented program to:
display the first 13 odd numbers (starting from 0) and their sum.

"""
sum = 0
for counter in range(13):
    print(counter*2+1)
    odd_number = counter*2+1
    sum += odd_number
print("Sum =", sum)