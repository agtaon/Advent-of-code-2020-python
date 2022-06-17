import os

answers = []
total_answered_questions = 0
with open(os.path.join(os.getcwd(), "input.txt")) as f:
    group_answer = f.readlines()
    for answer in group_answer:
        answers += [answer.rstrip()]
        if answer.rstrip() == "":
            total_answered_questions += len(set("".join(answers)))
            answers = []
print(total_answered_questions)
