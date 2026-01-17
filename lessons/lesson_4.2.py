class User:
    # переменная класса
    user_count = 0

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        User.user_count += 1

    @classmethod
    def get_user_count(cls):
        return cls.user_count

    @classmethod
    def create_user(cls, name, phone):
        new_user = cls(name, phone)
        return new_user

    @staticmethod
    def validate_phone(phone: str) -> bool:
        if phone.isdigit():
            return True
        return False

user_1 = User("Albert", "99677711111")
print(User.user_count)
User.user_count += 1
print(User.user_count)
print(User.get_user_count())
user_2 = User.create_user(name="Albert", phone="11111111")