import json


class Tax():
    def __init__(self, filename='default_brackets.json'):
        file = open(filename)
        self.brackets = json.load(file)
        file.close()

    def tax(self, amount):
        total_tax = 0
        amount_to_tax = amount
        previous_cap = 0
        for b in self.brackets:
            if b['cap'] and amount_to_tax > b['cap']:
                current_bracket = b['cap'] - previous_cap
                total_tax += current_bracket * b['rate']
                amount_to_tax -= current_bracket
                previous_cap = b['cap']
            else:
                total_tax += amount_to_tax * b['rate']
                break
        return int(total_tax)
