# TiddlyWiki Builder

## 概要

完全個人用。単一ファイル版のTiddlyWikiでの，静的サイト作成，及びサイトマップ作成までの手順を自動化します。TiddlyWiki Builderとかそれらしい名前がついているが，ただ作業を自動化しただけ・・・

## 要件

- python3，Node，npm，tiddlywikiがインストール済みであること
- macOSでの動作を想定
  - 他のOSで動作するかは未確認

### 動作確認済みの環境

- Python v3.9.6
- Node v18.13.0
- npm v8.19.3
- tiddlywiki v5.3.0

## 使用法

### TW5-sitemapの用意・設定

dullroar氏作成の[TW5-sitemap](https://github.com/dullroar/TW5-sitemap)をダウンロードし，`sitemap`ディレクトリを`build.sh`，`init.sh`がと同じディレクトリにコピーする。  
サイトマップの設定は，[TW5-sitemap](https://github.com/dullroar/TW5-sitemap)のREADMEを確認していただきたい。

### tiddlywikiを初期化

`sh init.sh`

### 単一html版のTiddlyWikiをインポート

コンソールに表示されたアドレスにアクセスし，サイドバーの「Tools」タブの「import」ボタンを押下し，静的サイト化したいhtmlファイルを選択する。インポート後，コンソールに戻り，control+cでサーバを終了する。

### ビルド  

`sh build.sh`

2つのshファイルを実行後，新たに作成された`myfirstwiki/output/`ディレクトリ内に，サイトマップとHTMLファイルが生成されているはず。
