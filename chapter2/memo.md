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
sed -e 's/hoge/huga/g' ./file.txt 

# 1から5行目を削除
sed -e 1,5d
# 1から5行目以外を削除
sed -e '1,5!d'
```

### tr コマンド
文字の置換や削除などを行うコマンド
tr は特定の1文字を別の1文字に置換する処理

参照: https://hydrocul.github.io/wiki/commands/tr.html

### expand コマンド
ファイルのタブをスペースに置き換えて出力するコマンド

参照: https://codezine.jp/unixdic/w/expand

```
# file.txt のタブを n (数字) こ分のスペースに置換する
expand -t n file.txt
```