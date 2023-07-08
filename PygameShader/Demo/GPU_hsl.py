"""
PygameShader HSL DEMO
"""
from random import randint, uniform, randrange

try:
    import numpy
    from numpy import uint8
except ImportError:
    raise ImportError("\n<numpy> library is missing on your system."
          "\nTry: \n   C:\\pip install numpy on a window command prompt.")

# PYGAME IS REQUIRED
try:
    import pygame
    from pygame import Surface, RLEACCEL, QUIT, K_SPACE, BLEND_RGB_ADD
    from pygame.surfarray import pixels3d

except ImportError:
    raise ImportError("\n<Pygame> library is missing on your system."
          "\nTry: \n   C:\\pip install pygame on a window command prompt.")

try:
    import cupy
except ImportError:
    raise ImportError("\n<Pygame> library is missing on your system."
                      "\nTry: \n   C:\\pip install cupy on a window command prompt.")

try:
    import PygameShader
    from PygameShader.shader_gpu import block_grid, hsl_gpu, \
        get_gpu_info, block_and_grid_info, area24_gpu
except ImportError:
    raise ImportError("\n<PygameShader> library is missing on your system."
                      "\nTry: \n   C:\\pip install PygameShader on a window command prompt.")


def show_fps(screen_, fps_, avg_) -> None:
    """ Show framerate in upper left corner """
    font = pygame.font.SysFont("Arial", 15)
    fps = str(f"fps:{fps_:.3f}")
    av = sum(avg_)/len(avg_) if len(avg_) > 0 else 0

    fps_text = font.render(fps, 1, pygame.Color("coral"))
    screen_.blit(fps_text, (10, 0))
    if av != 0:
        av = str(f"avg:{av:.3f}")
        avg_text = font.render(av, 1, pygame.Color("coral"))
        screen_.blit(avg_text, (100, 0))
    if len(avg_) > 200:
        avg_ = avg_[200:]


get_gpu_info()

width = 800
height = 600

SCREENRECT = pygame.Rect(0, 0, width, height)
SCREEN = pygame.display.set_mode(SCREENRECT.size, pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.SCALED)

pygame.init()

background = pygame.image.load('..//Assets//Parrot.jpg')
background = pygame.transform.smoothscale(background, (width, height))
background.convert(32, RLEACCEL)
background.set_alpha(None)
# background_copy = background.copy()

FRAME = 0
clock = pygame.time.Clock()
avg = []
v = 0.01
hsl = 0
# TWEAKS
cget_fps = clock.get_fps
event_pump = pygame.event.pump
event_get = pygame.event.get
get_key = pygame.key.get_pressed
get_pos = pygame.mouse.get_pos
flip = pygame.display.flip

STOP_GAME = True

grid, block = block_grid(width, height)
block_and_grid_info(width, height)

while STOP_GAME:

    event_pump()

    keys = get_key()
    for event in event_get():

        if keys[pygame.K_ESCAPE]:
            STOP_GAME = False
            break

        if event.type == pygame.MOUSEMOTION:
            MOUSE_POS = event.pos

    image = hsl_gpu(background, hsl, grid, block)

    SCREEN.blit(image, (0, 0))
    t = clock.get_fps()
    avg.append(t)
    show_fps(SCREEN, t, avg)
    pygame.display.flip()
    clock.tick()
    FRAME += 1

    # pygame.display.set_caption(
    #     "Demo HSL GPU %s fps"
    #     "(%sx%s)" % (round(clock.get_fps(), 2), width, height))

    hsl += v
    if hsl > 1.0:
        hsl = 0.99
        v *= -1
    if hsl < 0.0:
        hsl = 0.01
        v *= -1
    # background = background_copy.copy()

pygame.quit()