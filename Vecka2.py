right_answer = 0
wrong_answer = 0
answer = 0


print("Welcome to the Python Quiz!")
print("We will ask you 10 questions and in the end you will get a result")

print("""1. When was Python first released?
A: 1981
B: 1991
C: 1989""" )
answer = input()

if answer == "A":
    right_answer+=1
else:
    wrong_answer+=1

print("""2. Who is the founder of Python?
A: Guido van Rossum
B: James Gosling
C: Anders Hejlsberg""")
answer = input()

if answer == "A":
    right_answer+=1
else:
    wrong_answer+=1

print("""3. What level is Python defined as?
A: Low-level
B: Mid-level
C: High-level""")
answer = input()

if answer == "C":
    right_answer+=1
else:
    wrong_answer+=1

print("""4. How do you write if you want to print a text string in Python?
A: System.out.print():
B: Console.Write
C: print("")""")
answer = input()

if answer == "C":
    right_answer+=1
else:
    wrong_answer+=1

print("""5. Which sympol/sympols do you write when commenting in Python?
A: //
B: //*
C: #""") 
answer = input()

if answer == "C":
    right_answer+=1
else:
    wrong_answer+=1

print("""6. What is a correct syntax to output "Hello World" in Python?
A: p("Hello World")
B: echo("Hello WOrld");
C: print("Hello World")""")
answer = input()

if answer == "C":
    right_answer+=1
else:
    wrong_answer+=1

print("""7. What is the correct file extension for Python files?
A: .pyth
B: .py
C: .pyt""")
answer = input()

if answer == "B":
    right_answer+=1
else:
    wrong_answer+=1

print("""8. In Python, 'Hello' is the same as "Hello"
A: False
B: True
C: Depends on how you write the code""")
answer = input()

if answer == "B":
    right_answer+=1
else:
    wrong_answer+=1

print("""9. Which operator can be used to compare two values?
A: =
B: ==
C: ><""")
answer = input()

if answer == "B":
    right_answer+=1
else:
    wrong_answer+=1

print("""10. Which statement is used to stop a loop?
A: stop
B: break
C: exit""")
answer = input()

if answer == "B":
    right_answer+=1
else:
    wrong_answer+=1

print("Congratulations you have finished the quiz!")
print(f"Your result is {right_answer} right answer and {wrong_answer} wrong answer")
