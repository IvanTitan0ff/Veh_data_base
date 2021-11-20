a = 1
colors = ['red','orange','yellow','green','cyan','blue','violet','brown','grey','white','black','purple']
car = ["null"]
car_num_last = 0
car_num_last = 0
car_num = 0
car_name = ("car"+str(car_num))

def car_output(x, y, z, w):
    print( )
    print(x)
    print("Colour is",y)
    print("Doors are",z)
    print("Headlights are",w)

class Car:
    def __init__(self, brand, color, doors, headlights):
        self.color = color
        self.doors = doors
        self.headlights = headlights
        self.brand = brand

while true:
    vvod = str(input())
    if vvod[:8] == 'New car':
        print("Enter car brand:")
        car_brand = str(input())
        car_num_last += 1
        car.append(car_name)
        car[car_num_last] = Car(car_brand ,"not defined", "closed", "off")
        print('Car №',car_num_last,'is created.')
    elif vvod[:9] == 'Edit car':
        print('Choose car number:')
        car_num = int(input())
        if  car_num <= len(car)-1:
            car_output(car[car_num].brand, car[car_num].color, car[car_num].doors, car[car_num].headlights)
            edit = str(input())
            while edit != "Stop edit":
                if edit[:11] == "Set colour":
                    print("Enter colour: ")
                    car_colour = str(input())
                    if car_colour in colors:
                        car[car_num].color = car_colour
                        print("Colour is changed to",car[car_num].color)
                    else:
                        print("This colour is not avaliable!")
                elif edit[:18] == "Switch headlights":
                    if car[car_num].headlights == "off":
                        car[car_num].headlights = "on"
                    else:
                        car[car_num].headlights = "off"
                    print("Headlights are",car[car_num].headlights)
                elif edit[:13] == "Switch doors":
                    if car[car_num].doors == "closed":
                        car[car_num].doors = "open"
                    else:
                        car[car_num].doors = "closed"
                    print("Doors are",car[car_num].doors)
                elif edit[:11] == "Car profile":
                    car_output(car[car_num].brand, car[car_num].color, car[car_num].doors, car[car_num].headlights)
                else:
                    print("Incorrect input!")
                edit = str(input())
        else:
            print("No car with such a number!")
    elif vvod[:11] == 'Delete car':
        print('Choose car number:')
        car_num = int(input())
        if  car_num <= len(car)-1:
            del car[car_num]
            print('Car №',car_num,"was deleted.")
        else:
            print("No car with such a number!")
    else:
        print("Incorrect input!")
