#### 20
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