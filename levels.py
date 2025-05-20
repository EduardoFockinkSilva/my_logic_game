### levels.py
from components import InputNode, AndGate, OrGate, NotGate, Lamp

def load_level(level_id):
    if level_id == 1:
        input1 = InputNode((160, 220), 1)
        input2 = InputNode((160, 340), 0)
        and_gate = AndGate((400, 280))
        lamp = Lamp((780, 280))

        and_gate.inputs = [input1, input2]
        lamp.inputs = [and_gate]

        components = [input1, input2, and_gate, lamp]
        wires = [
            (input1, and_gate),
            (input2, and_gate),
            (and_gate, lamp),
        ]
        return components, wires, lamp

    if level_id == 2:
        in1 = InputNode((120, 160), 1)
        in2 = InputNode((120, 260), 1)
        in3 = InputNode((120, 360), 0)

        or_gate = OrGate((360, 210))
        not_gate = NotGate((360, 360))
        final_and = AndGate((560, 285))
        lamp = Lamp((820, 285))

        or_gate.inputs = [in1, in2]
        not_gate.inputs = [in3]
        final_and.inputs = [or_gate, not_gate]
        lamp.inputs = [final_and]

        components = [in1, in2, in3, or_gate, not_gate, final_and, lamp]
        wires = [
            (in1, or_gate),
            (in2, or_gate),
            (in3, not_gate),
            (or_gate, final_and),
            (not_gate, final_and),
            (final_and, lamp),
        ]
        return components, wires, lamp

    raise ValueError("Level não definido")