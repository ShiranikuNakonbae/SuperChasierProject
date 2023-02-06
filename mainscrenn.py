# Import library needed for this to work
from superchasier import Transactions
from platform   import system as system_name  # Returns the system/OS name
from subprocess import call   as system_call  # Execute a shell command
import warnings

# Ignore future warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Define global variables in order to make it repeatable.
isCartMsg = 'Your cart has filled out with your item(s).'
isNotCartMsg = 'Your cart does not have any items.'
successMsg = 'Your cart has successfully updated.'
invalidInputMsg = 'Invalid input. Please enter a valid positive whole number.'

trx = Transactions()

def is_true_main():
    '''
    A boolean function that returns True if the cart is not empty, otherwise false.
    It was being used by all functions except add_item_main.

    The purpose is to encourage user that other functions are not available if add_item_main not executed yet.
    '''
    if (trx.is_true()):
        pass
    else:
        print(isNotCartMsg)
        main()


def add_item_main():
    '''
    A function to add a new item to the cart.

    Parameters:
    User will be prompted to enter an item name, item count/quantity, and item price, as long as they answer yes afterward.
    If the user's answer is no, it will be going back to main screen.

    Input:
    itemName [string] - The name of the item.
    itemCount [string] - The quantity of the itemName.
    itemPrice [string] - The price of the itemName.

    Process:
    itemCount and itemPrice will be type-cased into integer.
    Then all those values will be passed to add_item function in Transactions class.

    Output:
    It will print out a table containing its itemName, itemCount, itemPrice, and total.

    '''
    clear_screen() # Clear the main screen
    flag = True
    while flag: # While the flag is True, the code below will be executed continuously.
        try: # Control user input so that the input should match the requirements.
            print('Please enter your items, counts, and price.')
            itemName = input('Enter item name: ')
            itemCount = input('Please enter item count: ')
            itemPrice = input('Please enter item price: ')
            trx.add_item(itemName, int(itemCount), int(itemPrice))
        except ValueError: # If the user enter a wrong format, this exception will be printed.
            print(f'{invalidInputMsg} For item count and item price.')
            continue
        print('Do you want to enter item again? (yes or no)')
        if not input('> ').lower().startswith('y'): # Ask the user whether they want to enter item again.
            print(isCartMsg)
            trx.display_cart() # Call display_cart function in class Transactions to print out a cart table.
            flag = False # To break the while loop.
            clear_screen() # Clear the main screen
            main() # And go back to main menu.
        else:
            continue


def update_item_main(): 
    '''
    A function to update/modify user's cart.

    Parameters:
    A cart will be displayed as reference.
    Choices are given to the user for updating itemName, itemCount, or itemPrice they have entered in add_item function.

    Input:
    oldItem [String] - The itemName entered the cart user want to update.
    newItem [String] - The new itemName will be entered to the cart.
    newCount [String] - The new itemName's itemCount will be entered to the cart.
    newPrice [String] - The new itemName's itemPrice will be entered to the cart.

    Process::
    1. For updating itemName, user should enter exactly the itemName as oldItem and enter the new ItemName as newItem.
    Both names will be passed to update_item_name function in class Transactions.
    2. For updating itemCount, user should enter exactly the itemName and enter the newCount.
    Both names will be passed to update_item_count function in class Transactions.
    3. For updating itemPrice, user should enter exactly the itemName and enter the newPrice.
    Both names will be passed to update_item_price function in class Transactions.

    Output:
    An updated cart.

    '''
    clear_screen() # Clear the main screen
    trx.display_cart() # Call display_cart function in Transaction  class to print out a cart.
    flag = True
    while flag: # While the flag is True, the code below will be executed continuously.
        print('=====' * 10)
        print('Select what do you want to update: ')
        print('1. Item name update')
        print('2. Item count update')
        print('3. Item price update')
        print('4. View current cart')
        print('0. Back to main screen')
        try:
            select = int(input("Enter your selection > "))
            if select == 1:
                clear_screen()
                oldItem  = input('Enter item name to be updated: ')
                newItem = input('Enter a new item name: ')
                trx.update_item_name(oldItem, newItem)
                continue
            elif select == 2:
                clear_screen()
                oldItem  = input('Enter item name to be updated: ')
                newCount = input('Enter new count for the item name: ')
                trx.update_item_count(oldItem, int(newCount))
                continue
            elif select == 3:
                clear_screen()
                oldItem  = input('Enter item name to be updated: ')
                newPrice = input('Enter new price for the item name: ')
                trx.update_item_price(oldItem, int(newPrice))
                continue
            elif select == 4:
                clear_screen()
                trx.display_cart() # Call display_cart function in Transactions class to print out a cart.
                continue
            elif select == 0:
                flag = False # Break the while loop
                clear_screen() # Clear the main screen
                main()
            else:
                print('You have entered a wrong value. Try again with 1, 2, 3, 4, or 0.')
                continue
        except ValueError:
            print(invalidInputMsg)


