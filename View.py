class View:
    def input_num(self):
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        return num1, num2

    # catalog alchemy
    def show_vehicle_alchemy(self, v):
        if v:
            print("vehicles:")
            for i in v:
                print(f"Vehicle_id: {i.vehicle_id}, vehicle type: {i.vehicle_type}")
        else:
            print("No vehicle found.")

    def show_vehicle(self, v):
        if v:
            print("vehicles:")
            for i in v:
                print(f"Vehicle_id: {i[0]}, vehicle type: {i[1]}")
        else:
            print("No vehicle found.")

    def get_vehicle_input(self):
        vehicle_type = input("Enter vehicle type: ")
        return vehicle_type

    def get_vehicle_id(self):
        vehicle_id = input("Enter vehicle ID: ")
        return vehicle_id

    def show_staff_alchemy(self, s1):
        if s1:
            print("Staff:")
            for s in s1:
                print(f"Staff id: {s.staff_id}, Vehicle id: {s.vehicle_id}, position: {s.position}, name: {s.name}")
        else:
            print("No staff found.")

    def show_staff_(self, s_1):
        if s_1:
            print("Staff:")
            for s in s_1:
                print(f"Staff ID: {s[0]}, position: {s[1]}, name: {s[2]}, vehicle id: {s[3]}")
        else:
            print("No staff found.")

    def get_staff_input(self):
        position = input("Enter position:")
        vehicle_id = input("Enter vehicle ID: ")
        name = input("Enter staff name: ")
        return position,  name, vehicle_id

    def get_staff_id(self):
        staff_id = input("Enter staff ID: ")
        return staff_id

    def show_user_alchemy(self, users):
        if users:
            print("Users:")
            for User in users:
                print(f"ID: {User.user_id}, Phone: {User.phone}, Name: {User.name}, Surname: {User.surname}")
        else:
            print("No users found")

    def show_user(self, users):
        if users:
            print("Users:")
            for User in users:
                print(f"ID: {User[0]}, Phone: {User[1]}, Name: {User[2]}, Surname: {User[3]}")
        else:
            print("No users found")

    def get_user_input(self):
        Phone = input("Enter phone number:")
        Name = input("Enter user Name: ")
        Surname = input("Enter user Surname: ")
        return Phone, Name, Surname

    def get_user_id(self):
        user_id = input("Enter user ID: ")
        return user_id

    def show_booking_alchemy(self, b):
        if b:
            print("Bookings:")
            for i in b:
                print(
                    f"Booking ID: {i.booking_id}, User id: {i.user_id}, Vehicle id: {i.vehicle_id}, price: {i.price}, Booking time: {i.booking_time}")
        else:
            print("No booking found.")

    def show_booking_(self, b):
        if b:
            print("Bookings:")
            for i in b:
                print(
                    f"booking id: {i[0]}, user id: {i[1]}, vehicle id: {i[2]}, price: {i[3]}, booking time: {i[4]}")
        else:
            print("No booking found.")

    def get_booking_input(self):
        vehicle_id = input("Enter vehicle ID: ")
        price = input("Enter price: ")
        user_id = input("Enter user ID: ")
        booking_time = input("Enter booking time: ")
        return user_id, vehicle_id, price, booking_time

    def get_booking_id(self):
        booking_id = input("Enter booking ID: ")
        return booking_id

    def show_message(self, message):
        print(message)