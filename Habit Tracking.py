logo = """

                             ____                           
|         |       .'.       |    ~.    | `````|`````        
|_________|     .''```.     |____.'_   |      |             
|         |   .'       `.   |       ~. |      |             
|         | .'           `. |_______.' |      |             
                                                            
                                                
"""
print(logo)


import datetime

class Habit:
    def __init__(self, name, frequency):
        self.name = name
        self.frequency = frequency  # Daily, Weekly, etc.
        self.log = []  # To store the progress as (date, status)

    def log_progress(self, date, status):
        self.log.append((date, status))

    def get_progress(self):
        return self.log

class HabitTracker:
    def __init__(self):
        self.habits = []

    def add_habit(self, name, frequency):
        new_habit = Habit(name, frequency)
        self.habits.append(new_habit)
        print(f"Habit '{name}' added with a frequency of '{frequency}'.")

    def log_habit(self, habit_name, date, status):
        for habit in self.habits:
            if habit.name == habit_name:
                habit.log_progress(date, status)
                print(f"Logged progress for habit '{habit_name}' on {date}.")
                return
        print(f"Habit '{habit_name}' not found.")

    def view_summary(self):
        for habit in self.habits:
            print(f"\nHabit: {habit.name} (Frequency: {habit.frequency})")
            if habit.log:
                for entry in habit.log:
                    date, status = entry
                    print(f" - {date}: {'Completed' if status else 'Not completed'}")
            else:
                print("No progress logged yet.")

def main():
    tracker = HabitTracker()

    while True:
        print("\n--- Habit Tracker Menu ---")
        print("1. Add a new habit")
        print("2. Log habit progress")
        print("3. View summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter habit name: ")
            frequency = input("Enter habit frequency (e.g., Daily, Weekly): ")
            tracker.add_habit(name, frequency)

        elif choice == '2':
            habit_name = input("Enter the habit name: ")
            date = input("Enter the date (YYYY-MM-DD): ")
            date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            status = input("Did you complete the habit? (yes/no): ").lower() == 'yes'
            tracker.log_habit(habit_name, date, status)

        elif choice == '3':
            tracker.view_summary()

        elif choice == '4':
            print("Exiting Habit Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
