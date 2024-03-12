# Pair of gloves
# Winter is coming, you must prepare your ski holidays. The objective of this kata is to determine the number of pair of gloves you can constitute from the gloves you have in your drawer.

# Given an array describing the color of each glove, return the number of pairs you can constitute, assuming that only gloves of the same color can form pairs.

# Examples:
# input = ["red", "green", "red", "blue", "blue"]
# result = 2 (1 red pair + 1 blue pair)

# input = ["red", "red", "red", "red", "red", "red"]
# result = 3 (3 red pairs)


def solution(gloves):
    output = 0
    while gloves:
        if gloves.count(gloves[0]) > 1:
            output += 1
            pair = gloves[0]
            gloves.remove(pair)
            gloves.remove(pair)
        else:
            single = gloves[0]
            gloves.remove(single)
    return output

