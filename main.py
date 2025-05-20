### main.py
import sys
import pygame
from ui import draw_game
from engine import update_gates, handle_click
from levels import load_level
from components import InputNode, Lamp

pygame.init()
screen = pygame.display.set_mode((960, 640))
pygame.display.set_caption("Boolean Logic Puzzle")
clock = pygame.time.Clock()

# --- Controle de níveis ---
current_level = 1
components, wires, output = load_level(current_level)

selected = None
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clicked = handle_click(event.pos, components)
            if clicked:
                if isinstance(clicked, InputNode):
                    clicked.toggle()
                elif isinstance(clicked, Lamp) and clicked.output:
                    if current_level == 1:
                        current_level = 2
                        components, wires, output = load_level(current_level)
                        selected = None
                        continue
                    elif current_level == 2:
                        running = False
                        continue
                if selected:
                    selected.selected = False
                selected = clicked
                selected.selected = True

    update_gates(components)
    draw_game(screen, components, wires, output, current_level)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()