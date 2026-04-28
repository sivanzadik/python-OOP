class Bag:
    def __init__(self, owner, color):
        self.owner = owner
        self.color = color
        self.items = []  # empty list

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"{item} not found in bag")

    def show_contents(self):
        if self.items:
            print(f"{self.owner}'s {self.color} bag contains: {', '.join(self.items)}")
        else:
            print(f"{self.owner}'s {self.color} bag is empty")


# Usage
bag = Bag("Sara", "red")
bag.add_item("book")
bag.add_item("water bottle")
bag.remove_item("keys")  # not found
bag.show_contents()