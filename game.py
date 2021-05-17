import random
print("Welcome to Snake, Water and Gun game!")
play=["s","w","g"]
i=0
player=0
comp=0
while(True):
    person=input("Enter your choice:\nType 's' for Snake, 'w' for Water and 'g' for Gun:\n")
    computer=random.choice(play)
    if person=="s" and computer=="w":
      print(f"Player:{person}\tcomputer:{computer}\nYou won the strike.\n")
      player+=1
    elif person=="w" and computer=="g":
      print(f"Player:{person}\tcomputer:{computer}\nYou won the strike.\n")
      player+=1
    elif person=="g" and computer=="s":
      print(f"Player:{person}\tcomputer:{computer}\nYou won the strike.\n")
      player+=1
    elif person=="w" and computer=="s":
      print(f"Player:{person}\tcomputer:{computer}\nYou loose the strike.\n")
      comp+=1
    elif person=="g" and computer=="w":
      print(f"Player:{person}\tcomputer:{computer}\nYou loose the strike.\n")
      comp+=1
    elif person=="s" and computer=="g":
      print(f"Player:{person}\tcomputer:{computer}\nYou loose the strike.\n")
      comp+=1
    elif person==computer:
         print(f"player:{person}\tcomputer:{computer}\nIts a Draw\n")
    if i==3:
        break
    i=i+1
if player==comp and i==10:
    print(f"Match is  Draw\nplayer:{player}\tcomputer:{comp}")
elif player<comp:
    print(f"Computer won the match:\nplayer:{player}\tcomputer:{comp}")
else:
    print(f"You won the match:\nplayer:{player}\tcomputer:{comp}")
