# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 12:41:57 2022

@author: agfrxa
"""
answers = []
total_answered_questions = 0
with open(r'C:\Users\agfrxa\Python\advent of code 2020\day6\input.txt') as f:
    group_answer = f.readlines()
    for answer in group_answer:
        answers += [answer.rstrip()]
        if answer.rstrip() == '':
            total_answered_questions += len(set(''.join(answers)))
            answers = []
print(total_answered_questions)