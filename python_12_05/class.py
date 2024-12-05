# class Car():
#     kinds = []
#     brand = None

#     def __init__(self, name):
#         self.name = name

#     def app_kinds(self, kind):
#         self.kinds.append(kind)

#     def change_brand(self, input_brand):
#         self.brand = input_brand



# k5 = Car("케이파이브")

# k5.change_brand("kia")
# print(k5.brand)

# class Human(object):
#     name = None
#     gender = None
#     age = None

#     def __init__(self, name, gender, age):
#         self.name = name
#         self.gender = gender
#         self.age = age

#     def __str__(self):
#         return f"저는 {self.name}, {self.gender}, {self.age} 입니다."

#     def say_name(self):
#         print(f"제 이름은 {self.name}입니다.")
    
#     def say_gender(self):
#         print(f"제 성별은 {self.gender}입니다.")

#     def say_age(self):
#         print(f"제 나이는 {self.age}입니다.") 




# human1 = Human("이주성", "남", "27")
# human1.say_name()
# human1.say_gender()
# human1.say_age()
# print(human1)



# class Car(object):
#     maxSpeed = 300
#     maxPeople = 5
#     def move(self, x):
#         print(x, '의 스피드로 달리고 있습니다.')
#     def stop(self):
#         print('멈췄습니다.')

# class HybridCar(Car):
#     battery = 1000
#     batteryKM = 300

# class ElectricCar(HybridCar):
#     battery = 2000
#     batteryKM = 600
    
#     def move(self, x):
#         print(self.batteryKM, '만큼 달릴 수 있습니다.')
#         print(x, '스피드로 달리고 있습니다.')


# k5 = HybridCar()
# electricCarK5 = ElectricCar()
# k5.maxSpeed
# electricCarK5.maxSpeed
# electricCarK5.battery
# electricCarK5.move(10)