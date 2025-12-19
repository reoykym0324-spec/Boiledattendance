from openpyxl import Workbook
from gui1 import wait_for_export_button


def main():
    # 保存したい配列
    data = [
        [1, 2, 3],
        ["a", "b", "c"],
        [4.5, 6.7, 8.9]
    ]

    wb = Workbook()
    ws = wb.active

    for row in data:
        ws.append(row)

    # ===== GUI を表示，出力指示を待つ =====
    ok = wait_for_export_button()

    # ===== GUI の結果に応じて処理 =====
    if ok:
        wb.save("output.xlsx")
        print("output.xlsx を保存しました")
    else:
        print("出力はキャンセルされました")


if __name__ == "__main__":
    main()
