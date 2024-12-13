"""

Lista - []
Set -   {}
Dict -


"""

# listas (arrays)


fast_food_items = [
    "Hambúrguer Clássico",
    "Cheeseburger",
    "Hambúrguer de Bacon",
    "Double Cheeseburger",
    "Chicken Burger",
    "Veggie Burger",
    "Pizza Pepperoni",
    "Pizza Margherita",
    "Pizza de Frango com Catupiry",
    "Hot Dog Clássico",
    "Hot Dog com Chili",
    "Sanduíche de Frango Crocante",
    "Wrap de Frango",
    "Taco de Carne",
    "Taco Vegetariano",
    "Batatas Fritas",
    "Nuggets de Frango",
    "Anéis de Cebola",
    "Milkshake de Chocolate",
    "Milkshake de Morango",
    "Batata Recheada com Queijo",
    "Quesadilla de Frango",
    "Sundae de Chocolate",
    "Açaí com Granola",
    "Churros com Doce de Leite"
]

print(fast_food_items[0])

print(fast_food_items[0:5])
print(fast_food_items[0:10: 5])

print(fast_food_items[:5])

print(fast_food_items[::-1]) # print(fast_food_items[n:m:s]) n ate m-1 com step de s


print(fast_food_items[10:5:-1])



for item in fast_food_items:
    print(item)


print("---" * 5)

lista1 = [1, 2, 3]
print(lista1)
lista1.append(4)
print(lista1)

lista1.insert(1, 99)
lista1.insert(3, 99)
print(lista1)

lista1.remove(99) # apagar um valor

print(lista1)

lista1.pop()
print(lista1)


lista1.pop(1) # apagar por pos
print(lista1)

lista1.append(1)
lista1.append(1)
lista1.append(1)

print(lista1.count(1))



print(lista1.__len__())
print(len(lista1))
print("---" * 4)

for item in enumerate(lista1):
    print(item)


print("---" * 4)
print(lista1.index(1, 1))
print("---" * 4)
#lista1.remove(21223)


# set (conjunto)

mySet = {"Val1", "Val2", "Val4", "Val3"}


print(mySet.__contains__("Val3"))

mySet2 = {"Val5", "Val6", "Val4", "Val7"}

print("---" * 5)

print(mySet)

mySet.add("Val5")
print(mySet)

mySet.add("Val5")
print(mySet)
print("---" * 5)
print(mySet.union(mySet2))
print(mySet2.union(mySet))
print("---" * 5)
print(mySet.difference(mySet2))
print(mySet2.difference(mySet))
print("---" * 5)

print(mySet.symmetric_difference(mySet2))
print(mySet2.symmetric_difference(mySet))
print("---" * 5)

print(mySet.intersection(mySet2))

print(mySet.intersection_update(mySet2))



mySet2 = {"Val5", "Val6", "Val4", "Val7"}

mySet3 = {"Val5", "Val6", "Val1"}

mySet = {"Val1", "Val2", "Val4", "Val3"}


print(mySet3.issubset(mySet2.union(mySet)))

# Dict (hash map)  par key : val



my_dict = {"key1": "Value1",
           "key2": "Value2",
           "key3": "Value3"}

print(my_dict["key2"])

my_dict["key4"] = "Value4"

print(my_dict)

my_dict["key1"] = "Novo Valor"

print(my_dict)

my_dict.pop("key2")
print(my_dict)


my_dict.popitem()
print(my_dict)

print("---" * 5)
print(my_dict.keys())
print(my_dict.values())



print("---" * 5)
for elm in my_dict:
    print(elm)

# eqivalente a
print("---" * 5)
for elm in my_dict.keys():
    print(elm)


print("---" * 5)
for elm in my_dict.values():
    print(elm)



print("---" * 5)
for elm in my_dict.items():
    print(elm)

# funcs