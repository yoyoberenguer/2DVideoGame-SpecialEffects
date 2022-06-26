# Pygame Shaders Library 


*New Version 1.0.5*

Some scripts have been ported to GPU using CUPY and CUDA raw Kernels for running 
on NVIDIA graphics cards (NVIDIA CUDA GPU with the compute Capability 3.0 or larger.). 
These shaders are only compatible with NVIDIA chipset.

In order to use the GPU shaders the library `CUPY` has to be 
installed on your system in addition to CUDA Toolkit: 
v10.2 / v11.0 / v11.1 / v11.2 / v11.3 / v11.4 / v11.5 / v11.6. 
Please refer to the below link for the full installation 
https://docs.cupy.dev/en/stable/install.html

The GPU shaders are still experimental, and the performances are restricted
by the pci-express bandwidth due to the amount of data sent from the CPU to 
the GPU, especially when the shaders are use for real time rendering.

Check the Shader GPU_demo_ripple.py in the `Demo folder` for an example of real time 
rendering of a pygame.Surface.

How this shaders compare to GLSL (GL shading language): 
You may ask yourself how fast these shaders perform against the shading language GLSL,
well without any doubt GLSL outperform CUPY & CUDA for graphics performance. 
However, CUDA is taking advantage of its highly parallelized architecture and will improve 
the speed of pygame, python & cython algorithms designed for CPU architecture only.

Difference between shading language and CUDA:
CUDA is essentially just a way to run compute shaders without the graphics API and
without requiring a particular language. CUDA programs are compiled into PTX (NVIDIA's
analoque to x86 assembly for the GPU.

For the curious, please check this excellent post 
https://carpentries-incubator.github.io/lesson-gpu-programming/aio/index.html
to have an overview of CUPY and CUDA 

`A wiki page will be soon available for the GPU shaders`


---

*New version 1.0.4* and WIKI available here https://github.com/yoyoberenguer/PygameShader/wiki
```
pip install PygameShader==1.0.4
```


Pygame shader project is a `2D game library` written in Python and Cython containing
`special effects` for development of multimedia applications like video games, arcade game, 
video and camera image processing or to customize your sprites textures/surfaces.

This library is compatible with BMP, GIF (non - animated), JPEG, PNG image format.
```
pygame may not always be built to support all image formats. At minimum it will support 
uncompressed BMP. If pygame.image.get_extended() returns 'True', you should be able to
load most images (including PNG, JPG and GIF).
```

The shaders can be applied to the `entire game display` for a real time rendering @ 60 fps
for games running in medium resolution such as `1024 x 768`. 
Some algorithms are more demanding than others in terms of processing power 
ex : median filtering and predator vision (due to the fact that it is built with more
than one shader to provide a composite effect). Consequently, not all shader will run at
the same speed at medium resolutions. Feel free to experiment with higher display resolutions
while the shader provides 60 fps or above.

If you are using the shader library for sprites texturing and special effects
then the overall processing time should be extremely fast due to code optimization with
cython. Nevertheless, to keep a good frame rate, it is advised to keep the sprites below
the screen display resolution e,g 200x200 texture size.

The shaders effect can be placed into 5 different categories
* Color variations
* Filters
* Transformations
* Ambiances
* Special effects
 
Some effects can be used for interaction with the player(s) (ex the player is being hit
and receive damages, use the shader blood effect to turn your screen red).
Screen shacking after an explosion, check the shader dampening effect (horizontal or zoom in/out)
Player is pausing the game, use the blur effect to blur the background image.
You need to change the brightness of a scene uses the shader brightness.
Sprite texture colors can be changed over time with the HSL algorithm.
Your game needs to look a bit more retro, use the reduction shader to decrease the amount
of colors in your texture or display
etc

PygameShader provide tools to improve your overall game appearance by changing 
Sprites texture/surface and or by using great special effects that will affect 
the entire screen. 

This version contains the following shaders:  

* `Color variations`
  
  - RGB to BGR (Change your game display from RGB to a BGR model) 
  - RGB to BRG (Change your game display from RGB to a BRG model) 
  - grayscale mode
  - sepia; Sepia mode  
  - color reduction, decrease the amount of color 
  - hsl Rotate the colors
  - invert (Invert the game display negative color)
  - plasma (Add a plasma effect to your display)
  - heatmap conversion

* `Filters`
  - median* 
  - sobel effect (edge display)
  - gaussian blur 5x5 (add a blur effect to your game)
  - sharpen filter (increase the image sharpness)
  - bright pass filter (bpf) 
  
* `Transformations`
  - wave effect, create a wave effect to your game display
  - swirl, swirl the entire screen or texture 
  - horizontal glitch, create a glitch effect affecting 
    your display
  - mirroring 
  - lateral dampening (lateral dampening effect that can 
    be used  for explosions)
  - dampening effect (zoom in and out dampening effect)
  - fisheye your game display is turned into a fisheye model
  - heatwave 

* `Ambiances`
  - brightness, increase / decrease the brightness of your
    texture or game display in real time
  - saturation, increase / decrease the level of saturation 

* `Special effects` 
  - bloom effect, real time bloom effect for your display
  - water ripple effect, create water ripple effect in real 
    time on your game display 
  - tunnel effect, show a tunnel effect 
  - tv scanline, TV scanline effect
  - blood effect, use a red vignette to color your screen 
    each time your player is taking damage 
  - predator vision, create a predator vision mode
  - fire effect, Display an amazing fire effect onto your 
    game display or texture in real time
  - smoke/cloud effect, create a smoke effect or moving cloud 
  - RGB split, split all the RGB channels separately and display 
    the R, G and B channel with an offset
  - rain (bubble effect), You can generate a hundred bubbles or 
    water droplets on your game display, the droplets/bubbles will 
    reflect the game display in real time
 
* New in version 1.0.3 
  - Added blending mode for `Predator mode`                  
  - New algorithm `dirt_lens effect` bokeh effect (texture available in Assets directory)
  - `Dithering` The classic dithering effect to create a retro image effect
  - `Color_palette` to convert image into Amstrad CPC 6128
     COMMODORE C64, ZX SPECTRUM etc 
  - `Bilateral filter`Blur effect that conserve the edge of an image 
  - `Emboss filter` Emboss an image or create relief 
  - `Pixelation` Pixelate an image
  - `Convert to 27 colors` Similar to color_reduction effect but cap the reduction to 27 colors
  - `Spectrum surface` Create a pygame surface that contains the light spectrum (colors)
  - `Horizontal gradient (unit misc.pyx)` New algorithms to create custom 2D - 3D gradient colors surface
  - `New transition effect (blend effect)` Transistion between two images

## Demo

Youtube : https://youtu.be/XgLF2BWP0Rs

In the PygameShader `Demo` directory 

(press ESC to quit the demo)

```commandline
C:\>python demo_fire.py
C:\>python demo_cartoon.py
C:\>python demo_wave.py
```


The project is under the `GNU GENERAL PUBLIC LICENSE Version 3`

## Installation 
check the link for newest version https://pypi.org/project/PygameShader/

* Available python build 3.6, 3.7, 3.8, 3.9, 3.10 and source build
```
pip install PygameShader 
# or version 1.0.2  
pip install PygameShader==1.0.2
```

* version installed 
* Imported module is case sensitive 
```python
>>>from PygameShader.shader import __VERSION__
>>>__VERSION__
```

## Building cython code

#### When do you need to compile the cython code ? 

Each time you are modifying any of the following files 
shader.pyx, shader.pxd, __init__.pxd or any external C code if applicable

1) open a terminal window
2) Go in the main project directory where (shader.pyx & 
   shader.pxd files are located)
