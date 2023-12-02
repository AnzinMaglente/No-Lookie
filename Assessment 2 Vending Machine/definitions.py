# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 16:10:23 2023

@author: anzin
"""
import sqlite3
conn = sqlite3.connect("Item List.db")

shopping_cart = []
product = {
        'amount' : 1,
        'item' : 'b',
        'price' : 1.0,
        'type' : 'd',
        'bundle_item' : 'None',
        }
product_id = ("None")

def product_list():
    product_type = "chips"
    print("Formatting:\n\tProduct ID - Name - Price - Amount")
    
    print("\nChips:")
    while product_type == "chips":
        product_id = "C1"
        cur = conn.cursor()
        qry = cur.execute("SELECT item, price, amount, type FROM Item_Database WHERE product_id=?", (product_id,))
        res = qry.fetchone()
        print (f"\t{product_id} - {res[0]} - {res[1]} dhs - {res[2]} pieces")
        product_id = "C2"
        cur = conn.cursor()
        qry = cur.execute("SELECT item, price, amount, type FROM Item_Database WHERE product_id=?", (product_id,))
        res = qry.fetchone()
        print (f"\t{product_id} - {res[0]} - {res[1]} dhs - {res[2]} pieces")
        product_id = "C3"
        cur = conn.cursor()
        qry = cur.execute("SELECT item, price, amount, type FROM Item_Database WHERE product_id=?", (product_id,))
        res = qry.fetchone()
        print (f"\t{product_id} - {res[0]} - {res[1]} dhs - {res[2]} pieces")
        product_id = "C4"
        cur = conn.cursor()
        qry = cur.execute("SELECT item, price, amount, type FROM Item_Database WHERE product_id=?", (product_id,))
        res = qry.fetchone()
        print (f"\t{product_id} - {res[0]} - {res[1]} dhs - {res[2]} pieces")
        product_type = "chocolates"

    print("Chocolates:")
    while product_type == "chocolates":
        product_id = "Ch1"
        cur = conn.cursor()
        qry = cur.execute("SELECT item, price, amount, type FROM Item_Database WHERE product_id=?", (product_id,))
        res = qry.fetchone()
        print (f"\t{product_id} - {res[0]} - {res[1]} dhs - {res[2]} pieces")
        product_id = "Ch2"
        cur = conn.cursor()
        qry = cur.execute("SELECT item, price, amount, type FROM Item_Database WHERE product_id=?", (product_id,))
        res = qry.fetchone()
        print (f"\t{product_id} - {res[0]} - {res[1]} dhs - {res[2]} pieces")
        product_id = "Ch3"
        cur = conn.cursor()
        qry = cur.execute("SELECT item, price, amount, type FROM Item_Database WHERE product_id=?", (product_id,))
        res = qry.fetchone()
        print (f"\t{product_id} - {res[0]} - {res[1]} dhs - {res[2]} pieces")
        product_type = "pastries"
        
    print("Pastries:")
    while product_type == "pastries":
        product_id = "P1"
        cur = conn.cursor()
        qry = cur.execute("SELECT item, price, amount, type FROM Item_Database WHERE product_id=?", (product_id,))
        res = qry.fetchone()
        print (f"\t{product_id} - {res[0]} - {res[1]} dhs - {res[2]} pieces")
        product_id = "P2"
        cur = conn.cursor()
        qry = cur.execute("SELECT item, price, amount, type FROM Item_Database WHERE product_id=?", (product_id,))
        res = qry.fetchone()
        print (f"\t{product_id} - {res[0]} - {res[1]} dhs - {res[2]} pieces")
        product_id = "P3"
        cur = conn.cursor()
        qry = cur.execute("SELECT item, price, amount, type FROM Item_Database WHERE product_id=?", (product_id,))
        res = qry.fetchone()
        print (f"\t{product_id} - {res[0]} - {res[1]} dhs - {res[2]} pieces")
        product_type = "drinks"
        
    print("Drinks:")
    while product_type == "drinks":
        product_id = "D1"
        cur = conn.cursor()
        qry = cur.execute("SELECT item, price, amount, type FROM Item_Database WHERE product_id=?", (product_id,))
        res = qry.fetchone()
        print (f"\t{product_id} - {res[0]} - {res[1]} dhs - {res[2]} pieces")
        product_id = "D2"
        cur = conn.cursor()
        qry = cur.execute("SELECT item, price, amount, type FROM Item_Database WHERE product_id=?", (product_id,))
        res = qry.fetchone()
        print (f"\t{product_id} - {res[0]} - {res[1]} dhs - {res[2]} pieces")
        product_id = "D3"
        cur = conn.cursor()
        qry = cur.execute("SELECT item, price, amount, type FROM Item_Database WHERE product_id=?", (product_id,))
        res = qry.fetchone()
        print (f"\t{product_id} - {res[0]} - {res[1]} dhs - {res[2]} pieces")
        product_type = "softdrinks"
        
    print("Soft Drinks:")
    while product_type == "softdrinks":
        product_id = "SD1"
        cur = conn.cursor()
        qry = cur.execute("SELECT item, price, amount, type FROM Item_Database WHERE product_id=?", (product_id,))
        res = qry.fetchone()
        print (f"\t{product_id} - {res[0]} - {res[1]} dhs - {res[2]} pieces")
        product_id = "SD2"
        cur = conn.cursor()
        qry = cur.execute("SELECT item, price, amount, type FROM Item_Database WHERE product_id=?", (product_id,))
        res = qry.fetchone()
        print (f"\t{product_id} - {res[0]} - {res[1]} dhs - {res[2]} pieces")
        product_id = "SD3"
        cur = conn.cursor()
        qry = cur.execute("SELECT item, price, amount, type FROM Item_Database WHERE product_id=?", (product_id,))
        res = qry.fetchone()
        print (f"\t{product_id} - {res[0]} - {res[1]} dhs - {res[2]} pieces")
        product_type = "juice"
        
    print("Juice:")
    while product_type == "juice":
        product_id = "J1"
        cur = conn.cursor()
        qry = cur.execute("SELECT item, price, amount, type FROM Item_Database WHERE product_id=?", (product_id,))
        res = qry.fetchone()
        print (f"\t{product_id} - {res[0]} - {res[1]} dhs - {res[2]} pieces")
        product_id = "J2"
        cur = conn.cursor()
        qry = cur.execute("SELECT item, price, amount, type FROM Item_Database WHERE product_id=?", (product_id,))
        res = qry.fetchone()
        print (f"\t{product_id} - {res[0]} - {res[1]} dhs - {res[2]} pieces")
        product_id = "J3"
        cur = conn.cursor()
        qry = cur.execute("SELECT item, price, amount, type FROM Item_Database WHERE product_id=?", (product_id,))
        res = qry.fetchone()
        print (f"\t{product_id} - {res[0]} - {res[1]} dhs - {res[2]} pieces")
        product_type = "none"
        
    print ("""\nBundles (Just order one! It's 20% off!):
    Doritos Nacho Cheese & Sprite for only 3.68 dhs
    Lays Classic & Miranda for only 3.8 dhs
    Lays French Cheese & Coke for only 3.8 dhs
    Flaming Hot Cheetos & Mixed Berries Juice for only 2.88 dhs
    M&M & Orange Juice for only 2.28 dhs
    Kitkat & Apple Juice for only 2.67 dhs
    Chocolate Chip Cookie & Milk for only 4.4 dhs
    Biscuit & Hot Coffee for only 4.52 dhs
    """)

def decrease_amount(product_id):
    cur = conn.cursor()
    qry = cur.execute("SELECT amount FROM Item_Database WHERE product_id=?", (product_id,))
    res = qry.fetchone()
    amount = int(res[0]) - 1
    qry = "update Item_Database set amount=? where product_id=?;"
    conn.execute(qry,(amount, product_id))
    conn.commit()

def bundle_check(product_id, product, previous_product_id, p1, p2):
    cur = conn.cursor()
    qry = cur.execute("SELECT amount, item, price, type FROM Item_Database WHERE product_id=?", (product_id,))
    res = qry.fetchone()
    product['amount'] = res[0]
    if product['amount'] > 0:
        bundle_decision(product_id, product, previous_product_id, p1, p2)
    else:
        product['bundle_item'] = "None"
        return product

def bundle_decision(product_id, product, previous_product_id, p1, p2):
    cur = conn.cursor()
    qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
    res = qry.fetchone()
    new_price = float(res[4])
    product_check = False
    while product_check == False:
        print(f"""\nThere seems to be a bundle associated with your purchase, would you like to apply for it?
{p1} and {p2} for only {new_price} dhs.\t""")
        answer = input('\nPlease write "Yes" or "No": ')
        if answer == 'Yes':
            product['price'] = new_price
            product['type'] = 'bundle'
            print("\nThat will be " + str(product['price']) + " dhs, would you like anything else?\n")
            decrease_amount(product_id)
            product_check = True
            return product
        if answer == 'No':
            product_id = previous_product_id
            cur = conn.cursor()
            qry = cur.execute("SELECT amount, item, price, type, bundle_price, bundle_item FROM Item_Database WHERE product_id=?", (product_id,))
            res = qry.fetchone()
            product['bundle_item'] = "None"
            product['amount'] = res[0]
            print("\nThat will be " + str(product['price']) + " dhs, would you like anything else?\n")
            product_check = True
            return product
        else:
            print("Sorry, our system did not recognize your answer please try again.\n")

def product_menu_start(product_id, product):
    print("")
    cur = conn.cursor()
    qry = cur.execute("SELECT amount, item, price, type FROM Item_Database WHERE product_id=?", (product_id,))
    res = qry.fetchone()
    product['amount'] = res[0]
    if product['amount'] > 0:
        product['item'] = res[1]
        product['price'] = res[2]
        product['type'] = res[3]
        decrease_amount(product_id)
        print ("You added " + product['item'] + " to your cart, it cost " + str(product['price']) + " and it is in the " + product['type'] + " category.")
        return product
    else:
        print ("Sorry, but the item you selected ran out. Please choose again.")

def show_product(shopping_cart):
    print("Here are your products:")
    cart_check = False
    
    while cart_check == False:
        for product in shopping_cart:
            if product['type']  == "chips": 
                print("\tChips:")
                for product in shopping_cart:
                    if product['type']  == "chips":
                        print("\t\t" + product['item'] + " for " + str(product['price']) + " dhs")
                print("")
                cart_check = True
        cart_check = True
    cart_check = False
    
    while cart_check == False:
        for product in shopping_cart:
            if product['type']  == "chocolates": 
                print("\tChocolates:")
                for product in shopping_cart:
                    if product['type']  == "chocolates":
                        print("\t\t" + product['item'] + " for " + str(product['price']) + " dhs")
                print("")
                cart_check = True
        cart_check = True
    cart_check = False
    
    while cart_check == False:
        for product in shopping_cart:
            if product['type']  == "pastries": 
                print("\tPastries:")
                for product in shopping_cart:
                    if product['type']  == "pastries":
                        print("\t\t" + product['item'] + " for " + str(product['price']) + " dhs")
                print("")
                cart_check = True
        cart_check = True
    cart_check = False
    
    while cart_check == False:
        for product in shopping_cart:
            if product['type']  == "drinks": 
                print("\tDrinks:")
                for product in shopping_cart:
                    if product['type']  == "drinks":
                        print("\t\t" + product['item'] + " for " + str(product['price']) + " dhs")
                print("")
                cart_check = True
        cart_check = True
    cart_check = False
    
    while cart_check == False:
        for product in shopping_cart:
            if product['type']  == "softdrinks": 
                print("\tSoft Drinks:")
                for product in shopping_cart:
                    if product['type']  == "softdrinks":
                        print("\t\t" + product['item'] + " for " + str(product['price']) + " dhs")
                print("")
                cart_check = True
        cart_check = True
    cart_check = False
    
    while cart_check == False:
        for product in shopping_cart:
            if product['type']  == "juice": 
                print("\tJuice:")
                for product in shopping_cart:
                    if product['type']  == "juice":
                        print("\t\t" + product['item'] + " for " + str(product['price']) + " dhs")
                print("")
                cart_check = True
        cart_check = True
    cart_check = False
    
    while cart_check == False:
        for product in shopping_cart:
            if product['type']  == "bundle": 
                print("\tBundles:")
                for product in shopping_cart:
                    if product['type']  == "bundle":
                        print("\t\t" + product['item'] + " and " + product['bundle_item'] + " for " + str(product['price']) + " dhs")
                print("")
                cart_check = True
        cart_check = True
    cart_check = False
