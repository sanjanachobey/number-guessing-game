name = input("Type our name: ")
print("Welcome", name, " to this adventure")

answer = input ("You are on a dirt road, it has come to an end and you can go left or right. which way you would like to go left or right:  ").lower()

if answer == "left" :                                                          
    answer = input("you come to river, you walk around it or you can swim across? Type walk to walk around and swim to swim across: ")
    
    if answer == "swim": 
        print("You swam across awere eaten by the alligator")
    elif answer == "walk"                                                                                                                                                                                                                                                                                                                                                                                                        :                                                                                               
        print("you walked for many mile,ran out of water and lost")                                          
    else :
        print("not a valid option. you lose.")        
elif answer == "right" :
    answer = input("you come to bridge and it looks wobbly , do you want to cross it or head back(cross/back)?")
    if answer == "back":
        print("you go back and you lose")
    elif answer == "cross" :
        answer = input("You cross a bridge and meet a new stranger do you wanna talk to them or not(yes/no)?")


        if answer == "yes":
            print("you talk to the stranger and they give you gold you win...hurray!")

        elif answer == "no" :
            print("You ignore the stranger they get offended you lose")

        else :
            print("not a valid option. you lose")





else:
    print("not a valid option. you lose.")          

print("thankyou! for trying" ,name)                                                                                                               