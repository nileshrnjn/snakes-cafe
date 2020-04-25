"""
Lab 1 assignment with the below requirements:
    1. When run, the program should print an intro message and the menu for the restaurant
    2. The restaurant’s menu should include appetizers, entrees, desserts, and beverages. At least 3 in each category
    3. The program should prompt the user for an order
    4. When a user enters an item, the program should print an acknowledgment of their input
    5. The program should tell the user how to exit
"""

from textwrap import dedent

def print_welcome_message():
    welcome_message = """
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************
    """
    print(dedent(welcome_message))

def create_items_list():
    menu_items = {
        "Wings": 0,
        "Cookies": 0,
        "Spring Rolls": 0,
        "Salmon": 0,
        "Steak": 0,
        "Meat Tornado": 0,
        "A Literal Garden": 0,
        "Ice Cream": 0,
        "Cake": 0,
        "Pie": 0,
        "Coffee": 0,
        "Tea": 0,
        "Unicorn Tears": 0
    }
    return menu_items

def print_menu(items_list):
    menu = """
    Appetizers
    ----------
    {}
    {}
    {}

    Entrees
    -------
    {}
    {}
    {}
    {}

    Desserts
    --------
    {}
    {}
    {}

    Drinks
    ------
    {}
    {}
    {}
    """.format(*items_list)
    print(dedent(menu))

def process_order(items_list):
    prompt = """
    ***********************************
    ** What would you like to order? **
    *********************************** 
    """
    while True:
        order = input(dedent(prompt))
        if order == "quit":
            break
        formatted_order = order.title()
        if formatted_order not in items_list:
            print("Sorry, we don't serve that!")
        else:
            items_list[formatted_order] += 1
            item_count = items_list[formatted_order]
            print(f"** {item_count} order of {formatted_order} have been added to your meal **")

# def print_final_order(items_list):
#     final_order = ""
#     for items in items_list:
#         if items_list[items] > 0:
#             message = " orders of " if items_list[items] > 1 else " order of "
#             final_order = final_order + str(items_list[items]) + message + items + "\n"
#     if len(final_order) > 0:
#         print("Thank you for choosing us!")
#         print("Your final order is: ")
#         print(final_order)
    
def main():
    print_welcome_message()
    items_list = create_items_list()
    print_menu(items_list)
    process_order(items_list)
    # print_final_order(items_list)

if __name__ == "__main__":
    main()