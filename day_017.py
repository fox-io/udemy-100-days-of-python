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
                    self.list[index] = {
                            "question": entry["question"],
                            "answer": entry["correct_answer"],
                    }
                    index += 1
        except error.URLError as e:
            print(e.reason)


def main():
    questions = QuestionList()
    print(questions.list[0]["question"])
    guess = input("true or false? ")
    if guess == questions.list[0]["answer"]:
        print("Correct!")
    else:
        print("Wrong!")
    pass


if __name__ == "__main__":
    main()
