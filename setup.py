from setuptools import setup

with open('requirements.txt') as file:
    requirements = [line.strip() for line in file]

setup(name='zuul_routes_parser',
    version='0.6',
    author='Cezar Pauxis',
    author_email='cezarhpx@gmail.com',
    packages=['zuul_routes_parser'],
    entry_points={
        'console_scripts':[
            'zuul_parse=zuul_routes_parser.__main__:main'
        ]
    },
    install_requires=requirements,
    zip_safe=False)