3) run : `C:\>python setup_shader.py build_ext --inplace --force`

If you have to compile the code with a specific python 
version, make sure to reference the right python version 
in (`python38 setup_shader.py build_ext --inplace`)

If the compilation fail, refers to the requirement section and 
make sure cython and a C-compiler are correctly install on your
 system.
- A compiler such visual studio, MSVC, CGYWIN setup correctly on 
  your system.
  - a C compiler for windows (Visual Studio, MinGW etc) install 
  on your system and linked to your windows environment.
  Note that some adjustment might be needed once a compiler is 
  install on your system, refer to external documentation or 
  tutorial in order to setup this process.e.g https://devblogs.
  microsoft.com/python/unable-to-find-vcvarsall-bat/

## OPENMP 
In the main project directory, locate the file ```setup_shader.py```.
The compilation flag /openmp is used by default.
To override the OPENMP feature and disable the multi-processing remove the flag ```/openmp```

####
```setup_shader.py```
```python

ext_modules=cythonize(Extension(
        "*", ['*.pyx'],
        extra_compile_args=["/Qpar", "/fp:fast", "/O2", "/Oy", "/Ot"], language="c"
```
Save the change and build the cython code with the following instruction:

```python setup_shader.py build_ext --inplace --force```

If the project build successfully, the compilation will end up with the following lines
```
Generating code
Finished generating code
```
If you have any compilation error refer to the section ```Building cython code```, make sure 
your system has the following program & libraries installed. Check also that the code is not 
running in a different thread.  
- Pygame version >3
- numpy >= 1.18
- cython >=0.29.21 (C extension for python) 
- A C compiler for windows (Visual Studio, MinGW etc)

## Credit
Yoann Berenguer 

## Dependencies :
```
numpy >= 1.18
pygame >=2.0.0
cython >=0.29.21
```

## License :

GNU GENERAL PUBLIC LICENSE Version 3

Copyright (c) 2019 Yoann Berenguer

Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it is not allowed.


## Testing: 
```python
>>> import PygameShader
>>> from PygameShader.tests.test_shader import run_testsuite
>>> run_testsuite()
```