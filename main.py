import flet as ft
# 우리가 만든 파일들을 불러옵니다.
import app001
import app002

def main(page: ft.Page):
    page.title = "맘스세이프 산모 앱"

    # 1번 화면으로 이동하는 함수
    def go_to_screen_1(e=None):
        app001.show_screen_1(page, go_next=go_to_screen_2)

    # 2번 화면으로 이동하는 함수
    def go_to_screen_2(e=None):
        app002.show_screen_2(page, go_next=go_to_screen_3, go_back=go_to_screen_1)

    # 3번 화면으로 이동하는 함수 (아직 분리 안 함)
    def go_to_screen_3(e=None):
        page.clean()
        page.add(
            ft.AppBar(title=ft.Text("APP-003: 진료정보입력"), bgcolor="orange"),
            ft.Text("진단서 OCR 트랙 및 직접 입력 탭이 들어갈 자리입니다.", size=16),
            ft.ElevatedButton("다음 단계 (APP-004로 이동)", on_click=go_to_screen_4, bgcolor="blue", color="white"),
            ft.TextButton("뒤로 가기", on_click=go_to_screen_2)
        )
        page.update()

    # 4번 화면으로 이동하는 함수 (아직 분리 안 함)
    def go_to_screen_4(e=None):
        page.clean()
        page.add(
            ft.AppBar(title=ft.Text("APP-004: 홈 대시보드"), bgcolor="blue"),
            ft.Text("위험도 배지 및 증상일기 메뉴가 들어갈 자리입니다.", size=16),
            ft.TextButton("처음으로 돌아가기", on_click=go_to_screen_1)
        )
        page.update()

    # 앱 시작 시 1번 화면 띄우기
    go_to_screen_1()

ft.app(main)

# test 
