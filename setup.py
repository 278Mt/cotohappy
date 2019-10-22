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

    install_requires=['requests', 'json'],

    author='278Mt', # パッケージ作者の名前
    author_email='278mt.l.meitner@gmail.com', # パッケージ作者の連絡先メールアドレス

    url='https://github.com/278mt/cotohappy', # パッケージに関連するサイトのURL(GitHubなど)

    description='To translate Japanese sentences into Son Goku accent.', # パッケージの簡単な説明
    long_description=long_description, # PyPIに'Project description'として表示されるパッケージの説明文
    long_description_content_type='text/markdown' # long_descriptionの形式を'text/plain', 'text/x-rst', 'text/markdown'のいずれかから指定
    keywords='gokulang goku-lang', # PyPIでの検索用キーワードをスペース区切りで指定

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ], # パッケージ(プロジェクト)の分類。https://pypi.org/classifiers/に掲載されているものを指定可能。
)
