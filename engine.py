### engine.py
def update_gates(components):
    for comp in components:
        comp.evaluate()

def handle_click(pos, components, radius=28):
    x, y = pos
    for comp in components:
        dx = comp.pos[0] - x
        dy = comp.pos[1] - y
        if dx * dx + dy * dy <= radius * radius:
            return comp
    return None
