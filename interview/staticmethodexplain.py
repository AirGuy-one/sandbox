class User:
    role = 'user'

    def __init__(self, username):
        self.username = username

    @staticmethod
    def deliver_the_signal():
        return 'right here we send the msg about some emergency'

    @classmethod
    def get_username(cls):
        return f'Role of this user is {cls.role}'


user = User('Billy')
print(User.get_username())
print(User.deliver_the_signal())
