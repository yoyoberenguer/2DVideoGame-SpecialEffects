"""
PygameShader SMOKE DEMO
"""

from random import uniform, randint

try:
    from PygameShader.shader import custom_map, rgb_to_int, cloud_effect
    from PygameShader.misc import create_horizontal_gradient_1d
except ImportError:
    raise ImportError("\n<PygameShader> library is missing on your system."
          "\nTry: \n   C:\\pip install PygameShader on a window command prompt.")

try:
    import numpy
    from numpy import uint8
except ImportError:
    raise ImportError("\n<numpy> library is missing on your system."
          "\nTry: \n   C:\\pip install numpy on a window command prompt.")

# PYGAME IS REQUIRED
try:
    import pygame
    from pygame import Surface, RLEACCEL, QUIT, K_SPACE, BLEND_RGB_ADD, \
        BLEND_RGB_SUB, BLEND_RGB_MULT, BLEND_RGB_MAX

except ImportError:
    raise ImportError("\n<Pygame> library is missing on your system."
          "\nTry: \n   C:\\pip install pygame on a window command prompt.")


def show_fps(screen_, fps_, avg_) -> None:
    """ Show framerate in upper left corner """
    font = pygame.font.SysFont("Arial", 15)
    fps = str(f"CPU fps:{fps_:.3f}")
    av = sum(avg_)/len(avg_) if len(avg_) > 0 else 0

    fps_text = font.render(fps, 1, pygame.Color("coral"))
    screen_.blit(fps_text, (10, 0))
    if av != 0:
        av = str(f"avg:{av:.3f}")
        avg_text = font.render(av, 1, pygame.Color("coral"))
        screen_.blit(avg_text, (120, 0))
    if len(avg_) > 200:
        avg_ = avg_[200:]


# Set the display to 1024 x 768
WIDTH = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN | pygame.SCALED)
SCREEN.convert(32, RLEACCEL)
SCREEN.set_alpha(None)

pygame.init()

# Load the background image
BACKGROUND = pygame.image.load("../Assets/img.png").convert()
BACKGROUND = pygame.transform.smoothscale(BACKGROUND, (WIDTH, HEIGHT))

image = BACKGROUND.copy()
pygame.display.set_caption("Clound & smoke effect")

FRAME = 0
CLOCK = pygame.time.Clock()
GAME = True


arr = numpy.array([0, 1,  # violet
                           0, 1,  # blue
                           0, 1,  # green
                           2, 619,  # yellow
                           620, 650,  # orange
                           651, 660],  # red
                          numpy.uint32)

CLOUD_ARRAY = numpy.zeros((HEIGHT, WIDTH), dtype=numpy.float32)

heatmap_rescale = numpy.zeros(256 * 2 * 3, numpy.uint32)

arr1 = create_horizontal_gradient_1d(255, (0, 0, 0), (255, 255, 255))
arr2 = create_horizontal_gradient_1d(255, (255, 255, 255), (0, 0, 0))
arr3 = numpy.concatenate((arr1, arr2), axis=None)
i = 0
for r in range(0, 1530, 3):
    heatmap_rescale[i] = rgb_to_int(arr3[r], arr3[r + 1], arr3[r + 2])
    i += 1


avg = []
bpf = 0
delta = +0.1
while GAME:

    pygame.event.pump()
    for event in pygame.event.get():

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            GAME = False
            break

    # SCREEN.fill((0, 0, 0, 0))
    SCREEN.blit(BACKGROUND, (0, 0))

    surface_ = cloud_effect(
        WIDTH, HEIGHT, 3.9650 + uniform(0.002, 0.008),
        heatmap_rescale,
        CLOUD_ARRAY,
        reduce_factor_=3, cloud_intensity_=randint(60, 128),
        smooth_=True, bloom_=True, fast_bloom_=True,
        bpf_threshold_=bpf, low_=0, high_=WIDTH, brightness_=True,
        brightness_intensity_=-0.15,
        transpose_=False, surface_=None, blur_=True
    ).convert(32, RLEACCEL)

    SCREEN.blit(surface_, (0, 0), special_flags=BLEND_RGB_MAX)
    t = CLOCK.get_fps()
    avg.append(t)
    show_fps(SCREEN, t, avg)
    pygame.display.flip()
    CLOCK.tick()
    FRAME += 1

    bpf += delta
    bpf = max(bpf, 45)
    bpf = min(bpf, 0)
    if bpf == 45:
        delta *= -1

    pygame.display.set_caption(
        "Clound & smoke effect %s fps "
        "(%sx%s)" % (round(CLOCK.get_fps(), 2), WIDTH, HEIGHT))

    avg = avg[ 10: ]


    image = BACKGROUND.copy()