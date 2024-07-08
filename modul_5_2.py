class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if self.number_of_floors < new_floor or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)


    def __len__(self):
        return self.number_of_floors


    def __str__(self):
        col_floor = str(self.number_of_floors)
        #print (col_floor)

        return "Название: " f'{self.name}'' , ' 'Количество этажей: '  f'{self.number_of_floors}'


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
#print (col_floor)
# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))