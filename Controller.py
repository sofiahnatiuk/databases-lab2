from Model import Model
from View import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        while True:
            category = self.show_menu()
            if category == '1':
                self.run_add()
            elif category == '2':
                self.run_view()
            elif category == '3':
                self.run_update()
            elif category == '4':
                self.run_delete()
            elif category == '5':
                self.gener_user()
            elif category == '6':
                break

    def show_menu(self):
        self.view.show_message("\nMenu:")
        self.view.show_message("1. Add")
        self.view.show_message("2. View")
        self.view.show_message("3. Update")
        self.view.show_message("4. Delete")
        self.view.show_message("5. Generate new users")
        self.view.show_message("6. Quit")
        return input("Enter your choice: ")


    def menu(self):
        self.view.show_message("1. Vehicle")
        self.view.show_message("2. Staff")
        self.view.show_message("3. Booking")
        self.view.show_message("4. User")
        self.view.show_message("5. Quit")
        return input("Enter your choice: ")

    def run_view(self):
        print("\nView:")
        while True:
            category2 = self.menu()
            if category2 == '1':
                self.view_vehicle_al()
            elif category2 == '2':
                self.view_staff_al()
            elif category2 == '3':
                self.view_booking_al()
            elif category2 == '4':
                self.view_user_al()
            elif category2 == '5':
                break

    def run_add(self):
        self.view.show_message("\nAdd:")
        while True:
            category1 = self.menu()
            if category1 == '1':
                self.add_vehicle()
            elif category1 == '2':
                self.add_staff()
            elif category1 == '3':
                self.add_booking()
            elif category1 == '4':
                self.add_user()
            elif category1 == '5':
                break

    def run_update(self):
        self.view.show_message("\nUpdate:")
        while True:
            category3 = self.menu()
            if category3 == '1':
                self.update_vehicle()
            elif category3 == '2':
                self.update_staff()
            elif category3 == '3':
                self.update_booking()
            elif category3 == '4':
                self.update_user()
            elif category3 == '5':
                break

    def run_delete(self):
        self.view.show_message("\nDelete:")
        while True:
            category4 = self.menu()
            if category4 == '1':
                self.delete_vehicle()
            elif category4 == '2':
                self.delete_staff()
            elif category4 == '3':
                self.delete_booking()
            elif category4 == '4':
                self.delete_user()
            elif category4 == '5':
                break

    def gener_user(self):
        num1, num2 = self.view.input_num()
        self.model.gener_add_user(num1, num2)
        print("Added users successfully!")

    def add_vehicle(self):
        vehicle_type = self.view.get_vehicle_input()
        vehicle_id = self.view.get_vehicle_id()
        if vehicle_id.isdigit():
            self.model.add_vehicle(vehicle_id, vehicle_type)
        else:
            print("Error! Wrong input")

    def update_vehicle(self):
        vehicle_id = self.view.get_vehicle_id()
        vehicle_type = self.view.get_vehicle_input()
        if vehicle_id.isdigit():
            self.model.update_vehicle(vehicle_id,vehicle_type)
        else:
            print("Error! Wrong input")


    def view_vehicle_al(self):
        v = self.model.get_all_vehicle()
        self.view.show_vehicle_alchemy(v)

    def delete_vehicle(self):
        vehicle_id = self.view.get_vehicle_id()
        if vehicle_id.isdigit():
            self.model.delete_vehicle(vehicle_id)
        else:
            print("Error! Wrong input")

    def add_staff(self):
        position, name, vehicle_id = self.view.get_staff_input()
        staff_id = self.view.get_staff_id()
        if staff_id.isdigit() and vehicle_id.isdigit():
            self.model.add_staff(staff_id, position, name, vehicle_id)
        else:
            print("Error! Wrong input")

    def view_staff_al(self):
        s = self.model.get_all_staff()
        self.view.show_staff_alchemy(s)

    def update_staff(self):
        staff_id = self.view.get_staff_id()
        position, name, vehicle_id = self.view.get_staff_input()
        if staff_id.isdigit() and vehicle_id.isdigit():
            self.model.update_notes(staff_id, position, name, vehicle_id)
        else:
            print("Error! Wrong input")

    def delete_staff(self):
        staff_id = self.view.get_staff_id()
        if staff_id.isdigit():
            self.model.delete_notes(staff_id)
        else:
            print("Error! Wrong input")

    def add_user(self):
        phone, name, surname = self.view.get_user_input()
        user_id = self.view.get_user_id()
        if user_id.isdigit():
            self.model.add_user(user_id, phone, name, surname)
        else:
            print("Error! Wrong input")

    def view_user_al(self):
        users = self.model.get_all_user()
        self.view.show_user_alchemy(users)

    def update_user(self):
        user_id = self.view.get_user_id()
        phone, name, surname = self.view.get_user_input()
        if user_id.isdigit() and name.isalpha() and surname.isalpha():
            self.model.update_user(user_id, phone, name, surname)
            self.view.show_message("Updated successfully!")
        else:
            print("Error! Wrong input")

    def delete_user(self):
        user_id = self.view.get_user_id()
        if user_id.isdigit():
            self.model.delete_user(user_id)
        else:
            print("Error! Wrong input")

    def add_booking(self):
        booking_id = self.view.get_booking_id()
        user_id, vehicle_id, price, booking_time = self.view.get_booking_input()
        if booking_id.isdigit() and vehicle_id.isdigit() and user_id.isdigit():
            self.model.add_booking(booking_id, user_id, vehicle_id, price, booking_time)
        else:
            print("Error! Incorrect id")

    def view_booking_al(self):
        b = self.model.get_all_booking()
        self.view.show_booking_alchemy(b)

    def update_booking(self):
        booking_id = self.view.get_booking()
        user_id, vehicle_id, price, booking_time = self.view.get_booking_input()
        if booking_id.isdigit() and vehicle_id.isdigit() and user_id.isdigit():
            self.model.update_save_notes(booking_id, user_id, vehicle_id, price, booking_time)
        else:
            print("Error! Incorrect id")

    def delete_booking(self):
        booking_id = self.view.get_booking_id()
        if booking_id.isdigit():
            self.model.delete_booking(booking_id)
        else:
            print("Error! Incorrect id.")
