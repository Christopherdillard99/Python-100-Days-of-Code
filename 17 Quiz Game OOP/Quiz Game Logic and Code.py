# Day 17: Quiz Game logic and code
# write code for classes in different files within the same folder to ensure that the code is easy to read.


# this game is a true or false game, written using Object Oriented Programming (OOP):
# there needs to be classes for 
# 1. Questions with

#     attributes for text and answer
#     think new_q = Question("2+3=5","True")

class Question:
    def __init__(self, text,answer):
        self.text = text
        self.answer = answer

# ex:
# new_q = Question("What is my name?","Chris")
# print(new_q.text)
# "What is my name?" will be printed in the console.

# --------------------------------------------------------------------------------------------------------

# creating a question bank of question objects by creating a bunch of question object and including it in a list []
# make the list a bunch of dictionaries to make this process simpler [{"letter":"a","number"="one"},{"letter":"b","number"="two"},]
# data is already provided in a data.py file:

question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car,"
             " you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament,"
             " you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

# now import Question class from the question_model and the Data library the data.py data into the main.py file
from question_model import Question
from data import question_data

# create the question bank by looping through the question data:
# 1. Write a for loop to iterate over the question data.question_data.
# 2. Create a Question object from each entry in question_data.question_data.
# 3. Append each Question object to the question_bank. 

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

# now to print the answer for the first question in the newly created question_bank list.
print(question_bank[0].answer)

# --------------------------------------------------------------------------------------------------------

# another file called quiz_brain.py will carry out all the functionalities of the game, like:
# TODO: ask the questions
# TODO: checking if answer was correct
# TODO: checking if the quiz is over

# create a QuizBrain class within this file 
# two attributes: question_number = 0 (default starting at the first question) and questions_list
# one method: next_question()

# the question displays the questions like so:
# of course with inp() so that user can enter either True or False, saved into variable after applying .lower() so that it is not case sensitive.

# Q.1: A slug's blood is green. (True/False)?:

# input(f"Q.{}: {} (True/False)?:")

            # 1. Create a class called QuizBrain
            # 2. Write an __inti__() method
            # 3. Initialize the question_number to 0
            # 4. Initialize the question_list to an input

# start with attributes and assign default values of zero as they apply

question_number = 0
question_list

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        # q_list will be used in main.py file when calling QuizBrain with question_bank as the parameter

    # next method will be used to retrieve the next question
    # retrieve an item at the current question_number from the question_list
    # use the input() function to show the user the Question text and ask for the user's answer.
    def next_question(self):
        '''retrieves the next question and asks for user input for answer guess, current_question will be updated
        as the for loop runs in the main.py file'''
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        #the line above ensure that the printed input statements starts as Q.1 instead of showing as Q.0 to the user.
        #it also makes sure the current question is always moved along to the next question in the list while the for loop is running.
        input(f"Q.{self.question_number}: {current_question.text} (True/False): ").lower()

# now add from quiz_brain import QuizBrain in the main.py file 

# --------------------------------------------------------------------------------------------------------

# now, create a new quiz object to initialize the QuizBrain class passing through the question_bank as the argument

quiz = QuizBrain(question_bank)
quiz.next_question()


# --------------------------------------------------------------------------------------------------------

# now there needs to be a way for the program to continue to the next question after the user's input
# creating a new method for still_has_questions() in the QuizBrain
# then in main.py use a while loop 

# in QuizBrain class add this still_has_question(self) method.
def still_has_questions(self):
    '''return a boolean depending on the value of question_number
    use the While loop to show the next question until the end.'''
    # if self.question_number < len(self.question_list):
    #     return True
    # else:
    #     False
    # the code is simplify to automatically return a boolean of True or False like so:
    return self.question_number < len(self.question_list)


# add this while loop into the main.py file:
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    '''if this condition is True it goes to next question, else it exits the game'''
    quiz.next_question()


# --------------------------------------------------------------------------------------------------------

# now need to check the user's answer against the correct one.
# add one more method to QuizBrain to check_answer()
# also need to set default score to zero as an attribute for QuizBrain

