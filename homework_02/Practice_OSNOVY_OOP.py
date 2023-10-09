# class Fruit:
#     pass
#
#
# a = Fruit()
#
# b = Fruit()
#
# a.name = 'apple'
# b.name = 'orange'
# a.weight = 150
# b.weight = 120
#
#
# print(a.name, b.name, a.weight, b.weight)
#
# class Hello:
#     def hello_world(self):
#         print('Hello world!')
#
#     def greeting(self, name='name'):
#         print(f'Hi , {name}')
#
# greet = Hello()
#
# greet.hello_world()
# greet.greeting('akljsf')
#
#
# class Car:
#     def __init__(self, color):
#         self.e_on = False
#         self.color = color
#
#     def start(self):
#         self.e_on = True
#
#     def drive_to(self, city):
#         if self.e_on:
#             print(f'driving to {city} on {self.color} auto')
#         else:
#             print('car is not running')
#
# c = Car('black')
# c.start()
# c.drive_to("Ufa")

#
# def sum_fun(x,y):
#     return x + y
#
# print(sum_fun(6,56))


class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def get_name(self):
        return self.name

    def get_author(self):
        return self.author


b = Book('peace and war', 'tolstoy')
print(f'book name {b.get_name()} author {b.get_author()}')
print(f'book name {b.name} author {b.author}')