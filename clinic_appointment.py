print("🏥 Clinic Appointment Management System")

appointments = []

while True:
    print("\n1. Add Patient")
    print("2. View Appointments")
    print("3. Search Patient")
    print("4. Update Appointment")
    print("5. Cancel Appointment")
    print("6. Count Appointments")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # Add Patient
    if choice == "1":
        patient_id = input("Enter patient ID: ")
        name = input("Enter patient name: ")
        doctor = input("Enter doctor name: ")
        date = input("Enter appointment date: ")

        appointment = {
            "id": patient_id,
            "name": name,
            "doctor": doctor,
            "date": date
        }

        appointments.append(appointment)

        print("✅ Appointment added successfully!")

    # View Appointments
    elif choice == "2":
        if len(appointments) == 0:
            print("❌ No appointments found.")
        else:
            print("\n📋 Appointment Details")
            print("--------------------------")

            for appointment in appointments:
                print("Patient ID:", appointment["id"])
                print("Patient Name:", appointment["name"])
                print("Doctor:", appointment["doctor"])
                print("Appointment Date:", appointment["date"])
                print("--------------------------")

    # Search Patient
    elif choice == "3":
        search_id = input("Enter patient ID to search: ")

        found = False

        for appointment in appointments:
            if appointment["id"] == search_id:
                print("\n✅ Patient Found")
                print("Patient ID:", appointment["id"])
                print("Patient Name:", appointment["name"])
                print("Doctor:", appointment["doctor"])
                print("Appointment Date:", appointment["date"])
                found = True

        if not found:
            print("❌ Patient not found.")

    # Update Appointment
    elif choice == "4":
        update_id = input("Enter patient ID: ")

        found = False

        for appointment in appointments:
            if appointment["id"] == update_id:
                new_doctor = input("Enter new doctor name: ")
                new_date = input("Enter new appointment date: ")

                appointment["doctor"] = new_doctor
                appointment["date"] = new_date

                print("✅ Appointment updated successfully!")
                found = True
                break

        if not found:
            print("❌ Appointment not found.")

    # Cancel Appointment
    elif choice == "5":
        cancel_id = input("Enter patient ID to cancel appointment: ")

        found = False

        for appointment in appointments:
            if appointment["id"] == cancel_id:
                appointments.remove(appointment)
                print("✅ Appointment cancelled successfully!")
                found = True
                break

        if not found:
            print("❌ Appointment not found.")

    # Count Appointments
    elif choice == "6":
        print("📅 Total Appointments:", len(appointments))

    # Exit
    elif choice == "7":
        print("Thank you for using Clinic Appointment System! 🏥")
        break

    else:
        print("❌ Invalid choice!")
