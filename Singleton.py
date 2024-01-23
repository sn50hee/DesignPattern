class Singleton:
    _instances = {}

    def __new__(cls, name):
        if name not in cls._instances:
            cls._instances[name] = super(Singleton, cls).__new__(cls)
            cls._instances[name]._name = name
        return cls._instances[name]

    def get_name(self):
        return self._name

obj1 = Singleton("Instance 1")
obj2 = Singleton("Instance 2")

print(obj1.get_name())
print(obj2.get_name())
print(obj1 is obj2)