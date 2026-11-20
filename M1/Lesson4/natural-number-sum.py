# Python program to calculate the sum of the first n natural numbers using a while loop
n = int(input("enter the value of n: "))
total_sum = 0
num = 1

while num <= n:
    total_sum += num
    num += 1

print(f"The sum of the first {n} natural numbers is {total_sum}")