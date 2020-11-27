class User():

    def __init__(self, first_name: str, last_name: str, age: int, sex: str):
        """
        docstring
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0

    def describe_user(self):
        all_data = self.first_name.title() + '\n' + self.last_name.title() + '\n' + str(self.age) + '\n' + self.sex.title()
        return all_data

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):

    def __init__(self, first_name, last_name, age, sex):
        super().__init__(first_name, last_name, age, sex)
        self.privileges_1 = ['разрешено добавлять сообщения', 'разрешено  удалять пользователей', 'разрешенобанить пользователей']
        self.privileges_2 = Privileges()

    def show_privileges(self):
        privileges_1 = self.privileges_1
        return privileges_1

class Privileges():

    def __init__(self):
        self.privileges_2 = ['разрешено добавлять сообщения', 'разрешено  удалять пользователей', 'разрешенобанить пользователей']
        
    def show_privileges(self):
        privileges_2 = self.privileges_2
        return privileges_2    

user_2 = Admin('loh', 'pidr', 13, 'LadyBoy')
print (user_2.describe_user())
print (user_2.show_privileges())

user_3 = Admin('333', '444', 99, 'Female')
print (user_3.describe_user())
print (user_3.privileges_2.show_privileges())

# user_1 = User('bob', 'doom', 32, 'male')
# user_1.increment_login_attempts()
# print (user_1.describe_user())
# user_1.increment_login_attempts()
# user_1.increment_login_attempts()
# print (user_1.login_attempts)
# user_1.reset_login_attempts()
# print (user_1.login_attempts)

