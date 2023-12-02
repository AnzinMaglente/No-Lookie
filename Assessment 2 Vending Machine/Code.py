# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 10:12:30 2023

@author: Anzin R. Maglente
"""
import definitions
import sqlite3
conn = sqlite3.connect("Item List.db")

shopping_cart = []
product_id = ("None")
check = False
current_price = 0.0
total_price = float(0)

input("""Hello, welcome to the vending machine. This program was made by Anzin R. Maglente, 
if you find any errors please message him. Now without further adio, let us begin.\n""")

while check == False:
    product = {
            'amount' : 0,
            'item' : 'b',
            'price' : 0.0,
            'type' : 'd',
            'bundle_item' : 'None',
            }
    
    definitions.product_list()

    product_id = input("Please input the product ID, you would want to buy: ")
    definitions.product_menu_start(product_id, product)

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

    elif product['item'] == 'Lays French Cheese' or  product['item'] == 'Coke':
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

money_check = False
current_money = 0.0
change_money = 0.0
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
                        print("\n" + product['item'])
                    else:
                        print("\n" + product['item'] + " and " + product['bundle_item'])
                print("Thank you for shopping with us.")
                money_check = True
            else:
                print("Sorry, our system did not recognize your answer please try again.\n")

    else:
        money = input("Please input either 25 fils, 50 fils, 1 dhs, 5 dhs, 10 dhs, or 20 dhs into the machine to get your ordered products: ")
        if money == ("25 fils"):
            current_money += 0.25
        elif money == ("50 fils"):
            current_money += 0.25
        elif money == ("1 dhs"):
            current_money += 1
        elif money == ("5 dhs"):
            current_money += 5
        elif money == ("10 dhs"):
            current_money += 10
        elif money == ("20 dhs"):
            current_money += 20
        else:
            print("Sorry, our system did not recognize your answer please try again.\n")
