
import os 
folderpath = r"D:\Python\Projects\Github\awesome-python-projects\Python_Projects"
filepath = os.path.join(folderpath, "TODO.txt")
print(filepath)


if not os.path.exists(filepath):
    os.chdir(r'D:\Python\Projects\Github\awesome-python-projects\Python_Projects')
    with open('TODO.txt','w') as f: 
        f.write("____________________TODO LIST________________________\n")
        f.write("                TIME         WORK                      ")
    no_of_items = 0
else:
    with open('TODO.txt','r') as f:
        lines = f.readlines()
    no_of_items = len(lines) - 2 
    


#####TODO LIST


while True:
    os.chdir(r'D:\Python\Projects\Github\awesome-python-projects\Python_Projects')
    print('press 1: Add Item\n 2:Delete Item\npress 3: Update Item\npress 4: Display Item\n press 5: Exit')
    n=int(input())
    
    if n==1:
        todo=[]
        print('Enter the time in HH:MM format(24 Hours Format)')
        time = input()
        print('Enter your work')
        work=input()
        no_of_items +=1
        with open('TODO.txt','a') as f:
            f.write("\n"+str(no_of_items)+" "+time+"     "+work)
            
    elif n==2:
        if no_of_items <=0:
            print("There is not item in the list please add some items")
        else:
            print("______________________________________________")
            print("Your cuttent list:")
            todo=[]
            with open("TODO.txt") as f:
                for i in f.readlines():
                    print(i)
                    todo.append(i)
            print('_______________________________________________')
            print("Enter the position of the item you want to delete : ")
            pos=int(input())
            if pos <=0:
                print("Enter a valid position")
            else:
                todo.pop(pos+1)
                no_of_items-=1
                if no_of_items<=0:
                    print("Congratulations your todo list is empty!")
                
                with open('TODO.txt','w') as f:
                    for i in range(len(todo)):
                        if i >= pos+1:
                            f.write(str(pos)+todo[i][1:])
                            pos+=1
                        else:
                            f.write(todo[i])
    elif n==3:
        print("________________________________________________")
        print("Your current list:")
        todo=[]
        with open("TODO.txt") as f:
            for i in f.readlines():
                print(i)
                todo.append(i)

        print("__________________________________________________")
        print("Enter the position of the item you want to update")
        pos=int(input())
        if pos<=0:
            print("Please enter the valid position")
        elif pos > no_of_items:
            print("Plesae entere a vlid postion <= {}.format(no_of_items)")
        else:
            print('What you want to update : ')
            print("press 1: Time\npress 2: Work")
            choice = int(input())
            if choice ==1:
                print('Enter your updateed time:')
                time=input()
                p = todo[pos+1].index(":")
                
                y =0
                with open('TODO.txt','w') as f:
                    for i in range(len(todo)):
                        if i == pos+1:
                            f.write(str(pos)+" "+time+" "+' '.join(todo[pos+1][p+3]))
                        else:
                            f.write(todo[i])
            elif choice ==2:
                print("Please enter your updated work")
                work = input()
                p = todo[pos+1].index(":")
                y=0
                with open('D:TODO.txt','w') as f:
                    for i in range(len(todo)):
                        if i == pos+1:
                            f.write(str(pos) + " "+''.join(todo[pos+1][p-1:p+3])+" "+work)
                        else:
                            f.write(todo[i])
    elif n==4:
        print("Your current list: ")
        todo=[]
        print("________________________________________________")
        with open("TODO.txt",'r') as f:
            for i in f.readlines():
                print(i)
                todo.append(i)
        print("_________________________________________________")
        print("Press 1: Add Item \nPress 2: Delete the Item\nPress 3: Update item\nPress 4:Display Items\nPress 5:Exit")
        n=int(input())
    else:
        break
    
print("Thank You for using our application ")                            
                            
                            
                
        
                            
                                        
            

