from setuptools import setup

setup(
    name='vircade',
    packages=['app'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)