#### 20. JSONデータの読み込み
##### re.compile()
```
prog = re.compile(pattern)
result = prog.match(string)
```
は、以下と同等
```
result = re.match(pattern, string)
```
その式を一つのプログラムで何回も使う場合には、`re.compile()` を使ってその結果の正規表現オブジェクトを再利用した方がより効率的

##### re.search(pattern, string, flags=0)
`re.match()` は文字列の先頭のみにマッチし、各行の先頭にはマッチしない

##### re.match(pattern, string, flags=0)
https://docs.python.jp/3/library/re.html#re.search


#### 22. カテゴリ名の抽出
##### re.match.group()
マッチした1個以上のサブグループを返す。
```
>>> r = re.compile("([a-z]+)=([0-9])"
>>> m = r.search("abc=123&def=456")
>>> m.group(0)    # マッチした部分全て
'abc=1'
>>> m.group(1)    # 1番目のグループ
'abc'
>>> m.group(2)    # 2番目のグループ
'1'
>>> m.group(1, 2) # 複数のグループ
('abc', '1')
>>>
>>> m.groups()    # 全てのグループ
('abc', '1')
```
#### 26. 強調マークアップの除去
##### マークアップ早見表
https://wpdocs.osdn.jp/%E3%83%98%E3%83%AB%E3%83%97:Wiki_%E3%83%9E%E3%83%BC%E3%82%AF%E3%82%A2%E3%83%83%E3%83%97%E6%97%A9%E8%A6%8B%E8%A1%A8

##### 強調マークアップがある行は
```
|確立形態4 = 現在の国号「'''グレートブリテン及び北アイルランド連合王国'''」に変更
```
のみ