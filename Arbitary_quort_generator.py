import random
import quote
import quote.quote

def generate_quote():
    print("1. Inspirational")
    print("2. Motivational")
    print("3. Funny")
    print("4. Love")
    print("5. Life")
    
    choice = int(input("Enter Your choice: "))
    if choice == 1:
        search_term = "Inspirational" 
    elif choice == 2:
        search_term = "Motivational" 
    elif choice == 2:
        search_term = "Funny" 
    elif choice == 2:
        search_term = "Love" 
    elif choice == 2:
        search_term = "Life" 
    else:
        print('Invalid Choice')
        return 
    
    quotes = quote.quote(search_term)
    num=int(input("Enter the number of quotes to generate"))
    
    for i in range(num):
        print(i+1, ".", random.choice(quotes))

if __name__ == "__main__":
    generate_quote()
         