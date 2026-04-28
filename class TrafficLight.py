class TrafficLight:
    def __init__(self):
        self.color = "red"

    def next(self):
        if self.color == "red":
            self.color = "green"
        elif self.color == "green":
            self.color = "yellow"
        else:  # yellow
            self.color = "red"

    def show(self):
        print(self.color)


# Usage
light = TrafficLight()

light.show()   # red
light.next()
light.show()   # green
light.next()
light.show()   # yellow
light.next()
light.show()   # red