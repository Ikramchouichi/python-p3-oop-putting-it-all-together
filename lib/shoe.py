class Shoe:
    def __init__(self, brand, size, color):
        self.brand = brand
        if not isinstance(size, int):
            raise ValueError("size must be an integer")
        self.size = size
        self.color = color
        self.condition = "Old"

    def cobble(self):
        self.condition = "New"
        print("The shoe has been repaired.")

