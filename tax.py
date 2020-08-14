import json


class Tax:
    def __init__(self, filename='default_brackets.json'):
        file = open(filename)
        self.brackets = json.load(file)
        file.close()

    def tax(self, amount):
        """Return tax based on amount of money earned."""
        total_tax = 0
        amount_to_tax = amount
        previous_cap = 0
        for b in self.brackets:
            if b['cap'] and amount > b['cap']:
                current_bracket = b['cap'] - previous_cap
                total_tax += current_bracket * b['rate']
                amount_to_tax -= current_bracket
                previous_cap = b['cap']
            else:
                total_tax += amount_to_tax * b['rate']
                break
        return int(total_tax)

    def overall_rate(self, rate):
        """Return amount of money needed to get overall tax on given level"""
        if rate >= self.brackets[-1]['rate']:
            return None  # No amount can give pure maximum rate or more than it
        amount = 1
        while self.tax(amount) / amount < rate:
            amount += 1
        return amount
