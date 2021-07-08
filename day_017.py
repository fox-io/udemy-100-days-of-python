"""
-----
Day 17 Project: Trivia
-----

Trivia API https://opentdb.com/api.php?amount=4&type=boolean

(c)2021 John Mann <gitlab.fox-io@foxdata.io>
"""
from urllib import request, error
import json


class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


class QuestionList:
    list = {}

    def __init__(self):
        try:
            with request.urlopen('https://opentdb.com/api.php?amount=4&type=boolean') as f:
                data = json.load(f)
                index = 0
                for entry in data["results"]:
                    self.list[index] = Question(entry["question"], entry["correct_answer"])
                    index += 1
        except error.URLError as e:
            print(e.reason)

    def ask(self, num):
        print(f"[Q {num + 1}/4] {self.list[num].question}")
        guess = input("true or false? ").lower()
        if guess == self.list[num].answer.lower():
            print("That's correct!")
            return 1
        else:
            print("Wrong answer!")
            return 0


def main():
    score = 0
    questions = QuestionList()
    for question_round in range(0, 4):
        score += questions.ask(question_round)
    print(f"Final score: {score}/4")


if __name__ == "__main__":
    main()
