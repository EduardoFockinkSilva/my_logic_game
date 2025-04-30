from ursina import Entity, color
from typing import Tuple

class ClickableSphere(Entity):
    """
    Esfera clicável que alterna entre estados ligado/desligado.
    """
    def __init__(
        self,
        position: Tuple[float, float, float],
        scale: float = 0.5,
    ):
        super().__init__(
            model='sphere',
            position=position,
            scale=scale,
            color=color.gray,
            collider='sphere'
        )
        # cores para os estados
        self._off_color = color.gray
        self._on_color = color.yellow

    def toggle(self) -> None:
        """
        Alterna o estado da esfera entre ligado (amarelo) e desligado (cinza).
        """
        self.color = self._on_color if self.color == self._off_color else self._off_color


class Lamp(Entity):
    """
    Lâmpada que muda de cor com base no estado lógico.
    """
    def __init__(
        self,
        position: Tuple[float, float, float],
        scale: float = 0.5,
    ):
        super().__init__(
            model='sphere',
            position=position,
            scale=scale,
            color=color.gray
        )

    def update_state(self, active: bool) -> None:
        """
        Atualiza a cor da lâmpada conforme o estado da lógica.
        """
        self.color = color.yellow if active else color.gray
