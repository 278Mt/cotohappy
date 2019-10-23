

CotohapPy: Cotoha for Python
=========

CotohapPy (Japanese: コトハッピー) is for connecting to [Cotoha](https://api.ce-cotoha.com/contents/), one of the Japanese morphological analysis engines, and is for reshaping the response more readably.

Installation
------------

The easiest way to install the latest version is by using pip/easy_install to pull it from PyPI:

```bash
pip install cotohappy
```

You may also use Git to clone the repository from GitHub and install it manually:

```bash
git clone https://github.com/278Mt/cotohappy.git
cd cotohappy
python setup.py install
```

Python 3.7 and 3.8 are supported (frequently updated).

Requirements
------------

* json
* requests

Usage
-----

This is one of the examples.

```python
import cotohappy

coy = cotohappy.API()   # created instance of CotohapPy

print('\n#### parse origin ####')
sentence = '犬は歩く。'
type_    = 'default'
parse_li = coy.parse(sentence, type_)
for parse in parse_li:
    print(parse)

print(parse.key_name)

print('\n#### parse tokens ####')
for parse in parse_li:
    for token in parse.tokens:
        print(token)
        
print(token.key_name)
```

Output:

```
#### parse origin ####
犬は	 0,1,D,0,1
歩く。	 1,-1,O,0,1
form     id,head,dep,chunk_head,chunk_func

#### parse tokens ####
犬	 0,イヌ,犬,名詞,*,*,*,*,*
は	 1,ハ,は,連用助詞,*,*,*,*,*
歩	 2,アル,歩く,動詞語幹,K,*,*,*,*
く	 3,ク,く,動詞接尾辞,終止,*,*,*,*
。	 4,,。,句点,*,*,*,*,*
form     id,kana,lemma,pos,features[:5]
```



Please chek details on [examples](https://github.com/278Mt/cotohappy/tree/master/examples).
