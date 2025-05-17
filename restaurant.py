#greet 
print("welcome to python  cuisine")

#define the menu of dektop

menu = {
    'pizza' : 250,
    'burger':200,
    'salad':100,
    'coffe':350,
}


print("1.pizza:$250\n2.burger:$200\n3.salad:$100\n4.coffe:$350")

order_total = 0

item_1 = input("enter the name of the item you want to order")
if item_1 in menu:
        order_total += menu[item_1] 
        print(f" your item has benn added ")
else:
    print(f"ordered item is not available")

another_order = input("do you want to make another order ? (yes/no)")   
if another_order =="yes":
    item_2 = input("enter the name of order 2")
    if item_2 in menu:
        order_total += menu[item_2] 
        print(f" your item has benn added ")
    else:
        print(f"ordered item {item_2} is not available")

print(f"the total amount of the order is{ order_total}")        

