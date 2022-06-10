import os

def which_chars_in_all_strs(list_of_strings):
    chars = ''
    for char in list_of_strings[0]:
        verdict = True
        for string in list_of_strings[1:]:
            if char not in string:
                verdict = False
        if verdict:
            chars += char

    return chars

answers = []
total_answered_questions = 0
with open(os.path.join(os.getcwd(), 'input.txt')) as f:
    group_answer = f.readlines()
    for answer in group_answer:
        answers += [answer.rstrip()]
        if answer.rstrip() == '':
            chars_in_common = which_chars_in_all_strs(answers[:-1])
            total_answered_questions += len(chars_in_common)
            answers = []
print(total_answered_questions)


