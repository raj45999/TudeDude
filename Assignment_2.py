print("Task 1:")
x= int(input("Enter a number: "))
if x % 2 ==0:
    print(f"{x} is an even number")
else:
    print(f"{x} is an odd number")
print()
print()
print("Task 2: ")
a=0
for i in range(1,51,1):
    a=a+i
print(f"The sum of numbers from 1 to 50 is: {a}")
