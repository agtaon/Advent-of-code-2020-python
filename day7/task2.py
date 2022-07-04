import os

bag_dict = {}
outcome_dict = {}
tot_bags = 0


def line_parser(line):
    words = line.split()
    bag = "_".join(words[0:2])
    bag_dict[bag] = []
    if "no other bags" in line:
        return

    for i, word_num in enumerate(words):
        if word_num in "0123456789":
            inner_bag = "_".join(words[i : i + 3])
            bag_dict[bag] += [inner_bag]


def bag_tree(bag, mother_bags, tot_bags=0):
    contents = bag_dict[bag]
    for value in contents:
        tot_bags += int(value[0]) * mother_bags
        temp_mother_bags = mother_bags * int(value[0])
        tot_bags = bag_tree(value[2:], temp_mother_bags, tot_bags)
    return tot_bags


with open(os.path.join(os.getcwd(), "input.txt")) as f:
    rules = f.readlines()
    for rule in rules:
        line_parser(rule)

tot_bags = bag_tree("shiny_gold", 1)
print(tot_bags)
