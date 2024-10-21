class User:
    def __init__(self, user_id=0, name="", email="", password=""):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

    def check_password(self, input_password):
        return self.password == input_password


class ServiceRequest:
    def __init__(self, request_id, user, service_type):
        self.request_id = request_id
        self.user = user
        self.service_type = service_type
        self.status = "Pending"

    def update_status(self, new_status):
        self.status = new_status


class Technician:
    technician_count = 0

    def __init__(self, name, skills):
        self.technician_id = Technician.technician_count + 1
        self.name = name
        self.skills = skills
        Technician.technician_count += 1

    def __str__(self):
        return f"Technician ID: {self.technician_id}, Name: {self.name}, Skills: {', '.join(self.skills)}"


class System:
    def __init__(self):
        self.users = {}
        self.technicians = {}
        self.service_requests = {}
        self.next_user_id = 1
        self.next_request_id = 1

    def register_user(self, name, email, password):
        new_user = User(self.next_user_id, name, email, password)
        self.users[new_user.user_id] = new_user
        print(f"User registered successfully! User ID: {new_user.user_id}")
        self.next_user_id += 1

    def login_user(self, email, password):
        for user in self.users.values():
            if user.email == email and user.check_password(password):
                print(f"Login successful! Welcome {user.name}")
                return user.user_id
        print("Login failed! Invalid credentials.")
        return -1

    def register_technician(self, name, skills):
        technician = Technician(name, skills)
        self.technicians[technician.technician_id] = technician
        print(f"Technician registered successfully! Technician ID: {technician.technician_id}")

    def submit_service_request(self, user_id, service_type):
        if user_id in self.users:
            new_request = ServiceRequest(self.next_request_id, self.users[user_id], service_type)
            self.service_requests[self.next_request_id] = new_request
            print(f"Service request submitted successfully! Request ID: {new_request.request_id}")
            self.next_request_id += 1
        else:
            print("Invalid user ID! Please register first.")

    def view_service_requests(self, user_id):
        print(f"Service Requests for User ID {user_id}:")
        for request in self.service_requests.values():
            if request.user.user_id == user_id:
                print(f"Request ID: {request.request_id} | Service Type: {request.service_type} | Status: {request.status}")

    def update_service_request_status(self, request_id, new_status):
        if request_id in self.service_requests:
            self.service_requests[request_id].update_status(new_status)
            print(f"Service request status updated to: {new_status}")
        else:
            print("Request ID not found.")


def main():
    system = System()
    while True:
        print("\n1. Register User\n2. Login User\n3. Register Technician\n4. Submit Service Request\n5. View Service Requests\n6. Update Service Request Status\n7. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter name: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            system.register_user(name, email, password)

        elif choice == 2:
            email = input("Enter email: ")
            password = input("Enter password: ")
            user_id = system.login_user(email, password)

        elif choice == 3:
            name = input("Enter technician's name: ")
            skills = input("Enter technician's skills (comma-separated): ").split(',')
            system.register_technician(name, skills)

        elif choice == 4:
            user_id = int(input("Enter your user ID: "))
            service_type = input("Enter service type (Solar/Security): ")
            system.submit_service_request(user_id, service_type)

        elif choice == 5:
            user_id = int(input("Enter your user ID: "))
            system.view_service_requests(user_id)

        elif choice == 6:
            request_id = int(input("Enter request ID: "))
            new_status = input("Enter new status: ")
            system.update_service_request_status(request_id, new_status)

        elif choice == 7:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
