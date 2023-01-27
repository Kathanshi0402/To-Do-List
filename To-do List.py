class ToDo:
    """This class manages the record of all the users."""
    users = {'utkarshsen': ['Utkarsh Sen', 'iamowner']}


class Signup(ToDo):                                                        # This is a child class of ToDo class
    """This class manages New Registration."""
    def __init__(self):
        self.name = input("Enter you Full name:")
        while True:
            self.newuser = input("Enter your username:")
            if self.newuser in ToDo.users.keys():                          # Checks whether username is available or not
                print("username not available. Try again!")
            else:
                break
        while True:
            self.pswd = input("Enter your password:")
            conf = input("Enter your password again:")
            if self.pswd == conf:                                           # Confirms pswd. Returns False if not matched
                ToDo.users[self.newuser] = [self.name, self.pswd]
                print("New User Created")
                break
            else:
                print("Password Does not match!")


class Login(ToDo):                                                       # Child class of ToDo class
    """This class log user in. And also updates To-Do List."""
    tasks = []
    def __init__(self):
        while True:
            self.user = input('Enter your username:')
            self.password = input('Enter your password:')
            if self.user in ToDo.users:                                    # Checks username is registered or not
                if ToDo.users[self.user][1] == self.password:              # Checks pswd. Return False if pswd is not correct
                    print("Welcome %s. Good to see you!" % ToDo.users[self.user][0])
                    break
                else:
                    print("Something Went Wrong! Try Again.")
            else:
                print("Username not available.")
                option = input('Do you want to register?(Y/N)')
                if option.upper() == 'Y':                                  # Sign up if not already registered.
                    Signup()

    def addtask(self):
        '''To add a new task.'''
        task = input('Enter task to add:')
        Login.tasks.append(task.lower())
        print('New task added!')

    def markcomplete(self):
        '''To remove completed task.'''
        complete = input('Enter completed task:')
        if complete.lower() in Login.tasks:
            Login.tasks.remove(complete.lower())
            print("Hurray, you completed a task!")
        else:
            print('Task not found!')
            option = input('Do you want to add this task?(Y/N)')
            if option.upper() == 'Y':
                self.addtask()

    def view(self):
        '''To view tasks left.'''
        if len(Login.tasks) != 0:
            foo = 'Serial Number\t\t\t\tTask'
            print(foo.center(40))
            for i in range(len(Login.tasks)):
                bar = str(i+1) + '\t\t\t\t' + str(Login.tasks[i])
                print(bar.center(50))
        else:
            print("No task to complete.")


def main():
    print("\t\t\t*****Welcome to the Online To-Do task Maintenance System!******")
    print("1. New Registration\n2. Login\n3. Exit")
    while True:
        while True:
            try:
                choice1 = int(input("Enter your choice:"))
            except ValueError:
                print('Enter a number')
            except:
                print('!!!Invalid!!!')
            else:
                break
        if choice1 == 1:
            Signup()
        elif choice1 == 2:
            newlogin = Login()
            print('\t\t\t*****Main Menu*****')
            print('1. Add a new Task \n2. Mark a task complete \n3. View Task Left \n4. Go back to previous screen')
            while True:
                while True:
                    try:
                        print('What do you want to do?')
                        choice = int(input())
                    except ValueError:
                        print('Enter a number')
                    except:
                        print('!!!Invalid!!!')
                    else:
                        break
                if choice == 1:
                    newlogin.addtask()
                elif choice == 2:
                    newlogin.markcomplete()
                elif choice == 3:
                    newlogin.view()
                elif choice == 4:
                    print("\t\t\t*****Welcome to the Online To-Do task Maintenance System!******")
                    print("1. New Registration\n2. Login\n3. Exit")
                    break
                else:
                    print('!!!Wrong Input!!!')

        elif choice1 == 3:
            print("Thank you for using the Online To-Do task Maintenance System. Have a nice day!")
            break


main()