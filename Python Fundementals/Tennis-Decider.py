'''
Approach: Most straight-forward approach is to use a bunch of nested if statements, 
then optimize for readability if possible
'''

valid = False
while not valid:
    outlook = input("How is the outlook? (Sunny, Overcast, Rain): ")
    
    #Overcast Case
    if outlook == 'Overcast':
        valid = True
        print("Tennis Time!!")
    
    #Sunny Case
    elif outlook == 'Sunny':
        while not valid:
            valid = True #Assume innocent until proven guilty
            humidity = input("How is the Humidity? (High, Normal): ")
            if humidity == "High":
                print("No Tennis Today :(")
            elif humidity == "Normal":
                print("Tennis Time!!")
            else:
                print("I am a simple robot and don't understand, please try again", end='\n\n')
                valid = False
    
    #Rainy Case            
    elif outlook == 'Rain':
        while not valid:
            valid = True
            wind = input("How is the Wind? (Strong/Weak): ")
            if wind == "Strong":
                print("No Tennis Today :(")
            elif wind == "Weak":
                print("Tennis Time!!")
            else:
                print("I am a simple robot and don't understand, please try again", end='\n\n')
                valid = False
                
    else:
        print("I am a simple robot and don't understand, please try again", end='\n\n')
            
            