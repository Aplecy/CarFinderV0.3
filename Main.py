import os

#File to store the authorized vehicles
SAVE_FILE = "AUTHLIST.txt"

#Load vehicles from a txt file or use default list
def load_vehicles():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    else:
        return [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]

#Save vehicles to the txt file
def save_vehicles():
    with open(SAVE_FILE, "w") as f:
        for vehicle in AllowedVehiclesList:
            f.write(vehicle + "\n")

AllowedVehiclesList = load_vehicles()
#create a defined option to call for the list then returns to menu
def Printlist():
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicles in AllowedVehiclesList:
        print (vehicles)
    print("")
    menu()

#create a defined option to exit the menu
def Exit():
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")

#create a search option for authorized vehicles
def Search():
    SEARCHvech = input("Please Enter the full Vehicle name: ")
    if SEARCHvech in AllowedVehiclesList:
        print(f"{SEARCHvech} is an authorized vehicle")
        menu()
    else:
        print(f"{SEARCHvech} is not an authorized vehicle, if you received this error please check the spelling and try again.")
        menu()

#create a option to add authorized vehicles
def AddNewCar():
    new_vehicle = input("Please Enter the full Vehicle name you would like to add:")
    AllowedVehiclesList.append(new_vehicle)
    save_vehicles()
    print(f"You have added \"{new_vehicle}\" as an authorized vehicle.")
    menu()
#create a defined menu for AutoCountry with options to show authorized vehicles and option to exit
def menu():
    print("********************************")
    print("AutoCountry Vehicle Finder V.03")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicles")
    print("3. ADD Authorized Vehicle")
    print("4. Exit")
    print("********************************")
    option = int(input(""))
    if option == 1:
        Printlist()
    elif option == 2:
        Search()
    elif option == 3:
        AddNewCar()
    elif option == 4:
        Exit()    

menu()