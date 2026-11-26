# input number greater than 1
num = int(input("Enter the value of n: "))

# print the numbers from n to 1
print ("numbers from {0} to {1} are: ".format(num,1))

# loop to print numbers 
for i in range(num,0,-1):
	print (i)