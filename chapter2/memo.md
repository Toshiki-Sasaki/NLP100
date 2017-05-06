### 11. タブをスペースに置換
#### sed コマンド
文字列の全置換，行単位の抽出，削除など様々なテキスト処理を行うコマンド

参照: https://hydrocul.github.io/wiki/commands/sed.html
 - -e : 処理の指定
 - s : 置換 s
   - 's/hoge/huga'
   - hoge を huga に置換
 - g : 繰り返し (vimと同じ)
 - d : 行の削除

例）
```
# file.txtのhoge を huga に置換
$ sed -e 's/hoge/huga/g' ./file.txt 

# 1から5行目を削除
$ sed -e 1,5d
# 1から5行目以外を削除
$ sed -e '1,5!d'
```

#### tr コマンド
文字の置換や削除などを行うコマンド
tr は特定の1文字を別の1文字に置換する処理

参照: https://hydrocul.github.io/wiki/commands/tr.html

#### expand コマンド
ファイルのタブをスペースに置き換えて出力するコマンド

参照: https://codezine.jp/unixdic/w/expand

```
# file.txt のタブを n (数字) こ分のスペースに置換する
$ expand -t n file.txt
```

### 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
#### cut コマンド
タブ区切りでフィールドを選択して出力する、または各行の中の一部を範囲指定して出力するコマンド

参照: https://hydrocul.github.io/wiki/commands/cut.html

```
# タブ区切りで最初の列と3列目だけを抽出して、タブ区切りで出力する
$ cut -f1,3 foo.txt

#フィールドの区切りをタブではなくスペースにする
$ cat foo.txt | cut -d' ' -f1,3
```

### 13. col1.txtとcol2.txtをマージ
#### read() と readlines() と readline()
read() 改行文字を含み，テキスト全体を一気に読み込む
readlines() 改行文字を含み，行ごとに処理する?
readline() 改行文字を含み，行ごとに処理する?

#### paste コマンド
複数のファイルを行単位に連結して標準出力に出力するコマンド

参照: http://itdoc.hitachi.co.jp/manuals/3021/3021313320/JPAS0332.HTM

### 14. 先頭からN行を出力
#### head コマンド
ファイル内容の先頭部分を表示するコマンド
```
# 先頭からn行を表示
$ head -n N ./file.txt
```

### 15. 末尾のN行を出力
#### tail コマンド
テキスト入力の最後のn行を抜き出すコマンド
使い方は`head`と同じ

### 16. 
#### split コマンド
```
# testファイルを2行ごとに切り出し，"out."で始まるファイルに順次書き出す
$ split -l 2 test out.
```

### 17. １列目の文字列の異なり
#### 