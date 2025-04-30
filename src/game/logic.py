from typing import Iterable
from ursina import color
import game.config as cfg

class LogicGate:

    @staticmethod
    def and_gate(inputs: Iterable[object]) -> bool:
        return all(getattr(s, 'color', None) == cfg.COLOR_LAMP_ON for s in inputs)
