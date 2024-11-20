""" 
Find from second up to the fifth power of any number having 
absolute value less than 10 without using library function pow.
"""

num = float(input("Enter the number : "))

if num >= 10:
    print("Over the limit...")
    exit()

answer = num
for i in range(2, 5+1):
    answer = answer*num
    print(f"{num:.2f} to the power {i} is {answer:.2f}")
