### constants.py
"""Configurações visuais e de UI."""
import pygame

# Paleta de cores
BG_TOP = (25, 25, 35)
BG_BOTTOM = (10, 10, 15)
WIRE_ON = (50, 220, 50)
WIRE_OFF = (180, 60, 60)
GATE_FILL_ON = (60, 180, 60)
GATE_FILL_OFF = (180, 60, 60)
SELECT_BORDER = (255, 255, 0)
LAMP_ON = (255, 230, 90)
LAMP_OFF = (90, 90, 90)

# Raio / tamanhos
GATE_SIZE = (80, 50)  # largura, altura do retângulo
GATE_RADIUS = 10
NODE_RADIUS = 24  # lâmpada

pygame.font.init()
FONT_SMALL = pygame.font.SysFont("consolas", 20)
FONT_MED = pygame.font.SysFont("consolas", 24, bold=True)