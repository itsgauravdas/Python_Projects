def calculate_split(total_amount: float,number_of_people: int,currency:str)->None:
    if number_of_people<1:
        raise ValueError('Number of people should be at lease one.')
    
    #Calculate the share per person
    share_per_person:float=total_amount/number_of_people
    
    #Print the result
    print(f'Total Expenses : {currency}{total_amount:,.2f}')
    print(f'Number of people:{ number_of_people}')
    print(f'Each person should pay: {currency}{share_per_person}')
    
def main()->None:
    try:
        #input for total number
        total_amount:float=float(input('Enter the total number of expense::'))
        
        #Input for number of people
        number_of_people:float=float(input('Enter the total number of epeople sharing the xpense::'))
        
        #Call the function to calculate the split with currency set to rupees
        calculate_split(total_amount,number_of_people,currency="₹")
        
    except ValueError as e:
        print(f'Error:{e}')
        
if __name__=='__main__':
    main()