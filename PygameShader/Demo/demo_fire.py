"""
PygameShader FIRE DEMO
"""

from random import uniform, randint

# from PygameShader.shader_gpu import block_grid, block_and_grid_info, wave_gpu

try:
    from PygameShader.shader import custom_map, rgb_to_int, fire_effect, wave
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
    from pygame import Surface, RLEACCEL, QUIT, K_SPACE, BLEND_RGB_ADD
    from pygame.transform import scale

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
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN, vsync=True)
SCREEN.convert(32, RLEACCEL)
SCREEN.set_alpha(None)

pygame.init()

# Load the background image
BACKGROUND = pygame.image.load("../Assets/img.png").convert()
BACKGROUND = pygame.transform.smoothscale(BACKGROUND, (WIDTH, HEIGHT))

BACKGROUND_COPY = BACKGROUND.copy()
pygame.display.set_caption("demo fire effect")

FRAME = 0
CLOCK = pygame.time.Clock()
GAME = True


def palette_array() -> tuple:
    """
    Create a C - buffer type data 1D array containing the
    fire color palette (mapped RGB color, integer)

    :return: 1D contiguous array (C buffer type data)
    """
    # Set an array with pre-defined color wavelength
    arr = numpy.array([0, 1,        # violet
                       0, 1,        # blue
                       0, 1,        # green
                       2, 600,      # yellow
                       601, 650,    # orange
                       651, 660],   # red
                      numpy.int32)

    heatmap = [custom_map(i - 20, arr, 1.0) for i in range(380, 800)]
    heatmap_array = numpy.zeros((800 - 380, 3), uint8)
    heatmap_rescale = numpy.zeros(255, numpy.uint)

    i = 0
    for t in heatmap:
        heatmap_array[i, 0] = t[0]
        heatmap_array[i, 1] = t[1]
        heatmap_array[i, 2] = t[2]
        i += 1

    for r in range(255):
        s = int(r * (800.0 - 380.0) / 255.0)
        heatmap_rescale[r] = \
            rgb_to_int(heatmap_array[s][0], heatmap_array[s][1], heatmap_array[s][2])

    heatmap_rescale = numpy.ascontiguousarray(heatmap_rescale[::-1])

    return heatmap_rescale


fire_palette = palette_array()
fire_array = numpy.zeros((HEIGHT, WIDTH), dtype=numpy.float32)

avg = []
bpf = 0
delta = +0.1

# grid, block = block_grid(WIDTH, HEIGHT)
# block_and_grid_info(WIDTH, HEIGHT)

while GAME:

    pygame.event.pump()
    for event in pygame.event.get():

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            GAME = False
            break

    # image = wave_gpu(BACKGROUND, 8 * 3.14 / 180.0 + FRAME / 10, 8, grid, block)
    # image = scale(image, (WIDTH + 16, HEIGHT + 16))  # Hide the left and bottom borders
    # SCREEN.blit(image, (0, 0))

    SCREEN.blit(BACKGROUND, (0, 0))

    # Execute the shader fire effect
    surface_ = fire_effect(
        WIDTH,
        HEIGHT,
        3.97 + uniform(-0.012, 0.012),
        fire_palette,
        fire_array,
        fire_intensity_         =randint(0, 32),
        reduce_factor_          =3,
        bloom_                  =True,
        fast_bloom_             =False,
        bpf_threshold_          = bpf,
        brightness_             =True,
        brightness_intensity_   = 0.095 + uniform(0.055, 0.09),
        transpose_              =False,
        border_                 =False,
        low_                    =30,
        high_                   =WIDTH-30,
        blur_                   =True,
        smooth_                 =True
    ).convert(32, RLEACCEL)

    SCREEN.blit(surface_, (0, 0), special_flags=BLEND_RGB_ADD)
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
        "Test fire_effect %s fps "
        "(%sx%s)" % (round(CLOCK.get_fps(), 2), WIDTH, HEIGHT))


pygame.quit()