### ui.py
import pygame
from components import Lamp, InputNode
from constants import *


def _draw_gradient_background(surface):
    """Preenche a tela com um gradiente vertical BG_TOP -> BG_BOTTOM."""
    height = surface.get_height()
    for y in range(height):
        ratio = y / height
        r = BG_TOP[0] * (1 - ratio) + BG_BOTTOM[0] * ratio
        g = BG_TOP[1] * (1 - ratio) + BG_BOTTOM[1] * ratio
        b = BG_TOP[2] * (1 - ratio) + BG_BOTTOM[2] * ratio
        pygame.draw.line(surface, (int(r), int(g), int(b)), (0, y), (surface.get_width(), y))


def _draw_logic_gate(screen, gate, label_text):
    x, y = gate.pos
    w, h = GATE_SIZE
    rect = pygame.Rect(x - w // 2, y - h // 2, w, h)

    color = GATE_FILL_ON if gate.output else GATE_FILL_OFF
    pygame.draw.rect(screen, color, rect, border_radius=GATE_RADIUS)

    # Bordas e seleção
    border_color = SELECT_BORDER if gate.selected else (0, 0, 0)
    pygame.draw.rect(screen, border_color, rect, 3, border_radius=GATE_RADIUS)

    # Texto
    label = FONT_SMALL.render(label_text, True, (255, 255, 255))
    screen.blit(label, (x - label.get_width() // 2, y - label.get_height() // 2))


def _draw_input_node(screen, node):
    x, y = node.pos
    outer = SELECT_BORDER if node.selected else (150, 150, 150)
    inner = (50, 50, 50)
    pygame.draw.circle(screen, outer, (x, y), NODE_RADIUS)
    pygame.draw.circle(screen, inner, (x, y), NODE_RADIUS - 4)

    val_color = LAMP_ON if node.output else LAMP_OFF
    pygame.draw.circle(screen, val_color, (x, y), 8)


_def_icon_cache = {}


def _draw_lamp(screen, lamp):
    x, y = lamp.pos
    # Glow
    if lamp.output:
        glow_surface = pygame.Surface((NODE_RADIUS * 4, NODE_RADIUS * 4), pygame.SRCALPHA)
        pygame.draw.circle(glow_surface, (*LAMP_ON, 60), (glow_surface.get_width() // 2, glow_surface.get_height() // 2), NODE_RADIUS * 2)
        screen.blit(glow_surface, (x - glow_surface.get_width() // 2, y - glow_surface.get_height() // 2), special_flags=pygame.BLEND_PREMULTIPLIED)

    color = LAMP_ON if lamp.output else LAMP_OFF
    pygame.draw.circle(screen, color, (x, y), NODE_RADIUS)

    pygame.draw.circle(screen, (200, 200, 200), (x, y), NODE_RADIUS, 3)
    if lamp.selected:
        pygame.draw.circle(screen, SELECT_BORDER, (x, y), NODE_RADIUS + 4, 2)


def _draw_wire(screen, start, end, state):
    color = WIRE_ON if state else WIRE_OFF
    pygame.draw.line(screen, color, start.pos, end.pos, 4)


def draw_game(screen, components, wires, output, level_id):
    _draw_gradient_background(screen)

    # Desenha fios primeiro (para ficarem abaixo dos nós)
    for start, end in wires:
        state = start.output
        _draw_wire(screen, start, end, state)

    # Desenha componentes
    for comp in components:
        if isinstance(comp, Lamp):
            _draw_lamp(screen, comp)
        elif isinstance(comp, InputNode):
            _draw_input_node(screen, comp)
        else:
            _draw_logic_gate(screen, comp, type(comp).__name__.replace("Gate", ""))

    # UI fixa
    info_text = f"Lamp ON: {bool(output.output) if output.output is not None else 'N/A'}"
    info_surf = FONT_MED.render(info_text, True, (240, 240, 240))
    screen.blit(info_surf, (screen.get_width() - info_surf.get_width() - 20, 20))

    lvl_surf = FONT_MED.render(f"LEVEL {level_id}", True, (240, 240, 240))
    screen.blit(lvl_surf, (20, 20))
