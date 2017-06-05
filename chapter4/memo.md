##### mecab のインストール
```
Mecabと辞書のインストール
$ brew install mecab
$ brew install mecab-ipadic

Mecab-python3 をインストール
$ pip install mecab-python3
```

##### mecab の使い方
```
インスタンス化
$ mecab = MeCab.Tagger('-Ochasen')

parseする
$ mecab.parse(hoge.txt)
```


##### 事前準備
『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，その結果をneko.txt.mecabというファイルに保存せよ．
initialize.py に記述

参考URL: http://qiita.com/taroc/items/b9afd914432da08dafc8


##### 30
出力は一文を形態素のリストとしたもの。
一文目は以下の通り。
```
[{'surface': '一', 'pos1': '数', 'base': '一', 'pos': '名詞'}, {'surface': '\u3000', 'pos1': '空白', 'base': '\u3000', 'pos': '記号'}, {'surface': '
吾輩', 'pos1': '代名詞', 'base': '吾輩', 'pos': '名詞'}, {'surface': 'は', 'pos1': '係助詞', 'base': 'は', 'pos': '助詞'}, {'surface': '猫', 'pos1':
 '一般', 'base': '猫', 'pos': '名詞'}, {'surface': 'で', 'pos1': '*', 'base': 'だ', 'pos': '助動詞'}, {'surface': 'ある', 'pos1': '*', 'base': 'ある
', 'pos': '助動詞'}, {'surface': '。', 'pos1': '句点', 'base': '。', 'pos': '記号'}]
```

##### 31
