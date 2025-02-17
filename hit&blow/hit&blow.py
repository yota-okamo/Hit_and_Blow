import tkinter as tk
import tkinter.ttk as ttk
import random
from collections import Counter



COUNT = 5   #手数
NUMBER = 4  #答えの文字数
ANSWER = "" #答え
WIDTH = 300
HEIGHT = 400

#ポップアップウィンドウの表示
def show_popup(text):
    popup = tk.Toplevel()
    popup.title("Popup")
    popup.geometry("200x100")
    
    # ポップアップウィンドウが表示されている間に、メインウィンドウの操作を無効化する
    popup.grab_set()

    label = tk.Label(popup, text=text)
    label.pack(pady=20)

    close_button = tk.Button(popup, text="Close", command=lambda: close_popup(popup))
    close_button.pack(pady=10)

def close_popup(popup):
    popup.grab_release()  # メインウィンドウの操作を再度有効化
    for widget in right_frame.winfo_children():
        widget.destroy()
    
    
    popup.destroy()

def on_Click(frame):
    input_text = entry.get()
    global COUNT
    global ANSWER

    if(input_text != "" and len(input_text)==4):
        hit, blow = HB_num(ANSWER, input_text)
        label = tk.Label(frame, text=input_text+f"hit：{hit}/blow：{blow}")
        label.pack()
        entry.delete(0, tk.END)
        COUNT -= 1
        count_label.config(text=f"残り手数：{COUNT}")
    
    if(hit == 4):
        show_popup("Clear!!")

    if(COUNT == 0 and hit != 4):
        show_popup("Miss")

def on_Clear_Button():
    entry.delete(0, tk.END)
    

def on_key(event):
    if event.keysym in ["BackSpace", "Deliete"]:
        return
    if not event.char.isdigit():
        return "break"
    
#ランダムの4つの数字を出す
def create_answer():
    global NUMBER

    digits = list(range(10))
    ans = random.sample(digits, NUMBER)

    return "".join(map(str, ans))

#ヒットとブローの数をカウント
def HB_num(ans, inter):
    hit = 0
    blow = 0

    blow_ans = []
    blow_inter = []

    for i in range(4):
        if(ans[i] == inter[i]):
            hit+=1
        else:
            blow_ans.append(ans[i])
            blow_inter.append(inter[i])

    counter_ans = Counter(blow_ans)
    counter_inter = Counter(blow_inter)

    common_chars = counter_ans & counter_inter

    for _, count in common_chars.items():
        blow += count

    return hit, blow

#難易度選択画面の生成
def create_defficulty(root):
    frame = tk.Frame(root, width=WIDTH, height=HEIGHT, bg="lightblue")
    frame.pack()

    #スタートボタン，手数入力ボタン，桁数入力ボタン


#メインウィンドウ定義
root = tk.Tk()
root.title("Hit&Blow")
root.geometry(f'{WIDTH}x{HEIGHT}')

#答えの初期セット
ANSWER = create_answer()

#右フレームの作成
right_frame = tk.Frame(root, width=150, height=400, bg="white")
right_frame.pack(side="right", fill="both", expand=True)
right_frame.pack_propagate(False)


#左フレームの作成
left_frame = tk.Frame(root, width=150, height=400, bg="lightgreen")
left_frame.pack(side="left", fill="both", expand=True)
left_frame.pack_propagate(False)


#左フレーム内のウィジェット
count_label = tk.Label(left_frame, text=f"残り手数：{COUNT}", font=(16), bg="lightgreen")
count_label.grid(row=0, column=0, columnspan=2, padx=35, pady=10)

entry = tk.Entry(left_frame)
entry.grid(row=1, columnspan=2, pady=10)
entry.bind("<Key>", on_key)


button = tk.Button(left_frame, text="チェック", command=lambda: on_Click(right_frame))
button.grid(row=2, column=0, padx=5, pady=10)

clear_button = tk.Button(left_frame, text="クリア", command=on_Clear_Button)
clear_button.grid(row=2, column=1, padx=5, pady=10)

left_frame.pack_forget()
right_frame.pack_forget()

create_defficulty(root)

root.mainloop()