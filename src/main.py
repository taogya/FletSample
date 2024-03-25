import os
import threading
import time

import flet as ft

X_LEN = 60


def main(page: ft.Page):
    # タイトルの設定
    page.title = 'Flet Sample'
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
        tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.WHITE),
        min_y=30,
        max_y=80,
        min_x=0,
        max_x=X_LEN,
        expand=True,
    )

    # チャートをクリアする
    count = 0
    def clear_chart(e):
        count = 0
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
                ft.FilledButton(text='Clear', on_click=clear_chart, expand=True),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    # 温度を取得する
    def get_temperature():
        try:
            temp = os.popen('vcgencmd measure_temp').readline()
            temperature = float(temp.replace('temp=', '').replace('\'C\n', ''))
            return temperature
        except BaseException:
            # エラーが発生した場合はランダムな値を返す
            import random
            return random.randint(0, 40)

    # チャートを更新する
    def update_chart():
        while True:
            data_points.append(ft.LineChartDataPoint(x=count, y=get_temperature()))
            if len(data_points) > X_LEN:
                data_points.pop(0)
            count += 1
            chart.min_x = max(0, count - X_LEN)
            chart.max_x = max(count, X_LEN)
            chart.update()
            time.sleep(1)

    # チャートを更新するスレッドを開始
    th = threading.Thread(target=update_chart)
    th.start()


if __name__ == '__main__':
    from argparse import ArgumentParser

    # コマンドライン引数のパース
    parser = ArgumentParser()
    parser.add_argument('--host', type=str, default=None)
    parser.add_argument('--port', type=int, default=0)
    args = parser.parse_args()

    # アプリのビューを設定(host が指定されている場合はブラウザで開く)
    view = ft.AppView.FLET_APP if not args.host else ft.AppView.WEB_BROWSER

    # アプリの起動
    ft.app(target=main, host=args.host, port=args.port, view=view)
