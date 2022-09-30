print("Hi and welcome to the quiz of Code Compilers. Good luck!")
player_name = input("Input your name: ")
player_score = 0

print('Q 1: What does the following line of code print?\nprint("Rabbit")\na: Hello\nb: Rabbit\nc: Error ')
Answer1 = input("Answer: ")
if Answer1 == "b":
    player_score += 1

print('Q 2: What does the following lines of code print?\nx = 5\ny = 10\nprint(x + y)\na: 15\nb: x + y\nc: Rabbit')
Answer2 = input("Answer: ")
if Answer2 == "a":
    player_score += 1

print("Q 3: What does the following line of code print?\nprint(type(10))\na: <class 'int'>\nb: <class 'float'>\nc: <class 'str'>")
Answer3 = input("Answer: ")
if Answer3 == "a":
    player_score += 1

print('Q 4: What does the following syntax mean? def x()\na: Start a for-loop\nb: Execute division\nc: Defines a function')
Answer4 = input("Answer: ")
if Answer4 == "c":
    player_score += 1

print('Q 5: What does the following lines of code print?\nx = 5\ny = "10"\nprint(x + y)\na: 15\nb: x + y\nc: Error')
Answer5 = input("Answer: ")
if Answer5 == "c":
    player_score += 1

print('Q 6: What is a boolean in Python?\na: Data type which represents the values True or False\nb: A string of text\nc: An integer')
Answer6 = input("Answer: ")
if Answer6 == "a":
    player_score += 1

print('Q 7: What does the following lines of code print?\nx = 0\nprint(x += 1)\na: 0\nb: 1\nc: 2')
Answer7 = input("Answer: ")
if Answer7 == "b":
    player_score += 1

print('Q 8: How does one print out comments in Python?\na: # before text\nb: # after text\nc: not possible')
Answer8 = input("Answer: ")
if Answer8 == "a":
    player_score += 1

print('Q 9: What does the following lines of code print?\nx = 5\ny = "I am "\nprint(y + x)\na: Error\nb: I am 5\nc: x + y')
Answer9 = input("Answer: ")
if Answer9 == "a":
    player_score += 1

print('Q 10: What does the following lines of code print?\nx = 5\ny = "I am "\nprint(y, x)\na: Error\nb: I am 5\nc: x + y')
Answer10 = input("Answer: ")
if Answer10 == "b":
    player_score += 1

if player_score >= 8:
    print("Wow!", player_name,"you got", player_score, "out of 10 and the grade VG")
elif player_score < 8 and player_score >= 4:
    print("Great!", player_name,"you got", player_score, "out of 10 and the grade G")
else:
    print("Too bad!", player_name, "you got", player_score, "out of 10 and the grade IG. You should get your sh* together and probably cancel your plans for the weekend :(")