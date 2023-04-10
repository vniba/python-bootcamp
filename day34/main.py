from day34.ui import QuizGui
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import html

question_bank = []
for question in question_data:
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizGui(quiz)
