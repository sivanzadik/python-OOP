class Phone:
    def __init__(self, brand, model, storage_gb):
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.battery = 100
        self.is_on = False

    def power_on(self):
        self.is_on = True
        print("Phone is on")

    def power_off(self):
        self.is_on = False
        print("Phone is off")

    def use_battery(self, amount):
        self.battery = max(0, self.battery - amount)

    def charge(self, amount):
        self.battery = min(100, self.battery + amount)

    def show_status(self):
        status = "On" if self.is_on else "Off"
        print(f"Brand: {self.brand} | Model: {self.model} | Storage: {self.storage_gb}GB | Battery: {self.battery}% | Status: {status}")


# Usage
phone = Phone("Samsung", "S24", 256)
phone.power_on()
phone.use_battery(30)
phone.charge(10)
phone.show_status()