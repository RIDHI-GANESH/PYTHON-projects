print("Welcome to my computer quiz!")

playing = input("Do you want to play? ").strip().lower()

if playing != "yes":
    quit()

print("Okay! Let's play :)")
score = 0
# CPU
answer = input("What does CPU stand for? ").strip().lower()

if answer == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

# RAM
answer = input("What does RAM stand for? ").strip().lower()

if answer == "random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

# GPU
answer = input("What does GPU stand for? ").strip().lower()

if answer == "graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

# PSU
answer = input("What does PSU stand for? ").strip().lower()

if answer == "power supply unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print("you got "+ str(score) + " questions correct!!")
print("you got "+ str((score/4)*100) + "%")