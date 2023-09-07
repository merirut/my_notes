from setuptools import setup, find_packages

setup(
    name='my_notes',
    version='0.1.0',
    packages=find_packages(),
    package_data={'my_notes': ['*.ui']},
    install_requires='PyQt5'
)