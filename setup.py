from setuptools import setup


setup(
    name='lyrica',
    version='1.3.4',
    install_requires=[
        'requests',
        'bs4'
    ],
    packages=[
        'lyrica'
    ],
    entry_points={
        'console_scripts': [
            'lyrica = lyrica.bin:run'
        ]
    }
)
