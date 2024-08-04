#24023 entry_kadai.py
#エントリーウィジェット標準入力で受けた金額の税込み(10%)価格として出力するプログラム

import tkinter as tk # tkinterをtkと略して使う

def dispLabel():
    a = entry.get()
    print(f"aは{type(a)}")#ログの入力
    a = int(input())
    lbl.config(text=f"税込み{a*1.1}円です")

root = tk.Tk()
root.title("エントリーウィジェット")
root.geometry("400x200")#画面の大きさを決める

lbl = tk.Label(text="ラベル",font=("Helvetica",20))
entry = tk.Entry(font=("Helvetica",20))
btn = tk.Button(text="ボタン", font=("Helvetica",20), command=dispLabel)

lbl.pack()
entry.pack()
btn.pack()

tk.mainloop()
