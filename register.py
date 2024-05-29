from user import User

user = User()
user.register("James", 111,  "test@mail,com", "abc")
email = input("Enter your email")
password = input("Enter your password")

print(user.login(email, password))

#login
class User:
    def register(self, name, phone, email, password):
        return name
user = User()
print(User.register("","James", 111, "J@Z.com", "abc" ))
