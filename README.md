

CotohapPy: Cotoha for Python
=========

[![Downloads](https://pepy.tech/badge/cotohappy)](https://pepy.tech/project/cotohappy)
[![Downloads](https://pepy.tech/badge/cotohappy/month)](https://pepy.tech/project/cotohappy/month)
[![Downloads](https://pepy.tech/badge/cotohappy/week)](https://pepy.tech/project/cotohappy/week)

CotohapPy (Japanese: コトハッピー) is for connecting to [Cotoha API](https://api.ce-cotoha.com/contents/), one of the Japanese morphological analysis engines, and is for reshaping the response more readably.

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

```bash
├── payload.json
└── sjgyoen.py
```

JSON preperation (`payload.json`):

```json
{
  "AccessTokenPublishURL": "https://api.ce-cotoha.com/v1/oauth/accesstokens",
  "APIBaseURL"           : "https://api.ce-cotoha.com/api/dev/",
  "ClientId"             : "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456",
  "ClientSecret"         : "7890abcdefghijkl"
}
```

Programme (`sjgyoen.py`)

```python
import cotohappy
import requests
from bs4 import BeautifulSoup


def get_kotonoha_story():
    
    url = 'https://www.kotonohanoniwa.jp/page/product.html'
    res = requests.get(url)

    soup = BeautifulSoup(res.content, 'html.parser')
    p = soup.find_all('p', class_='mb24')[-1]

    return p.text


if __name__ == '__main__':

    coy = cotohappy.API()

    """ getting parse """
    print('\n#### parse origin ####')
    sentence = get_kotonoha_story()
    kuzure   = False
    parse_li = coy.parse(sentence, kuzure)
    for parse in parse_li:
        print(parse)

    print(parse.key_name)

    """ getting tokens; it is a little more difficult than MeCab Janome """
    print('\n#### parse tokens ####')
    for parse in parse_li:
        for token in parse.tokens:
            print(token)

    print(token.key_name)

    """ if you extract just nouns, you write: """
    print('\n#### extract nouns ####')
    nouns: [str] = []
    for parse in parse_li:
        for token in parse.tokens:
            if token.pos == '名詞':
                nouns.append(token.form)

    print(nouns)
    
```

Output:

```
#### parse origin ####
靴職人を	 0,1,D,1,2
目指す	 1,2,D,0,1
高校生・タカオは、	 2,51,D,2,3
雨の	 3,4,D,0,1
朝は	 4,7,D,0,1
...
互いの	 47,48,D,0,1
思いを	 48,51,D,0,1
よそに	 49,51,D,0,1
梅雨は	 50,51,D,0,1
明けようとしていた。	 51,-1,O,0,6
form	 id,head,dep,chunk_head,chunk_func

#### parse tokens ####
靴	 0,クツ,靴,名詞,*,*,*,*,*
職人	 1,ショクニン,職人,名詞,*,*,*,*,*
を	 2,ヲ,を,格助詞,連用,*,*,*,*
目指	 3,メザ,目指す,動詞語幹,S,*,*,*,*
す	 4,ス,す,動詞接尾辞,連体,*,*,*,*
...
し	 148,シ,し,動詞活用語尾,*,*,*,*,*
て	 149,テ,て,動詞接尾辞,接続,連用,*,*,*
い	 150,イ,いる,動詞語幹,A,Lて連用,*,*,*
た	 151,タ,た,動詞接尾辞,終止,*,*,*,*
。	 152,,。,句点,*,*,*,*,*
form	 id,kana,lemma,pos,features[:5]

#### extract nouns ####
['靴', '職人', '高校生', 'タカオ', '雨', '朝', '学校', '公園', '日本', '庭園', '靴', 'スケッチ', 'ある日', 'タカオ', 'ひとり', '缶', 'ビール', '年上', '女性', 'ユキノ', 'ふたり', '約束', '雨', '日', '逢瀬', '心', '居場所', 'ユキノ', '彼女', '靴', 'タカオ', '六月', '空', '揺れ', '互い', '思い', 'よそ', '梅雨']
```

Please check details on [examples](https://github.com/278Mt/cotohappy/tree/master/examples).

Whats's new?
------------

### 0.4.1, 0.4.2

Partial errors elimination.

### 0.4.0

`kuzure` and `default` become `kuzure=True` and `kuzure=False` 

### 0.3.6, 0.3.7

Partial errors elimination.

### 0.3.5

In version 0.3.5, you can choose translating mode: for example, "information-seeking" in sentence type, to "情報獲得".

### 0.3.4

In version 0.3.4, you can use technical term dictionaries on parse, named entity extraction, keyword extraction and similarity calculation. However, I, origin master of CotohapPy, cannot use nor examine the mode because I use Cotoha API for Developer, not for Enterprise. I want for Academic.
