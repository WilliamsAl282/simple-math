# Alex Williams
# 9/23/24
# basic math

# Practice 1
num1 = 10
num2 = 15

sum = (num2 + num1)
subtraction = (num2 - num1)
multiplication = (num1 * num2)
quotient_remainder = (num1 / num2)

print(f'{num1} plus {num2} equals {sum}')
print(f'{num2} minus {num1} equals {subtraction}')
print(f'{num1} times {num2} equals {multiplication}')
print(f'{num1} divided by {num2} equals {quotient_remainder}')

# practice 2

lv_length = float(input('What is the length of your living room in feet?: \n'))
lv_width = float(input('What is the width of your living room on feet?: \n'))
room_area = (lv_length * lv_width)
print(f'The area of the rectangular room is {room_area} square feet')

# practice 3

name = 'Alex'
age = 17
fav_color = 'Blue'
message = 'My name is {0} and my age is {1} years old. My favorite color is {2}' .format(name, age, fav_color)
print(message)

cabbage = 4.15
bananas = 2.08
beets = 2.43

cabbage_tax = 4.15 * 0.06
banana_tax = 2.08 * 0.06
beets_tax = 2.43 * 0.06

cabbage_total = cabbage + cabbage_tax
bananas_total = bananas + banana_tax
beets_total = beets + beets_tax

grand_total = cabbage_total + bananas_total + beets_total

print(f'The sales tax on the cabbage is {cabbage_tax:.2f}$ and the grand total for the cabbage is {cabbage_total:.2f}$.')
print(f'The sales tax on the bananas are {banana_tax:.2f}$ and the grand total for the bananas is {bananas_total:.2f}$.')
print(f'The sales tax on the beets was {beets_tax:.2f}$ and the grand total is {beets_total:.2f}$.')
print(f'The grand total of all items togethor is {grand_total:.2f}$.')




friend_name = 'JJ'
friends_school = 'Elk Rapids High School'
message2 = 'My friends name is {0} and he attends {1} with me.' .format(friend_name, friends_school)
print(message2)