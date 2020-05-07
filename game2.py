import random


choice=['rock','scissors','paper']

human_wins=[choice[0]+choice[1], choice[1]+choice[2], choice[2]+choice[0]]    
    
while True:
    print('to quit press q')
   
    
    human_choice=input('rock , scissors or paper: ')
    computer_choice=random.choice(choice)
    if human_choice == 'q':
        break 
    
    
    

    if human_choice in choice:
        print(computer_choice)
        
        if human_choice == 'q':
           break
        if human_choice==computer_choice:
            print("it's a draw")

        elif human_choice + computer_choice in human_wins :
            print('human wins')

        else:
            print('computer wins')

    else:
        
        print('try to type rock , scissors or paper in')



