class User:
    user_count = 0

    def __init__(self, name, phpone):
        self.name = name
        self.phpone = phpone
        User.user_count += 1

    @classmethod
    def get_user_count(cls):
        return cls.user_count

    @classmethod
    def create_user(cls, name, phpone):
        new_user = cls(name, phone)
       return new_user

user_1 = User('Albert', '996777111111')
print(User.user_count)
User.user_count += 1
print(User.user_count)
print(User.get_user_count())
user_2