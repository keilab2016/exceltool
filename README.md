# exceltool
学習達成度アンケートの結果出力ツール

## 使い方

1. Templateフォルダにアンケート回答のExcelファイルを置く（ファイル名は2019年度後期_回答データ.xls  2020年度前期_回答データ.xls  2020年度卒業時_回答データ.xlsなど）
2. ```python excel_job.py 学籍番号```
のように実行する。学籍番号はbなしで、複数指定可。
3. outputフォルダに学生ごとのExcelファイルが出力される
