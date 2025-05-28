import datetime as dt
from datetime import timedelta
import pandas as pd

class MachineOperation:

    def __init__(self):
        self.machines = self.load_json()

    def get_date(self):
        return dt.datetime.today()

    def load_json(self):

        try:
            self.machines = pd.read_json("Machine List.json", orient='index', convert_dates=["Next maintenance date"], keep_default_dates=True)

        except FileNotFoundError:
            print("File not found. Initialize empty DataFrame")
            self.machines = pd.DataFrame(
                columns=["Machine name", "Next maintenance date", "Status", "Note"])

        except ValueError:
            print("Invalid JSON format. Initialize empty DataFrame")
            self.machines = pd.DataFrame(
                columns=["Machine name", "Next maintenance date", "Status", "Note"])

        return self.machines

    def save_to_json(self):

        self.machines = self.machines.sort_index()
        self.machines.to_json("Machine List.json", orient="index", indent=4)

    def add_machine(self, machine_name, machine_id):
        today = self.get_date()
        next_maintenance_date = (today + timedelta(weeks=4)).strftime("%Y-%m-%d")

        new_row = pd.DataFrame({
            "Machine name": [machine_name],
            "Next maintenance date": [next_maintenance_date],
            "Status": ["New"],
            "Note": [f"Machine installed at {today}"]
        }, index=[machine_id])

        self.machines = pd.concat([self.machines, new_row])
        self.save_to_json()

        print(f"\nMachine detail: \n {new_row} \n---is saved")
        input("\nPress enter to proceed...")

    def update_machine(self, machine_id):
        today = pd.to_datetime(self.get_date())

        try:
            maintenance_progress = input("\nMaintenance finish? Y/N: ").capitalize().strip()

            if maintenance_progress == "Y":
                next_maintenance_date = (today + timedelta(weeks=4)).strftime("%Y-%m-%d")
                status = f"Maintained"
                note = f"Performed on {today.strftime("%Y-%m-%d")}"

            elif maintenance_progress == "N":
                next_maintenance_date = (today + timedelta(days=3)).strftime("%Y-%m-%d")
                status = "Maintenance in progress..."
                note = f"Finish by {next_maintenance_date}"
        except ValueError:
            print("Invalid input. Please input Y for yes and N for No")

        # input the updated value in the machine detail
        self.machines.loc[machine_id, ["Next maintenance date", "Status", "Note"]] = [next_maintenance_date, status,
                                                                                      note]
        self.save_to_json()

        print("Machine detail updated.")
        print("------------------------------------------------------------------------------")
        print(self.machines.loc[machine_id])
        print("------------------------------------------------------------------------------")
        input("\nPress enter to proceed...")

    def remove_machine(self, machine_id):

        try:
            print(f"Machine ({machine_id}) details will be removed.")
            delete_machine = input("Confirm to remove the machine? Y/N: ").capitalize()

            if delete_machine == "Y":
                self.machines.drop(index=machine_id, inplace=True)
                self.save_to_json()
                print("--------------------------------------------------------------")
                print(f"Machine ({machine_id}) details has been removed.")
                print("--------------------------------------------------------------")

            elif delete_machine == "N":
                return
        except ValueError:
            print("Invalid input. Please input Y for yes and N for No")

        print("Returning to main menu....")
        input("\nPress enter to proceed...")

    def view_detail(self):
        self.remaining_day()
        pd.set_option('display.max_columns', None)
        print(self.machines)
        input("\nPress enter to proceed...")

    def upcoming_maintenance(self):
        self.remaining_day()
        upcoming = self.machines[self.machines["Day Remaining"] < 10]

        print("--------------------------------------------------------------------------")
        print("Machine to be maintained within 10 days:")
        print("--------------------------------------------------------------------------")

        if not upcoming.empty:
            pd.set_option('display.max_columns', None)
            print(upcoming.loc[:, ["Machine name", "Note", "Day Remaining"]])
        else:
            print("None")
        print("--------------------------------------------------------------------------")

    def remaining_day(self):
        today = pd.to_datetime(self.get_date())

        self.machines["Next maintenance date"] = self.machines["Next maintenance date"].astype(str)
        self.machines["Next maintenance date"] = pd.to_datetime(self.machines["Next maintenance date"],
                                                                format="%Y-%m-%d", errors="coerce")
        self.machines["Day Remaining"] = (self.machines["Next maintenance date"] - today).dt.days


# End of Class_______________________________________________________________________
