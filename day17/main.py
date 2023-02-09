from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# adding each q&a object
for data in question_data:
    question_q = data["question"]
    question_a = data["answer"]
    new_question = Question(question_q, question_a)
    question_bank.append(new_question)

quiz = QuizBrain(questions_list=question_bank)

while quiz.still_has_question():
    quiz.next_question()


print("you've completed the quiz 💀")
print(f"your Final score Was :{quiz.score}/{quiz.question_number}")