# must modify the next_question() method too in the last line:
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct answer!")
        else:
            print("Wrong answer.")
        print(f"The correct answer was: {correct_answer}.")
        # by placing the print statement outside of the if else block, it will print True or False whether the user got the question right or not.

# Now, everytime a user gets a question right, it should increase their score by one.
# here is where the score is set to default zero as an attribute:
# score is += 1 if user input matches the correct answer and a print statement will show the user "Your current score is:1/1", where the denominator is the current question number.
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

# I modified the check_answer(self, user_answer, correct_answer) method like so:

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct answer!")
            self.score += 1
        else:
            print("Wrong answer.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n") 

# now just ensure that the game ends when all the questions have been answered, printing these two lines in the main.py file:
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

# --------------------------------------------------------------------------------------------------------

# use Open Trivia Database, to ensure that there a nice random questions for each new quiz object game.
# https://opentdb.com/
# now look at their api button at the top right to generate questions by entering the desired category, level of difficulty, choose True or False for answer type to work with this program.
# now enter the url that is generated at the top of the page and you will see a complete dictionary of data in a JSON (JavaScript Object Notation) format
# now replace the question_data with this dictionary.
# it will be difficult to read, so go to code header and select Reformat Code in the drop-down list.
# in this dictionary, there will be two key, value pairs: "response_code":0, "results:[]"
# now, reformat the code again, and it will show that results comprises 10 different dictionaries.

# I chose category to be Science and Nature, difficulty medium, type True or False (Boolean)
# https://opentdb.com/api.php?amount=10&category=17&difficulty=medium&type=boolean
# when reformatted correctly and saved to the question_data list in the data.py file, it looks like this:

question_data = [
    {"type": "boolean",
     "difficulty": "medium",
     "category": "Science &amp; Nature",
     "question": "Like with the Neanderthals, Homo sapiens sapiens also interbred with the Denisovans.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"type": "boolean",
     "difficulty": "medium",
     "category": "Science &amp; Nature",
     "question": "'Tachycardia' or 'Tachyarrhythmia' refers to a resting heart-rate near or over 100 BPM.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"type": "boolean",
     "difficulty": "medium",
     "category": "Science &amp; Nature",
     "question": "A person can get sunburned on a cloudy day.",
     "correct_answer": "True", 
     "incorrect_answers": ["False"]},
    {"type": "boolean",
     "difficulty": "medium",
     "category": "Science &amp; Nature",
     "question": "The Neanderthals were a direct ancestor of modern humans.",
     "correct_answer": "False", 
     "incorrect_answers": ["True"]},
    {"type": "boolean",
     "difficulty": "medium",
     "category": "Science &amp; Nature",
     "question": "Scientists once killed by accident the world's oldest living creature, a mollusc, at 507 years old.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"type": "boolean",
     "difficulty": "medium",
     "category": "Science &amp; Nature",
     "question": "Sugar contains fat.",
     "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"type": "boolean",
     "difficulty": "medium",
     "category": "Science &amp; Nature",
     "question": "In the periodic table, Potassium&#039;s symbol is the letter K.",
     "correct_answer": "True", 
     "incorrect_answers": ["False"]},
    {"type": "boolean",
     "difficulty": "medium",
     "category": "Science &amp; Nature",
     "question": "Anatomy considers the forms of macroscopic structures such as organs and organ systems.",
     "correct_answer": "True", 
     "incorrect_answers": ["False"]},
    {"type": "boolean",
     "difficulty": "medium",
     "category": "Science &amp; Nature",
     "question": "Pneumonoultramicroscopicsilicovolcanoconiosis is a synonym for the disease known as silicosis.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"type": "boolean",
     "difficulty": "medium",
     "category": "Science &amp; Nature",
     "question": "Steel is an alloy of Iron and Carbon.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]}
]

# since I only want the use the Question and the correct answer in this dictionary, I need to now modify the code in the main.py file.
# this is done by changing the name of the keys in the for loop to match the key names of "question" and "correct_answer"
# see the complete Quiz Game code file to see all the final code split in the various files. 


