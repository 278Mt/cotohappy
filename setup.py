from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cotohappy',
    packages=['cotohappy'],

    version='0.0.1',

    license='MIT',

    install_requires=['json', 'requests'],

    author='278Mt', # パッケージ作者の名前
    author_email='278mt.l.meitner@gmail.com', # パッケージ作者の連絡先メールアドレス

    url='https://github.com/278mt/cotohappy', # パッケージに関連するサイトのURL(GitHubなど)

    description='Cotoha API, created by NTT Communications Corporation, for Python'
    long_description=long_description,
    long_description_content_type='text/markdown'
    keywords='cotohappy CotohapPy cotoha library', # PyPIでの検索用キーワードをスペース区切りで指定

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
    ],
)
