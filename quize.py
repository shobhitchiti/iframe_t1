print("Welcome to my computer quize")
playing = input("Do you want to play ? ")

if (playing.lower() != 'yes'):
    quit()

print("okay ! let's play :)")
score = 0
answer = input("full form of CPU ? ")
if answer.lower() == "central processing unit":
    print("correct :)")
    score += 1
else:
    print("wrong")

answer = input("full form of PU ? ")
if answer.lower() == "processing unit":
    print("correct :)")
    score += 1
else:
    print("wrong")

print('Score = ' + str(score))