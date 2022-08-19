# exceltool
学習達成度アンケートの結果出力ツール

## 使い方


0. 事前にPython 3をインストールしておく
    - ```pip list``` したときに以下のモジュールがなければ、```pip install``` しておく
      - openopyxl
      - matplotlib
      - pandas
      - xlrd
1. Templateフォルダにアンケート回答のExcelファイルを置く（ファイル名は2019年度後期_回答データ.xls  2020年度前期_回答データ.xls  2020年度卒業時_回答データ.xlsなど）
    - 卒業時以外は、卒業時の回答データを除く過去最大4年分
    - 卒業時は、最新の卒業時の回答データと、それ以外の過去最大4年分
2. ```student-list.txt``` というテキストファイルを作成し、結果を出力したい学生の学籍番号を記入する
    - 卒業時以外は、在籍中の全学部生の学籍番号を、1行に1つずつ（学部3年以下は入学年度ごとに別々に出力させるとよい）
    - 卒業時は、卒業する全学生の学籍番号を、1行に1つずつ
3. ```./all2.sh``` のように実行する
3. outputフォルダに学生ごとのExcelファイルが出力される
