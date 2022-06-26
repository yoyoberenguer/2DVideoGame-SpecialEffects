"""
Setup.py file

Configure the project, build the package and upload the package to PYPI


python_version setup.py sdist bdist_wheel (to include the source)

[TEST PYPI]
repository = https://test.pypi.org/

[PRODUCTION]
repository = https://upload.pypi.org/legacy/
"""

import setuptools
from Cython.Build import cythonize
from setuptools import Extension

# NUMPY IS REQUIRED
try:
    import numpy
except ImportError:
    raise ImportError("\n<numpy> library is missing on your system."
                      "\nTry: \n   C:\\pip install numpy on a window command prompt.")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# version 1.0.1 Yank, latest version 1.0.2
# pypitest latest version 1.0.17

setuptools.setup(
    name="PygameShader",
    version= "1.0.5",       # testing version "1.0.23",
    author="Yoann Berenguer",
    author_email="yoyoberenguer@hotmail.com",
    description="Pygame shader effects for 2D video game and arcade game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yoyoberenguer/PygameShader",
    # packages=setuptools.find_packages(),
    packages=['PygameShader'],
    ext_modules=cythonize([
        Extension("PygameShader.shader", ["PygameShader/shader.pyx"],
                  extra_compile_args=["/openmp", "/Qpar", "/fp:fast", "/O2", "/Oy", "/Ot"],
                  language="c"),
        Extension("PygameShader.misc", ["PygameShader/misc.pyx"],
                  extra_compile_args=["/openmp", "/Qpar", "/fp:fast", "/O2", "/Oy", "/Ot"],
                  language="c"),
        Extension("PygameShader.gaussianBlur5x5", ["PygameShader/gaussianBlur5x5.pyx"],
                  extra_compile_args=["/openmp", "/Qpar", "/fp:fast", "/O2", "/Oy", "/Ot"],
                  language="c"),
        Extension("PygameShader.Palette", ["PygameShader/Palette.pyx"],
                  extra_compile_args=["/openmp", "/Qpar", "/fp:fast", "/O2", "/Oy", "/Ot"],
                  language="c"),
        Extension("PygameShader.shader_gpu", ["PygameShader/shader_gpu.pyx"],
                  extra_compile_args=["/openmp", "/Qpar", "/fp:fast", "/O2", "/Oy", "/Ot"],
                  language="c"),
    ]),

    include_dirs=[numpy.get_include()],
    define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
    license='GNU General Public License v3.0',

    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Cython',

        # Pick your license as you wish
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        # 'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],

    install_requires=[
        'setuptools>=49.2.1',
        'Cython>=0.28',
        'numpy>=1.18',
        'pygame>=2.0',
        'cupy >=9.6.0'
    ],
    python_requires='>=3.6',
    platforms=['Windows'],
    include_package_data=True,
    data_files=[
        ('./lib/site-packages/PygameShader',
         ['LICENSE',
          'MANIFEST.in',
          'pyproject.toml',
          'README.md',
          'requirements.txt',
          'PygameShader/__init__.py',
          'PygameShader/__init__.pxd',
          'PygameShader/setup_shader.py',
          'PygameShader/shader.pyx',
          'PygameShader/shader.pxd',
          'PygameShader/misc.pyx',
          'PygameShader/misc.pxd',
          'PygameShader/gaussianBlur5x5.pyx',
          'PygameShader/Palette.pyx',
          'PygameShader/shader_gpu.pyx',
          'PygameShader/shader_gpu.pxd'
          ]),
        ('./lib/site-packages/PygameShader/Include',
         ['PygameShader/Include/ShaderLib.c'
          ]),
        ('./lib/site-packages/PygameShader/tests',
         [
             'PygameShader/tests/test_shader.py',
             'PygameShader/tests/__init__.py',
          ]),
        ('./lib/site-packages/PygameShader/Assets',
         [
             'PygameShader/Assets/Aliens.jpg',
             'PygameShader/Assets/background.jpg',
             'PygameShader/Assets/background2.jpg',
             'PygameShader/Assets/city.jpg',
             'PygameShader/Assets/ES_WaterDrip1.wav',
             'PygameShader/Assets/ES_WaterDrip2.wav',
             'PygameShader/Assets/ES_WaterDrip3.wav',
             'PygameShader/Assets/img.png',
             'PygameShader/Assets/Radial4.png',
             'PygameShader/Assets/Radial8.png',
             'PygameShader/Assets/redvignette.png',
             'PygameShader/Assets/space1.jpg',
             'PygameShader/Assets/space2.jpg',
             'PygameShader/Assets/Bokeh__Lens_Dirt_9.jpg',
             'PygameShader/Assets/Bokeh__Lens_Dirt_38.jpg',
             'PygameShader/Assets/Bokeh__Lens_Dirt_46.jpg',
             'PygameShader/Assets/Bokeh__Lens_Dirt_50.jpg',
             'PygameShader/Assets/Bokeh__Lens_Dirt_54.jpg',
             'PygameShader/Assets/Bokeh__Lens_Dirt_67.jpg'

         ]),
        ('./lib/site-packages/PygameShader/Demo',
         [
             'PygameShader/Demo/cloud_smoke_effect.py',
             'PygameShader/Demo/demo_bloom.py',
             'PygameShader/Demo/demo_fire.py',
             'PygameShader/Demo/demo_transition.py',
             'PygameShader/Demo/demo_wave.py',
             'PygameShader/Demo/GPU_cartoon.py',
             'PygameShader/Demo/GPU_demo_ripple.py',
             'PygameShader/Demo/GPU_fisheye.py',
             'PygameShader/Demo/GPU_hsl.py',
             'PygameShader/Demo/GPU_light.py',
             'PygameShader/Demo/GPU_wave.py'
         ])
    ],

    project_urls={  # Optional
        'Bug Reports': 'https://github.com/yoyoberenguer/PygameShader/issues',
        'Source': 'https://github.com/yoyoberenguer/PygameShader',
    },
)

