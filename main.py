from store import *

target = Store("Target")

ball = Product("Bouncy Ball", 0.99, "Toy",1111)
action_figure = Product("Action Figure", 2.99, "Toy",2222)
laptop = Product("Laptop", 349.99, "Computer",3333)
race_car = Product("Race Car", 1.99, "Toy",4444)
table = Product("Table", 49.99, "Furniture",5555)

target.add_product(ball).add_product(action_figure).add_product(laptop).add_product(race_car).add_product(table)
target.set_clearance("Toy", .25).inflation(.10).sell_product(2222)

for product in target.product_list:
    product.print_info()