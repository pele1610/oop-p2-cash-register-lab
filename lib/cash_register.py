#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self._discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if not isinstance(value, int):
            print("Not valid discount")
        elif value < 0 or value > 100:
            print("Not valid discount")
        else:
            self._discount = value

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        self.items.append(item)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })


    def apply_discount(self):
        if len(self.previous_transactions) == 0:
            print("There is no discount to apply.")
        else:
            discount_amount = (self.total * self.discount) / 100
            self.total = self.total - discount_amount

    def void_last_transaction(self):
        if len(self.previous_transactions) == 0:
            print("There is no transaction to void.")
        else:
            last = self.previous_transactions[-1]
            self.total -= last["price"] * last["quantity"]
            self.items.remove(last["item"])
            self.previous_transactions.pop()