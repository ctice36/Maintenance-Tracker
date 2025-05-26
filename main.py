from machine_operation import MachineOperation


def main_menu():
    print("\n-----------------------------")
    print("Available operation")
    print("-----------------------------")
    print("1. Add new machine")
    print("2. Update machine upcoming maintenance date")
    print("3. Remove machine")
    print("4. View machine details")
    print("5. View upcoming maintenance date")
    print("6. Exit")
    print("-----------------------------")


def repair_id_or_menu(machines, must_exist=True):  # check_machine_id,machines): #********** add

    while True:  # ********** delete.self

        print("Input the Machine ID")
        machine_id_input = input("Machine ID: ").zfill(3)  # Machine ID might be the combination of str and int
        machine_id_input = "MS" + machine_id_input
        exist = machine_id_input in machines.values

        if not must_exist and exist:
            print(f"{machine_id_input} has been registered")

        elif must_exist and not exist:
            print(f"{machine_id_input} is not registered yet")
        else:
            return machine_id_input

        print("\nDo you want to:")
        print("1. Re-input the machine id?")
        print("2. Go back to the main menu?")

        while True:
            try:
                proceed_or_not = int(input("= "))
                if proceed_or_not == 1:
                    break  # to repeat checking machine_id while loop
                elif proceed_or_not == 2:
                    print("Going back to main menu")
                    return None
                else:
                    print("Invalid input. Please choose a number between 1 or 2")
                    continue
            except ValueError:
                print("Invalid input. Please choose a number between 1 or 2")
                continue


selection = MachineOperation()
print(f"Date: {selection.get_date().strftime("%Y-%m-%d")}")
selection.upcoming_maintenance()

while True:

    main_menu()

    try:

        user_input = int(input("\nSelect the number for the operation: "))
        id_list = selection.machines.index

        if user_input == 1:
            machine_id = repair_id_or_menu(id_list, must_exist=False)
            if machine_id is None:
                continue
            # print(machine_id)
            machine_name = input("Machine Name: ").title().strip()
            # print(machine_name)
            selection.add_machine(machine_name, machine_id)

        elif user_input == 2:
            machine_id = repair_id_or_menu(id_list, must_exist=True)
            if machine_id is None:
                continue
            selection.update_machine(machine_id)

        elif user_input == 3:
            machine_id = repair_id_or_menu(id_list, must_exist=True)
            if machine_id is None:
                continue
            selection.remove_machine(machine_id)

        elif user_input == 4:
            selection.view_detail()

        elif user_input == 5:
            selection.upcoming_maintenance()
            input("\nPress enter to proceed...")

        elif user_input == 6:
            print("-----------------------------")
            print("Exit the Program...")
            break
        # elif user_input == 7:
        else:
            print("Invalid input. Please choose a number between 1-6")
    except ValueError:
        print("Invalid input. Please choose a number between 1-6")
