print("Hello World")
number = input("Enter a number (integer) here: ")
print(' ')
input_number = int(number)
if input_number >= 51 and input_number <= 100:
  print(str(number) + ' is greater than 50 and less than 101')
elif input_number >= 1 and input_number <= 10:
  print(str(number) + ' is greater than 0 and less than 11')
elif input_number > 100:
  print(str(number) + ' is greater than 100')
elif input_number > 10 and input_number < 51:
  print(str(number) + ' is greater than 10 and less than 51')
elif input_number == 0:
  print(str(number) + ': The number is 0')
else: 
  print(str(number) + ' is a negative integer')
