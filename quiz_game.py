print("Welcome to my computer quiz!")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

print("okay! Let's play :)")

score = 0

answer1 = input("what does cpu stand for? ")
if answer1.upper() == "CENTRAL PROCESSING UNIT":
    print('correct')
    score = score + 1
else:
    print('incorrect')
    score = score - 1

answer2 = input("what does tcp stand for? ")
if answer2.upper() == "TRANSPORT CONTROL PROTOCOL":
    print('correct')
    score = score + 1
else:
    print('incorrect')
    score = score - 1

answer3 = input("what does ip stand for? ")
if answer3.upper() == "INTERNET PROTOCOL":
    print('correct')
    score = score + 1
else:
    print('incorrect')
    score = score - 1

print(f"your final score is {score},", end="")
print(' you passed' if score > 1 else 'you failed')