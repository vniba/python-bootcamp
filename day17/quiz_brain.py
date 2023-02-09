class QuizBrain:
    def __init__(self, questions_list):
        self.question_list = questions_list
        self.question_number = 0
        self.score = 0

    def still_has_question(self):
        return self.question_number < self.question_list.__len__()

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_choice = input(
            f"Q.{self.question_number}: {current_q.question}. (True/False)?. "
        ).lower()
        self.check_answer(user_choice, current_q.answer)

    def check_answer(self, user_choice, current_answer):
        if user_choice.lower() == current_answer.lower():
            self.score += 1
            print("You got it right !")
        else:
            print("That not right")
        print(f"The correct answer was: ${current_answer}")
        print(f"your current score is {self.score}/{self.question_number}")
        print("\n")
