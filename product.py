class Product:
    def __init__(self, name, price, category, id):
        self.name = name
        self.price = price
        self.category = category
        self.id = id
    def update_price(self,percent_change,is_increased):
        if is_increased:
            self.price += self.price * percent_change
        else:
            self.price -= self.price * percent_change
        return self
    def print_info(self):
        print(f"Name: {self.name}, Price: {self.price}, Category: {self.category}")
        return self

# pab = Product("pablo", 100, "humans")
# pab.print_info().update_price(.05, True).print_info().update_price(.10, False).print_info()