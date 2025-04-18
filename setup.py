from setuptools import setup, find_packages

setup(
    name='password_generator',
    version='0.1',
    packages=find_packages(where='develop'),
    package_dir={'': 'develop'},
)
