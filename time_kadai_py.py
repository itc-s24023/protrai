# s24023
# 　実行が確認出来たら時間を表示させる「時計アプリ」を作ってみたいと思います
#　時計アプリはモジュールを「time_kadai_py」を作成します
#　時計アプリを使いやすくバージョンアップしていきます

import datetime
import tkinter as tk

# 時間を処理する部分を関数で実装
def update_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%Y年%m月%d日 %H時%M分%S秒")
    #
    lbl.config(text=current_time)
    root.after(1000,update_time)

# TKinterのウィンドウを作成
root = tk.Tk()#初めのおまじない

root.title("現在の時刻")

lbl = tk.Label()
lbl.config(text="", font=("Helvetica", 20))
lbl.pack()

# 関数の呼び出し
update_time()


root.mainloop() # 終わりのおまじない
