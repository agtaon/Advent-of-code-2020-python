# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 13:53:51 2022

@author: agfrxa
"""
import os
import sys

answers = []
total_answered_questions = 0
with open(os.path.join(os.getcwd(), 'input.txt')) as f:
    group_answer = f.readlines()
    for answer in group_answer:
        answers += [answer.rstrip()]
        if answer.rstrip() == '':
            total_answered_questions += len(set(''.join(answers)))
            print(answers)
            answers = []
            break
print(total_answered_questions)


