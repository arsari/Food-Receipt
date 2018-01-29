#!/usr/local/bin/python3
# this script is not compatible with python2

# encoding definition
"""coding=utf-8"""

# import module
import os
import platform

# determine os system to clear screen
my_os = platform.system()
if my_os == 'Windows':
    os.system('cls')  # on windows
else:
    os.system('clear')  # on linux / os x


# function definition
def receipt(order):
    # print receipt
    print('\n')
    print('********** PYTHON\'S CAFE **********')
    print((' ' * 12), 'OCALA, FL\n')
    print(('-' * 13), 'RECEIPT', ('-' * 13))
    print('Your order:\n')
    # print food items and calculate print subtotal
    subtotal_order = 0
    for food_ordered in order:
        print(' ', food_ordered, ' @  $%.2f' % (order[food_ordered]))
        subtotal_order += order[food_ordered]
    print('')
    print('-' * 35)
    print('Subtotal:', (' ' * 18), '$%.2f' % (subtotal_order))
    # calculate and print sales tax
    sales_tax = subtotal_order * .07
    if subtotal_order > 10:
        print('Sales Tax:', (' ' * 18), '$%.2f' % (sales_tax))
    else:
        print('Sales Tax:', (' ' * 17), '$%.2f' % (sales_tax))
    # calculate and print total order
    total_order = subtotal_order + sales_tax
    print(('=' * 35), '\nTotal Order:', (' ' * 15), '$%.2f\n' % (total_order))
    print('*' * 35)


# menu dictionary
menu_options = {
    'Hot dogs': 2.25,
    'Cheeseburger': 3.50,
    'Ham and cheese': 4.35,
    'Waffles': 5.25,
    'Taco': 3.15
}

# initial output
print('********** Pyrhon\'s Cafe Menu **********')
i = 1
for food_drink in menu_options:  # print menu
    print('%d. %s --- $%.2f each' % (i, food_drink, menu_options[food_drink]))
    i += 1
print(('*' * 40), '\n')

user_order = {}  # dictionary for user food order
user_selection = ''
while (user_selection != 0):  # input while loop
    user_selection = input('Enter name of food to order ("0" to exit): ')
    if user_selection in menu_options:
        user_order[user_selection] = menu_options[user_selection]
    elif user_selection == '0':
        receipt(user_order)  # call Receipt function
        break
    else:
        print('\n<< Food not in menu! >>\n')
