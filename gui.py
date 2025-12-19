from __future__ import annotations

import threading
import tkinter as tk
from tkinter import filedialog, messagebox
from dataclasses import dataclass
from typing import Optional

def wait_for_export_button() -> bool:
    """
    GUIを表示して、[出力]ボタンが押されたら True を返す。
    それ以外（×で閉じる等）は False を返す。
    """
    result = {"ok": False}

    root = tk.Tk()
    root.title("XLSX 出力指示")
    root.geometry("360x180")

    label = tk.Label(root, text="XLSXを出力する場合はボタンを押してください。")
    label.pack(pady=18)

    def on_export():
        result["ok"] = True
        root.destroy()  # mainloopを終了させる

    def on_close():
        # ×で閉じた場合は False のまま終了
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)

    btn = tk.Button(root, text="出力", command=on_export, height=2, width=12)
    btn.pack(pady=10)

    root.mainloop()
    return result["ok"]


if __name__ == "__main__":
    ok = wait_for_export_button()
    print(ok)  # 出力ボタンなら True, ×なら False
