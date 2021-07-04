import tkinter as tk

class Application(tk.Frame):
    # メインWindow2を取得する関数
    def getMainWindow(self):
        mainWindow2 = tk.Tk()
        # メインWindow2へタイトルをつける。
        mainWindow2.title('mainWindow2')
        # Window(メインWindow2)の画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        mainWindow2.geometry("300x200+420+0")

    # サブWindowを取得する関数
    def getSubWindow(self):
        # subWindowをグローバル変数とする。
        # global subWindow
        # subWindowがNoneもしくはsubWindow(サブWindow)が存在しない場合
        # winfo_exists() : サブWindowが存在するのか判定する関数。True(サブWindowが存在する), False(サブWindowが存在しない)が返されます。
        # if subWindow == None or not subWindow.winfo_exists():

        # メインWindowに紐づくサブWindowを作成する。
        subWindow = tk.Toplevel()
        # サブWindowへタイトルをつける。
        subWindow.title('subWindow')
        # Window(サブWindow)の画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        subWindow.geometry("300x200+420+0")

        # subWindow(サブWindow)を親要素として、Button Widgetを作成する。
        # text : テキスト情報
        # command : ボタンを選択した場合に、実行する関数を設定。self.getSubWindowとする。
        # Buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
        button = tk.Button(subWindow, text='button', command=self.getSubWindow)
        # subWindow(サブWindow)を親要素とした場合に、Button Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        button.pack()

    def __init__(self, master=None):
        # メインWindow1の初期設定を行う。
        super().__init__(master)
        # メインWindow1へタイトルをつける。
        self.master.title("mainWindow1")
        # Window(メインWindow1)の画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("300x200+120+0")

        # self.getMainWindow()
        self.getSubWindow()

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    root = tk.Tk()

    # subWindowに関する変数の初期化
    # subWindow = None

    app = Application(master=root)

    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
