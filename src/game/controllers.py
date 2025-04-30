from ursina import mouse, camera, EditorCamera, Vec2, time
from typing import List
import game.config as cfg
from game.entities import ClickableSphere, Lamp
from game.logic import LogicGate

class GameController:
    def __init__(self):
        EditorCamera(
            rotation_speed=0,
            move_speed=0,
            rotate_button=None,
            pan_button='f up',
            zoom_button='scroll'
        )
        camera.position = (0, 0, -5)
        camera.look_at((0, 0, 0))

        self.orbiting = False
        self.last_mouse_pos = Vec2(0, 0)

        self.spheres: List[ClickableSphere] = [
            ClickableSphere(position=(-1.5, 0, 0)),
            ClickableSphere(position=(-1.5, -1, 0)),
        ]
        self.lamp = Lamp(position=(1.5, -0.5, 0))

    def input(self, key: str) -> None:
        print(f'Input: {key}')
        if key == 'mouse2 up':
            self.orbiting = True
            self.last_mouse_pos = Vec2(mouse.x, mouse.y)
        elif key == 'mouse3 up':
            self.orbiting = False
        elif key == 'mouse1 up':

            hovered = mouse.hovered_entity
            if hovered in self.spheres:
                hovered.toggle()
                active = LogicGate.and_gate(self.spheres)
                self.lamp.update_state(active)

    def update(self) -> None:
        if self.orbiting:
            current = Vec2(mouse.x, mouse.y)
            delta = current - self.last_mouse_pos
            sensitivity = cfg.CAMERA_SENSITIVITY
            camera.orbit('y', delta.x * sensitivity * time.dt, origin=(0, 0, 0))
            camera.orbit('x', -delta.y * sensitivity * time.dt, origin=(0, 0, 0))
            self.last_mouse_pos = current
