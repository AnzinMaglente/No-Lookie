# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 10:12:30 2023

@author: Anzin R. Maglente
"""

import definitions
import sqlite3
conn = sqlite3.connect("Item List.db")
#This is a comment:
"""Above this line, shows two connections to different files
        Definitions is the other part of this code, where you can find several functions that speeds
        up several processes.
        SQlite3('Item List.db') on the other hand, connects this file to my database which has the
        product_id, item, price, bundle, type, and amount of each product"""

shopping_cart = [] #This creates a list where the bought products will end up in. 
product_id = ("None")
check = False
current_price = 0.0
total_price = float(0)
money_check = False
current_money = 0.0
change_money = 0.0
#Above are variables that will be used later.

input("""Hello, welcome to the vending machine. This program was made by Anzin R. Maglente, 
if you find any errors please message him. Now without further adio, let us begin.\n""")

#This is a comment:
"""The while loop below allows the program to loop until the user is satisfied with
their selections, it allows for multiple products to be selected from the vending machine."""

while check == False:
    product = {
            'amount' : 0,
            'item' : 'b',
            'price' : 0.0,
            'type' : 'd',
            'bundle_item' : 'None',
            }
    #This is the product's values that are impacted by the user's input.
    
    definitions.product_list() 
    #This is a comment:
    """
    This line of code gets a definitions called "product_list()" from the definitions file. 
    Which shows off the products, their price, and the amount left on the product.
    """
    
    product_id = input("Please input the product ID, you would want to buy: ")
    #This allows the user to select an item to add to their shopping cart.
    
    definitions.product_id_assurance(product_id)
    
    cur = conn.cursor()
    qry = cur.execute("SELECT product_id FROM Item_Database")
    res = qry.fetchall()
    database_list = [x[0] for x in res]
    if product_id in database_list:
        print("")
        cur = conn.cursor()
        qry = cur.execute("SELECT amount, item, price, type FROM Item_Database WHERE product_id=?", (product_id,))
        res = qry.fetchone()
        product['amount'] = res[0]
        if product['amount'] > 0:
            product['item'] = res[1]
            product['price'] = res[2]
            product['type'] = res[3]
            definitions.decrease_amount(product_id)
            print ("You added " + product['item'] + " to your cart, it cost " + str(product['price']) + " and it is in the " + product['type'] + " category.")
        else:
            input("Sorry, but the item you selected ran out. Please choose again. ")
            continue
    else:
        input("Sorry, our system did not recognize your answer please try again. ")
        continue
    
    definitions.product_menu_start(product_id, product)
    #

    if product['item'] == 'Doritos Nacho Cheese' or product['item'] == 'Sprite':
        if product['item'] == 'Doritos Nacho Cheese':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("SD2")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)
        elif product['item'] == 'Sprite':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("C1")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)

    elif product['item'] == 'Lays Classic' or product['item'] == 'Miranda':
        if product['item'] == 'Lays Classic':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("SD3")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)
        elif product['item'] == 'Miranda':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("C2")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)

    elif product['item'] == 'Lays French Cheese' or product['item'] == 'Coke':
        if product['item'] == 'Lays French Cheese':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("SD3")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)
        elif product['item'] == 'Coke':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("C3")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)

    elif product['item'] == 'Flaming Hot Cheetos' or  product['item'] == 'Mixed Berries Juice':
        if product['item'] == 'Flaming Hot Cheetos':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("J3")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)
        elif product['item'] == 'Mixed Berries Juice':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("C4")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)

    elif product['item'] == 'M&M' or  product['item'] == 'Orange Juice':
        if product['item'] == 'M&M':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("J2")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)
        elif product['item'] == 'Orange Juice':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("Ch1")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)

    elif product['item'] == 'Kitkat' or  product['item'] == 'Milk':
        if product['item'] == 'Kitkat':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("J1")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)
        elif product['item'] == 'Orange Juice':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("Ch2")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)

    elif product['item'] == 'Chocolate Chip Cookie' or  product['item'] == 'Apple Juice':
        if product['item'] == 'Chocolate Chip Cookie':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("D2")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)
        elif product['item'] == 'Milk':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("P1")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)

    elif product['item'] == 'Biscuit' or  product['item'] == 'Apple Juice':
        if product['item'] == 'Biscuit':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("D2")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)
        elif product['item'] == 'Hot Coffee':
            previous_product_id = product_id
            p1 = product['item']
            product_id = ("D3")
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = res[1]
            p2 = product['bundle_item']
            definitions.bundle_check(product_id, product, previous_product_id, p1, p2)
    else:
        print ("There does not seem to be a bundle associated with your purchase")

    shopping_cart.append(product)
    
    continue_check = False
    while continue_check == False:
        continue_answer = input('Do you want to continue your shopping? Please enter "Yes" or "No" ')
        if continue_answer == "Yes":
            continue_check = True
        elif continue_answer == "No":
            check = True
            continue_check = True
        else:
            print("Sorry, our system did not recognize your answer please try again.\n")

for product in shopping_cart:
    current_price = (product['price'])
    total_price += current_price

input("\nProcessing order...\n")

print("Your total purchase is " + str(total_price) + " dhs\n")
definitions.show_product(shopping_cart)

while money_check == False:
    if current_money >= total_price:
        change_money = current_money - total_price
        if change_money == 0:
            print("\n~~ A sound is heard in the opening beneath ~~\n")
            print("Here are your products:")
            for product in shopping_cart:
                if product['type'] == "bundle":
                    print("\t" + product['item'] + " and " + product['bundle_item'])
                else:
                    print("\t" + product['item'])
            print("\nThank you for shopping with us.")
            money_check = True
        else:
            change_check = input('\nPlease enter "Yes" keep your change and "No" if you want to donate it to charity, it is ' + str(change_money) + ' dhs: ')
            if change_check == 'Yes':
                print("\nHere is your change: " + str(change_money))
                print("\n~~ A sound is heard in the opening beneath ~~\n")
                print("Here are your products:")
                for product in shopping_cart:
                    if product['type'] == "bundle":
                        print("\t" + product['item'] + " and " + product['bundle_item'])
                    else:
                        print("\t" + product['item'])
                print("\nThank you for shopping with us.")
                money_check = True
            elif change_check == 'No':
                print("\n~~ A sound is heard in the opening beneath ~~\n")
                print("Here are your products:")
                for product in shopping_cart:
                    if product['type'] == "bundle":
                        print("\n" + product['item'] + " and " + product['bundle_item'])
                    else:
                        print("\n" + product['item'])
                print("Thank you for shopping with us.")
                money_check = True
            else:
                print("Sorry, our system did not recognize your answer please try again.\n")

    else:
        money = input("Please input either 25 fils, 50 fils, 1 dhs, 5 dhs, 10 dhs, or 20 dhs into the machine to get your ordered products: ")
        if money == ("25 fils") or ("25 Fils") or ("0.25"):
            current_money += 0.25
        elif money == ("50 fils") or ("50 Fils") or ("0.50"):
            current_money += 0.25
        elif money == ("1 dhs") or ("1 Dhs") or ("1"):
            current_money += 1
        elif money == ("5 dhs") or ("5 Dhs") or ("5"):
            current_money += 5
        elif money == ("10 dhs") or ("10 Dhs") or ("10"):
            current_money += 10
        elif money == ("20 dhs") or ("20 Dhs") or ("20"):
            current_money += 20
        else:
            print("Sorry, our system did not recognize your answer please try again.\n")