def delete_item_main():
    '''
    A function that delete a single item in the cart.

    Parameters:
    A cart will be displayed for reference.
    There is a condition that will check whether the cart is empty or not.

    Input:
    deleteItem [String] - The itemName user want to delete.

    Process:
    If the cart is not empty:
    The deleteItem will be passed to delete_item method in class Transactions.
    Then, the main screen will be displayed.
    If the cart is empty:
    Main screen will be displayed.

    Output:
    An updated cart.

    '''
    clear_screen() # Clear the main screen
    trx.display_cart() # Call dispaly_cart function in Transactions class to print out a cart table.
    flag = True
    while flag:
        print('=====' * 10)
        deleteItem = input('Enter item name to be deleted: ')
        trx.delete_item(deleteItem)
        is_true_main()
        if not input('Do you want to delete another item? (yes/no) > ').lower().startswith('y'):
            flag = False
            clear_screen() # Clear the main screen
            main()
        else:
            continue


def reset_item_main():
    '''
    A function that will reset the cart.

    Parameters:
    A cart will be displayed as reference.
    There is a condition that will check whether the cart is empty or not.

    Input:
    A question for user whether they really want to reset the cart.

    Process:
    If the cart is not empty:
    And the user is answering no, main menu will be displayed.
    Otherwise, ResetItem method is called, and the cart will be cleared out.
    If the cart is empty:
    Main menu will be displayed.

    Output:
    An updated cart.

    '''
    clear_screen() # Clear the main screen
    trx.display_cart()
    print('Do you want to reset the order? (yes/no): ')
    if not input('> ').lower().startswith('y'):
        clear_screen() # Clear the main screen
        main()
    else:
        trx.reset_item()
        clear_screen() # Clear the main screen
        main()


def check_order_main():
    '''
    A function that will print out user cart.

    Parameters:
    Calling out CheckOrder method and go back to main menu.

    '''
    clear_screen() # Clear the main screen
    trx.check_order()
    input('Press enter to go back to main menu > ').lower().startswith(' ')
    main()


def checkout_main():
    '''
    A function that call TotalPrice function in class Transaction.

    Parameters:
    Method TotalPrice and print oout a thank-you message. Then will go back to main menu.

    '''
    clear_screen() # Clear the main screen
    trx.checkout()
    input('Press enter to go back to main menu > ').lower().startswith(' ')
    main()

            
def main():
    '''
    A main menu function.
    The store name is NAKONBAE SUPERSTORE.

    Parameters:
    User will be prompted to enter a number corresponding to its option.

    Input:
    A number entered by user and will route to its option.

    Process:
    Main menu always appears until the user enter 0 for exit.
    If the user input a number outside the option given, an error message will be displayed.

    '''
    while True:
        try:
            print('=====' * 10)
            print("WELCOME TO NAKONBAE SUPERSTORE")
            print('=====' * 10)
            print("Please choose the menu below by entering its corresponding number: ")
            print("1. Add items")
            print("2. Update items")
            print("3. Delete single item")
            print("4. Reset all items")
            print("5. Check order")
            print("6. Checkout cart")
            print("0. Exit")
            choices = int(input("Enter your selection > "))
            if choices == 0:
                exit()
            elif choices == 1:
                add_item_main()
            elif choices == 2:
                is_true_main()
                update_item_main()
            elif choices == 3:
                is_true_main()
                delete_item_main()
            elif choices == 4:
                is_true_main()
                reset_item_main()
            elif choices == 5:
                is_true_main()
                check_order_main()
            elif choices == 6:
                is_true_main()
                checkout_main()
            else:
                print('You have entered a wrong value. Try again with number: 1, 2, 3, 4, 5, 6, or 0 for exit.')
                print('=====' * 10)
        except ValueError:
            print('You have entered a wrong value. Try again with number: 1, 2, 3, 4, 5, 6, or 0 for exit.')


def clear_screen():
    """
    Clears the terminal screen.
    """
    # Clear screen command as function of OS
    command = 'cls' if system_name().lower().startswith('win') else 'clear'
    # Action
    system_call([command])


if __name__ == "__main__": # To start main() when the file is being executed in pyhton.
    main()