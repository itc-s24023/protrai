#GUIで動くアプリを作ってみよう

import tkinter as tk #まずこの行を書く必要があるよ

root = tk.Tk() #初めのおまじない

root.geometry("400x300") #ウィンドウズのサイズを決める 
root.title("ハローアプリ") #ウィンドウのタイトルを決める
lbl = tk.Label(text="こんにちは世界") #いつもの
lbl.pack() #lblを配置させる必要がある


root.mainloop() #終わりのおまじない
