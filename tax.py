import json


def tax(amount, filename='default_brackets.json'):
    total_tax = 0
    amount_to_tax = amount
    file = open(filename)
    brackets = json.load(file)
    file.close()
    previous_cap = 0
    for b in brackets:
        if b['cap'] and amount_to_tax > b['cap']:
            current_bracket = b['cap'] - previous_cap
            total_tax += current_bracket * b['rate']
            amount_to_tax -= current_bracket
            previous_cap = b['cap']
        else:
            total_tax += amount_to_tax * b['rate']
            break
    return int(total_tax)
