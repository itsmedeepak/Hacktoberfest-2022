class QuizBrain:

    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_q = self.question_list[self.question_no]
        self.question_no += 1
        usr_answer = input(f"0.{self.question_no} {current_q.text} (True/False)?")
        self.check_answer(usr_answer, current_q.answer)

    def check_answer(self, usr_answer, correct_answer):
        if usr_answer == correct_answer:
            print("you got it right")
            self.score += 1
        else:
            print("that's wrong")
            print(f"The correct answer is {correct_answer}.")
        print(f"Your current score is : {self.score}/{self.question_no}\n")