from setuptools import setup

setup(
    name='screenplay',
    version='0.1.0',
    description='Count words in TV shows',
    entry_points={
        'console_scripts': ['swc=screenplay.main:main']
    },
)
