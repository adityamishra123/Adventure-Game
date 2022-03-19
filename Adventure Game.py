name=str(input("enter your name: "))
print(f"{name} you are stuck at work")
print("you are still working and suddenly you saw a ghost,now you have two options")
print("1.Run. 2.Jump from the window")
user=int(input("choose 1 or 2: "))
if user==1:
    print("you did it")
elif user==2:
    print("you are not that smart")
else:
    print("please check your input")