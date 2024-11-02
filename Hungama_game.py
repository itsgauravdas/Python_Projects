from os import system
import random 

def cls():
    system('cls')
    
def hungama_game():
    cls()

    print("\nWelcome")
    print("Lets play Hangman\n")
    
    name=input("What is your name")
    name=name.capitalize()
    print("Hello "+ name + ", Its time to play Hungama")
    print("Start Guessing...")
    guess_word=[]
    
    #Create a variable with empty value 
    guesses=""
    
    #Datermine the number of turns 
    turns=10 
    
    #Here we set the secret 
    
    words=[
        "Forrest Gump",
        "Hangman Project",
        "The Godfather",
        "The Green Mile",
        "Hotel Rwanda",
        "Goodfellas",
        "Scarface",
        "The Terminal",
        "Million Dollar Baby",
        "Driving Miss Daisy",
        "Catch Me If You Can",
        "Chinatown",
        "The Departed",
        "Dances with Wolves",
        "Ford v Ferrari",
        "Little Women",
        "A Star Is Born",
        "Dear Basketball"
    ]
    
    word=random.choice(words)
    word=word.upper()
    
    while turns>10:
        failed=0
        
        for char in word:
            if char in guesses:
                print(char,end='')
                
            elif char ==" ":
                print(' / ',end='')
                
            else:
                print("_",end='')
                failed+=1
    

        if failed == 0:
            print("\n "+ name + "you WON!")
            break
        
        guess=input("\nGuess a Character : ")
        guess=guess.upper()
        
        if len(guess) > 1:
            break 
        
        
        guesses+=guess
        if (guess not in word) and (guess not in guess_word):
            turns-=1
            guess_word.append(guess)
            print('\nWrong')
        cls()
        
        print("\nYou have ", + turns, "more guesses")
        print("\nWrong Character's Entered : ", guessed_word)
        
        if turns == 0:
            print('\nGame is OVER, you lost : 0')
            
    check=input("\nDo you want to play again Y/N?")
    if check =='Y' or check=='y':
        hungama_game()
        

if __name__=='__main__':
    hungama_game()
                