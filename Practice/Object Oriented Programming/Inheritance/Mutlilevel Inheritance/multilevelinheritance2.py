# electronic device
# pocket gadget
# phone

class Electronic_device:
    power = "50000 mh"


class pocket_gadget(Electronic_device):
    appearance = "keypad"

    def feature(self):
        return f"Hi i am an electronic device my feature is {self.appearance}"


class phone(pocket_gadget):
    appearance = "screen touch"

    def feature(self):
        return f"Hi i am electronic device my feature is {self.appearance}"


fridge = Electronic_device()
nokia = pocket_gadget()
samsung = phone()

print(samsung.feature())
print(nokia.feature())
