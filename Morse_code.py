import pyfiglet 
import pyperclip


normal_word = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
               "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..",
              "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."]



def option_menu():
    print(pyfiglet.figlet_format("MORSE CODE"))
    option = int(input("Choose 1. For Encoding and 2.For Decoding and 3 For Exit:"))
    if option == 1 :
        word = input("Enter the sentance that you want to encode:-")
        word = word.upper()
        code_form = ""
        for letter in word:
            if letter == " ":
                code_form+="/ "
            else:
                ind = normal_word.index(letter)
                code_form+=morse_code[ind]
                code_form+=" "
        
        print(f"{word} in morse codde is {code_form}")
        pyperclip.copy(code_form)
        print("Copied it in clipboard 😊")
        print("\n")
        option_menu()
        
    if option == 2:
        decode_form = ""
        encode_word = input("Enter the sentence that you want to decode:")
        encode_word = encode_word.split(" ")
        for item in encode_word:
            if item.isalnum() or item.isalpha():
                print("Please enter valid morse code 😀")
                option_menu()
            if item == "/":
                decode_form+= " "
                continue
            if item == "":
                continue
            else:
                ind = morse_code.index(item)
                decode_form+= normal_word[ind]
        print(f"{encode_word} in decoded form is {decode_form}")
        pyperclip.copy(decode_form)
        print("Copied it to clipboard 😊")
        print("\n")
        option_menu()
    
    if option == 3:
        print("Thanks for using this page")
        exit()
                
          
         
    
option_menu()