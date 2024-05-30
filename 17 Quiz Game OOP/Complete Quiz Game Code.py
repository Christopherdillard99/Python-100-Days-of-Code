# Quiz Game in OOP: Split into various files:

# Note: the list of dictionaries (question_data) in the data.py file was generated from Open Trivia Database:
# https://opentdb.com/  (see the quiz game logic and code file for more info)
# the unique url for this specific data is:
# https://opentdb.com/api.php?amount=10&category=17&difficulty=medium&type=boolean


#----------------------------------------------------------------------------------

# in the main.py file:

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

#----------------------------------------------------------------------------------

# in the quiz_brain.py file:

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        '''return a boolean depending on the value of question_number
        use the While loop to show the next question until the end.'''
        return self.question_number < len(self.question_list)
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct answer!")
        else:
            print("Wrong answer.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")

#----------------------------------------------------------------------------------

# in the question_model.py file:

class Question:
    def __init__(self, text,answer):
        self.text = text
        self.answer = answer

#----------------------------------------------------------------------------------

# in the data.py file:

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
     "question": "In the periodic table, Potassium's symbol is the letter K.",
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





