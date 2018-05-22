class DataBaseObj():
    def __init__(self, new_name):
        print('init')
        self.new_name = new_name

    def __new__(cls, new_name):
        print('cls_id:', id(cls))
        return object.__new__(cls)


# print(id(DataBaseObj))
# db = DataBaseObj('mysql')
# print(db)


class SingleInstance():
    __instance = None

    def __init__(self):
        print('init')

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance


s1 = SingleInstance()
print(id(s1))
s2 = SingleInstance()
print(id(s2))
