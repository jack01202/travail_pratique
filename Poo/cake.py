class Cake :
    def __init__(self,flavor):
        self.flavor = flavor

    def cut_in_part(self):
        print("le gateau est coupe en 4 parts")

cake = Cake("chocolate")
print(cake.flavor)
cake.cut_in_part() 