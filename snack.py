from menu_item import MenuItem

class Snack(MenuItem):
    def __init__(self, name, price, caloriesnack_count):
        super().__init__(name, price)
        self.caloriesnack_count = caloriesnack_count
    
    def info(self):
        return self.name + ': ' + str(self.price) + 'k  (' + str(self.caloriesnack_count) + 'kkal)'
    
    def calorie_info(self):
        print('kkal: ' + str(self.calorie_count))
