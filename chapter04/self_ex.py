from chapter04.class_method import Date


class Person:
    """人"""
    name = "user"


class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name


if __name__ == '__main__':
    user = Student("Mooc")
    print(user.__dict__)  # {'school_name': 'Mooc'}
    print(user.name)  # user
    # 为什么 name 属性不在 user 的 __dict__ 中呢？
    # 因为 name 是 Person 的属性，不是 Student 的

    print(Person.__dict__)

    user.__dict__['school_addr'] = "Beijing"
    print(user.school_addr)  # Beijing

    print(dir(user))  # 列出对象的所有属性，只列出属性名，不列出值
