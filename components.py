### components.py
class Gate:
    def __init__(self, pos):
        self.pos = pos
        self.inputs = []
        self.output = None
        self.selected = False

    def evaluate(self):
        pass

class InputNode(Gate):
    def __init__(self, pos, value=0):
        super().__init__(pos)
        self.output = value

    def toggle(self):
        self.output = 0 if self.output else 1

class AndGate(Gate):
    def evaluate(self):
        self.output = all(inp.output for inp in self.inputs)

class OrGate(Gate):
    def evaluate(self):
        self.output = any(inp.output for inp in self.inputs)

class NotGate(Gate):
    def evaluate(self):
        self.output = None if not self.inputs else (not self.inputs[0].output)

class Lamp(Gate):
    def evaluate(self):
        if self.inputs:
            self.output = self.inputs[0].output
        else:
            self.output = None