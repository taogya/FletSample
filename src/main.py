import os
import threading
import time

import flet as ft


def main(page: ft.Page):
    # タイトルの設定
    page.title = "Flet Sample"
    # ページの配置を中央に設定
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # チャートに表示するデータ
    data_points = [
    ]
    # チャートに表示するシリーズの設定
    data_series = [
        ft.LineChartData(
            data_points=data_points,
            stroke_width=5,
            color=ft.colors.CYAN,
            curved=True,
            stroke_cap_round=True,
        )
    ]
    # チャートの設定
    chart = ft.LineChart(
        data_series=data_series,
        border=ft.border.all(3, ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE)),
        horizontal_grid_lines=ft.ChartGridLines(
            interval=1, color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE), width=1
        ),
        vertical_grid_lines=ft.ChartGridLines(
            interval=1, color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE), width=1
        ),
        left_axis=ft.ChartAxis(
            labels_size=48,
        ),
        bottom_axis=ft.ChartAxis(
            labels_size=32,
        ),
        tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLUE_GREY),
        min_y=0,
        max_y=100,
        expand=True,
    )

    # チャートをクリアする
    def clear_chart(e):
        data_points.clear()
        chart.update()

    # ページにコンポーネントを追加
    page.add(
        ft.Row(
            controls=[
                chart,
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            controls=[
                ft.FilledButton(text="Clear", on_click=clear_chart, expand=True),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    # 温度を取得する
    def get_temperature():
        try:
            temp = os.popen("vcgencmd measure_temp").readline()
            temperature = float(temp.replace("temp=", "").replace("'C\n", ""))
            return temperature
        except BaseException:
            # エラーが発生した場合はランダムな値を返す
            import random
            return random.randint(0, 40)

    # チャートを更新する
    def update_chart():
        while True:
            data_points.append(ft.LineChartDataPoint(x=len(data_points), y=get_temperature()))
            chart.update()
            time.sleep(1)

    # チャートを更新するスレッドを開始
    th = threading.Thread(target=update_chart)
    th.start()


# アプリの起動
ft.app(target=main)