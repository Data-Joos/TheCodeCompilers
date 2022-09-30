class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
    

print("Welcome to this quiz about Python!")
name = input("Please enter your name: ")

question_prompts = [
    "What level of programming is python considerd as? \n(a) Low-level \n(b) Fullstack \n(c) High-level\n\n",
    "Is python considered to be a compiled or an interperated language? \n(a) Compiled \n(b) Interperated \n(c) Both\n\n",
    "Does indentation matter in python syntax? \n(a) Yes, it does \n(b) No, it doesn't \n(c) Only when creating a variable\n\n",
    "What does garbage collection has to do with python? \n(a) It involves clearing data memory. \n(b) It'll empty the desktop trash can automatically. \n(c) It's a built in function for debugging code.\n\n",
    "Wich alternative is correct? \nx = 3 \nif x < 5: \n\tprint('Math is awesome!') \nelse: \n\tprint('Math sucks.') \t\n(a) x < 5 \n(b) Math sucks. \n(c) Math is awesome!\n\n",
    "var_1 = 'cat' \nvar_2 = 'bird' \nprint(var_1 + var_2) \t\nWhat answer should we get? \n(a) cat bird \n(b) catbird \n(c) cat + bird\n\n",
    "Wich of the following is a common datatype in python? \n(a) A leaflet \n(b) A boolean \n(c) A snoarlax\n\n",
    "var_1 = 13\nvar_2 = 8\nsum = var_1 + var_2\nprint (sum)\t\nWhat answer will we get?\n(a) 13 + 8 \n(b) 138 \n(c) 21\n\n",
    "Wich of the following is not a built-in data type for storing collections of data in python?\n(a) Array \n(b) Tuple \n(c) Dictionary\n\n",
    "What is the __init__() function used for? \n(a) It creates a function in itself. \n(b) Assigning values to object properties or operations. \n(c) It initiates the execution of a block of code.\n\n"
    ]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "c"),
    Question(question_prompts[5], "b"),
    Question(question_prompts[6], "b"),
    Question(question_prompts[7], "c"),
    Question(question_prompts[8], "a"),
    Question(question_prompts[9], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct!")
    if score >= 7:
        print("You did great, awesome!")
    elif score >= 4:
        print("You did okay.")
    else:
        print("That's not very good, there's deffinitly room for improvement...")

run_test(questions)