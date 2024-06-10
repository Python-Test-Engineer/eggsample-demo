from setuptools import find_packages
from setuptools import setup


setup(
    name="eggsample",
    install_requires="pluggy",
    entry_points={"console_scripts": ["eggsample=eggsample.host:main"]},
    packages=find_packages(),
)
