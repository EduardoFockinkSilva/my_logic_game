from setuptools import setup, find_packages

setup(
    name='my_logic_game',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'ursina>=0.10.0',
    ],
    entry_points={
        'console_scripts': [
            'logic-game = game.main:main',
        ],
    },
)
