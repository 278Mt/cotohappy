from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cotohappy',
    packages=['cotohappy'],

    version='0.4.0',

    license='MIT',

    install_requires=['requests'],

    author='278Mt',
    author_email='278mt.l.meitner@gmail.com',

    url='https://github.com/278mt/cotohappy',

    description='Cotoha API, created by NTT Communications Corporation, for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='cotohappy CotohapPy cotoha library',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
    ],
)
