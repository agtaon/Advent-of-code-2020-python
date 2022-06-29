import os

bag_dict = {}
outcome_dict = {}


def line_parser(line):
    words = line.split()
    bag = "_".join(words[0:2])
    bag_dict[bag] = []
    if "no other bags" in line:
        return

    for i, word_num in enumerate(words):
        if word_num in '0123456789':
            inner_bag = "_".join(words[i+1:i+3])
            bag_dict[bag] += [inner_bag]


def dict_parser(key):
    values = bag_dict[key]

    if "shiny_gold" in values:
        outcome_dict[key] = "Yes"
        return "Yes"

    for value in values:
        response = dict_parser(value)
        if response == "Yes":
            return response

    return "No"


with open(os.path.join(os.getcwd(), "input.txt")) as f:
    rules = f.readlines()
    for rule in rules:
        line_parser(rule)

for key in bag_dict.keys():
    response = dict_parser(key)
    outcome_dict[key] = response

counter = 0
for value in outcome_dict.values():
    if value == "Yes":
        counter += 1

print(counter)
