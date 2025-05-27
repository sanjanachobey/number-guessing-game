print("welcome to my computer quiz")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
 quit()



print("okay lets play")
score = 0
   
    
answer = input("what does CPU stands for?")
if answer.lower() == "central processing unit" :
 print("correct")
 score += 1
else:
 print("incorrect")


answer = input("what does GUI stands for? ")
if answer.lower()== "graphical user interface":
   print("correct")
   score +=1
else:
   print("incorrect")


answer = input("what does RAM stands for?")
if answer== "random access memory":
  print("correct")
  score +=1
else:
  print("incorrect")


answer = input("what does VPN stands for?")
if answer == "virtual private network":
 print("correct")
 score +=1
else:
  print("incorrect")


answer = input("what does rom stands for?")
if answer == "random access memory":
 print("correct")
 score +=1
else:
 print("incorrect")

print("you got"  +  str((score/4)* 100) + "%")



 
 


 



 

 