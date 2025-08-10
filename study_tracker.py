def show_menu():
    print("\nStudy Tracker Menu:")
    print("1. Add Study Session")
    print("2. View All Sessions")
    print("3. Show Summary")
    print("4. Exit")

def main():
    sessions = []

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            subject = input("Enter subject: ")
            duration = input("Enter duration in minutes: ")
            try:
                duration = int(duration)
                sessions.append({'subject': subject, 'duration': duration})
                print("Session added.")
            except ValueError:
                print("Please enter a valid number for duration.")

        elif choice == "2":
            if not sessions:
                print("No study sessions recorded.")
            else:
                print("\nAll Study Sessions:")
                for i, session in enumerate(sessions, 1):
                    print(f"{i}. {session['subject']} - {session['duration']} minutes")

        elif choice == "3":
            total_time = sum(session['duration'] for session in sessions)
            print(f"\nTotal study time: {total_time} minutes")

        elif choice == "4":
            print("Exiting Study Tracker. Good luck!")
            break

        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
