from distutils.core import setup, Extension
import os

base = os.path.split(os.path.abspath(__file__))[0]


setup(
    name='sample',
    ext_modules = [
        Extension(
            'sample',
            ['cal.c'],
            include_dirs=[base],
            define_macros=[],
            undef_macros=[],
            library_dirs=[base],
            libraries=['sample']
        )
    ]
)