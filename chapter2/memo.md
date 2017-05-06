### 11. タブをスペースに置換
#### sed コマンド
文字列を全置換したり、行単位で抽出したり、削除したり、いろいろなテキスト処理のできるコマンド

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
read() は改行文字を含まず，テキスト全体を一気に読み込む
readlines() は改行文字を含み，テキスト全体を一気に読み込む
readline() は改行文字を含み，一行ごとに読み込む
