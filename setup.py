'''setup module'''
from setuptools import setup, find_packages


setup(
    name="Calculator",
    version="0.5",
    packages=find_packages(),
    license="GPL",
    entry_points={
        'console_scripts': ['calculate = app:main'],
        'setuptools.installation': ['eggsecutable = app:main']
    }
)
