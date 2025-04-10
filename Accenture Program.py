#Importing Python libraries
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#Creating two attributes within a constructer function as part of a initialising constructor function
class Product:
    def __init__(self, name, price):
        self.name= name
        self.price = price

#Products created using the constructor function with pre-determined attributes (passed through the constructor function). 
eggs = Product("Eggs", price=0.35)
bananas = Product("Bananas", price=0.15)
apple = Product("Apple", price=0.60)
orange = Product("Orange", price=0.30)
cake = Product("Cake", price=7.30)
milk = Product("Milk", price=1.15)
yoghurt = Product("Yoghurt", price=2.15)
water = Product("Water", price=1.35)
crisps = Product("Crisps", price=1.20)

#Several methods coded below, breaking down the code into smaller readable (and managable chunks)
def introduction():
    username = input("Hello, what is your name? ")
    print(f"Welcome {username}. Learn more about the menu and add what you like to your cart")
    food_menu = print(['Eggs', 'Apples', 'Bananas', 'Oranges', 'Cake', 'Milk', 'Cookies', 'Yoghurt', 'Water', 'Crisps'])#Array which shall later call the attributes above
    main_menu(username)#Passing a parameter through to the next method

def main_menu(username):
    overall_total=0
    try:#Rather than providing an error, using a catch/except concept will allow the program to intercept potential and appropriately react to unwanted inputs
        info_count = int(input("How many products would you learn about? "))
        for i in range(info_count):#Loop based on the users desired number of learnings
            chosen_product = input("Please state the product based on list: ")
            final_cost = product_info(chosen_product)
            overall_total+= final_cost#Operator adding individual items (in a seperate method for the final cost)
            new_total=round(overall_total,2)
        print(f"Final total: £{new_total}")
        database(username, new_total)
    except ValueError:
        print("Please enter your answer in digits")
        main_menu(username)



def product_info(chosen_product):
    match chosen_product.lower():#Match-case used as a more readable version of the code (rather than if/elif/else statements)
        case "eggs":
            print(f"Product: {eggs.name}. Price: {eggs.price}.")
            cost = eggs.price
            print(cost)           
        case "bananas":
            print(f"Product: {bananas.name}. Price: {bananas.price}.")
            cost = bananas.price
        case "apples":
            print(f"Product: {apple.name}. Price: {apple.price}.")
            cost = apple.price
        case "oranges":
            print(f"Product: {orange.name}. Price: {orange.price}.")
            cost = orange.price
        case "cake":
            print(f"Product: {cake.name}. Price: {cake.price}.")
            cost = cake.price
        case "milk":
            print(f"Product: {milk.name}. Price: {milk.price}.")
            cost = milk.price
        case "yoghurt":
            print(f"Product: {yoghurt.name}. Price: {yoghurt.price}.")
            cost = yoghurt.price
        case "water":
            print(f"Product: {water.name}. Price: {water.price}.")
            cost = water.price
        case "crisps":
            print(f"Product: {crisps.name}. Price: {crisps.price}.")
            cost = crisps.price
        case _:
            print("Unrecorgnised product - Goodbye!")
            exit()
    confirmation=item_confirmation(chosen_product, cost) 
    return confirmation #Through the variable 'cost', updating the individual cost which shall feed back to the aggregate cost (variable: overall_total) from this return statement



def item_confirmation(chosen_product, cost):
    add_to_basket = input("Would you like to add " + chosen_product.lower() + " to your cart? ")
    if add_to_basket.lower() == "yes":#Lowercases to intercept any unwanted inputs (when requiring the same outcome)
        quantity = int(input("How many would you like? "))
        extra_cost=cost*quantity
    else:
        print("Not added")
        extra_cost=0    
    return extra_cost


def database(username, new_total):
    nothing_purchased = mpimg.imread("nothing_purchased.jpg")
    something_purchased = mpimg.imread("something_purchased.jpg")
    print(f"{username}, I have added your name and total to our database of previous customers")
    previous_customers_names = ["Kevin", "Ella", "Joe", "Hattie", "Fergus"]
    previous_customer_totals = []
    for i in range(5):
        random_prices = round(random.uniform(1, 10), 2)#Rounding the random prices of previous shoppers to 2 decimal places using the random library
        previous_customer_totals.append(random_prices)

    new_customer_price=float(new_total)
    previous_customers_names.append(username)
    with open("Todays_customers.txt","a") as file:#Appending a text written file with the users name and cost (seperate document)
            file.write("\n" + username + " - ")
    previous_customer_totals.append(new_customer_price)
    with open("Todays_customers.txt","a") as file:
            file.write(str(new_customer_price))
    pairing = list(zip(previous_customers_names, previous_customer_totals))#'Mapping' the random and new customer with their associated costs

    #Bubble sort organising least to most expensive shopper
    for i in range(len(pairing)):
        for j in range(0, len(pairing) - i - 1):
            if pairing[j][1] > pairing[j + 1][1]:
                temp = pairing[j]
                pairing[j] = pairing[j+1]
                pairing[j+1] = temp
    
        
    number=1
    for previous_customers_names, previous_customer_totals in pairing:
        print(f"{number}: {previous_customers_names} who paid £{previous_customer_totals}")#Printing bubble sort results         
        number+=1

    #If statement to show an happy/sad emjoi which is dependent on whether the customer has bought anything
    if new_customer_price>0:
        plt.imshow(something_purchased)
    else:
        plt.imshow(nothing_purchased)
    plt.axis('off') 
    plt.show()
    
    
introduction()#Calling the first method to start the program
    
