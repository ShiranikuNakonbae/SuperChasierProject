# %%
# Import the library needed 
import pandas as pd
from tabulate import tabulate
import warnings

# Ignore future warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Create Transaction class
class Transactions:
    '''
    This class handle all functions in the superstore application.

    It contains attributes:
    lower_total_items : the minimum of total transaction user will get lower_discount which is 5%.
    middle_total_items : the minimum of total transaction user will get mid_discount which is 8%.
    upper_total_items : the minimum of total transaction user will get upper_discount which is 10%.
    column_names : the column names of the cart.
    empty_cart_msg : the message will be displayed if the cart is empty.
    current_cart_msg : the message will be displayed current condition of the cart.

    And the rest is all functions defined accordingly.

    '''
    lower_total_items = 200000
    lower_discount = 0.05

    mid_total_items = 300000
    mid_discount = 0.08

    upper_total_items = 500000
    upper_discount = 0.1

    column_names = ['Item', 'Count', 'Price', 'Total']
    empty_cart_msg = 'Your cart is empty. Please add item to start shopping.'
    current_cart_msg = 'Your current cart so far.'


    def __init__(self):
        '''
        An initial class function containing an empty pandas dataframe that will be filled out with items and its attributes.

        '''
        # try to make item name as index
        self.df = pd.DataFrame(columns=self.column_names)  
    
    def is_true(self):
        '''
        A boolean function for checking the cart is empty or not that being used for another functions.
        If the cart is not empty, which means the AddItem function has called, another function could be called properly.
        Otherwise, an error message will be returned.

        '''
        if len(self.df) != 0:
            return True
        else:
            return False
    
    def display_cart(self):
        '''
        A function that storing and displaying the cart. 
        It can be called among functions within this class.

        '''
        print_cart = self.df.to_markdown(tablefmt="fancy_grid", index=False)
        return print(print_cart)

    def add_item(self, item_name, item_count, item_price):
        '''
        A function that handle adding item to the cart.

        This function receives item_name, item_count, and item_price then append it to dataframe.
        Total_item is resulted from multiplication of item_count and item_price.

        '''

        self.item_name = item_name
        self.item_count = item_count
        self.item_price = item_price

        if (isinstance(item_count, int) and item_count > 0) and (isinstance(item_price, int) and item_price > 0): # Checking user input. Whether the input was positif integer or not.
            total_item = item_count * item_price
            self.df = self.df.append({
                'Item' : item_name,
                'Count' : item_count,
                'Price' : item_price,
                'Total' : total_item
            }, ignore_index=True)
            self.display_cart() # Calling display_cart function.
        else:
            print('Invalid input. Please enter a valid positive whole number for item_count and item_price.')
        
    def update_item_name(self, item_name, new_item):
        '''
        A Function that handle updating the item_name user has entered into the cart.

        Input:
        item_name [String] - The name of the item user has entered into the cart.
        new_item [String] - The name of the new item user want to update.

        Process:
        If item_name is in the cart, it will be replaced to new_item.
        Then the cart will be updated.
        Otherwise, it will print out an error message.

        '''
        if self.is_true():
            if item_name in self.df['Item'].values:
                    print(f'{item_name} is in the list, and now become {new_item}.')
                    self.df['Item'] = self.df['Item'].replace(to_replace=item_name, value=new_item)
                    self.display_cart()
            else:
                    print(f'{item_name} is not in the list. Can not do further update. Please check item again.')
        else:
            print(self.empty_cart_msg)

    def update_item_count(self, item_name, new_count): 
        '''
        A function that handle updating the item_count user has entered into the cart.

        Input:
        item_name [String] - The name of the item user has entered into the cart.
        new_count [Integer] - The item_name's new_count user want to update.

        Process:
        If item_name is in the cart, item_count will be replaced to new_count.
        Then the cart will be updated.
        Otherwise, it will print out an error message.

        '''
        if self.is_true(): # Check if the cart is not empty by calling isTrue function.
            if (item_name in self.df['Item'].values) and (isinstance(new_count, int) and new_count > 0): # Check if the item_name is in the cart AND new_count is positive integer
                print(f'{item_name} is in the list, and now the count is {new_count}.')
                self.df.loc[self.df['Item'] == item_name, 'Count'] = new_count
                self.df.loc[self.df['Item'] == item_name, 'Total'] = new_count * self.df['Price'] 
                self.display_cart()
            else: # Otherwise, it will print out an error message
                print(f'{item_name} is not in the list or the {new_count} is not valid prositive whole number.')
                print(f'Please enter new name for item name or a positive whole number for new count.')
        else:
            print(self.empty_cart_msg)
    
    def update_item_price(self, item_name, new_price):
        '''
        A function that handle updating the item_price user has entered into the cart.

        Input:
        item_name [String] - The name of the item user has entered into the cart.
        new_price [Integer] - The item_name's new_price user want to update.

        Process:
        If item_name is in the cart, item_price will be replaced to new_price.
        Then the cart will be updated.
        Otherwise, it will print out an error message.

        '''
        if self.is_true(): # Check if the cart is not empty by calling isTrue function.
            if item_name in self.df['Item'].values and (isinstance(new_price, int) and new_price > 0): # Check if the item_name is in the cart AND new_price is positive integer
                print(f'{item_name} is in the list, and now the price is IDR{new_price} per each')
                self.df.loc[self.df['Item'] == item_name, 'Price'] = new_price
                self.df.loc[self.df['Item'] == item_name, 'Total'] = new_price * self.df['Count'] 
                self.display_cart()
            else: # Otherwise, it will print out an error message
                print(f'{item_name} is not in the list or the {new_price} is not valid positive whole number.')
                print(f'Please enter new name for item name or a positive whole number for new price.')
    
        else:
            print(self.empty_cart_msg)
    
    def delete_item(self, item_name):
        '''
        A Function that deletes an item from the cart.

        Input:
        item_name [String] - name of the item to be deleted.

        Process:
        If item_name is in the cart, then it will be directly deleted from the cart.
        Otherwise, an error message will be printed.

        '''
        if self.is_true():
            if item_name in self.df['Item'].values:
                self.df = self.df[self.df.Item != item_name]
                print(f'{item_name} was successfully deleted.')
                print(self.current_cart_msg)
                self.display_cart()
            else:
                print(f'{item_name} is not in the list. Choose a different item')
        else:
            print(self.empty_cart_msg)

        
    def reset_item(self):
        '''
        A function that will clear out all the items in the cart.

        Process:
        It will check whether the cart is empty or not.
        If so, it will drop all value user have entered.
        Otherwise, it will print out an error message.

        '''
        if self.is_true():
            self.df.drop(self.df.index, inplace=True)
            print('All items have successfully deleted from the list.')
            self.display_cart()

        else:
            print(self.empty_cart_msg)

    def check_order(self):
        if self.is_true():
            print(self.current_cart_msg)
            self.display_cart()
            grand_total = self.df['Total'].sum()
            print(f'Your grand total: IDR{grand_total}')
            print('Your order is ready to checkout. Please go to checkout page for discount eligibility.')
        else:
            print(self.empty_cart_msg)


    def checkout(self):
        '''
        A function that handle and calculate the cart.

        Process:
        If the cart is not empty:
        It will print out the current cart and grand_total, which was generated by summing all total columns.
        If grand_total is greater than upper_total_items (500_000), user will get an 10% discount.
        If grand_total is greater than mid_total_items (300_000), user will get an 8% discount.
        If grand_total is greater than lower_total_items (200_000), user will get an 5% discount.
        If grand_total is lower or equal to lower_total_items (200_000), user will not get any discount.
        Then the grand_total will be deducted by its discount and the value will be displayed.
        Otherwise:
        An error message will be displayed.
        '''
        if self.is_true():
            grand_total = self.df['Total'].sum()
            self.display_cart()
            print('=====' * 10)
            print(f'Your grand total: IDR{grand_total}')

            if grand_total > self.upper_total_items:
                grand_total = grand_total - (grand_total * self.upper_discount)
                print(f'You get 10% discount. Your total order become: IDR{grand_total:.0f}')
                print('Thank you for your order.')
            elif grand_total > self.mid_total_items:
                grand_total = grand_total - (grand_total * self.mid_discount)
                print(f'You get 8% discount. Your total order become: IDR{grand_total:.0f}')
                print('Thank you for your order.')
            elif grand_total > self.lower_total_items:
                grand_total = grand_total - (grand_total * self.lower_discount)
                print(f'You get 5% discount. Your total order become: IDR{grand_total:.0f}')
                print('Thank you for your order.')
            else:
                print(f'You did not get a discount.')
                print('Thank you for your order.')
        else:
            print(self.empty_cart_msg)