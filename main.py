

def process_orders(data_input: str) -> str:
    if not data_input:
        raise ValueError("Empty input or insufficient")

    data_input = data_input.split('\n')
    if len(data_input) < 2:
        raise ValueError("Empty input or insufficient")

    data_input = [row.split(',') for row in data_input]

    restaurant = Restaurant(data_input.pop(0))
    output = restaurant.process_orders(data_input)
    return output


class Restaurant:
    ingredient_type = ['P', 'L', 'T', 'V', 'B']

    def __init__(self, restaurant_row):
        # R1,4C,1,3A,2,2P,1,100,200,200,100,100
        self.id = restaurant_row[0]
        self.cookers = restaurant_row[1]
        self.cookers_time = restaurant_row[2]
        self.assembler = restaurant_row[3]
        self.assembler_time = restaurant_row[4]
        self.packager = restaurant_row[5]
        self.packager_time = restaurant_row[6]
        self.P = int(restaurant_row[7])
        self.L = int(restaurant_row[8])
        self.T = int(restaurant_row[9])
        self.V = int(restaurant_row[10])
        self.B = int(restaurant_row[11])

        self.orders = []


    def ingredient_availability(self, ingredients_str):
        for ingredient in self.ingredient_type:
            if getattr(self, ingredient) < ingredients_str.count(ingredient):
                return False
        return True

    def take_ingredients(self, ingredients_str):
        for ingredient in self.ingredient_type:
            setattr(self, ingredient, getattr(self, ingredient) - ingredients_str.count(ingredient))

    def process_orders(self, order_list):
        for order in order_list:
            # R1,2020-12-08 19:15:31,O1,BLT,LT,VLT
            ingredients_str = ','.join(order[3:]) + 'P' * (len(order) - 3)  # Add patties
            if self.ingredient_availability(ingredients_str):
                self.take_ingredients(ingredients_str)
            else:
                print('REJECT')

        # Inventory
        inventory_str = f'R1,INVENTORY'
        for ingredient in self.ingredient_type:
            inventory_str += f',{getattr(self, ingredient)}'
        return inventory_str
