class OldSystem:
    def perform_operation(self):
        return "Old System Operation"

class NewSystem:
    def execute(self):
        return "New System Execution"

class Adapter(NewSystem):
    def __init__(self, old_system):
        self.old_system = old_system

    def execute(self):
        return f"Adapter: {self.old_system.perform_operation()}"

old_system = OldSystem()
adapter = Adapter(old_system)

print(old_system.perform_operation())
print(adapter.execute())