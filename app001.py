import flet as ft

def show_screen_1(page, go_next):
    page.clean()
    page.add(
        ft.AppBar(title=ft.Text("APP-001: 회원가입"), bgcolor="green"),
        ft.TextField(label="이름", hint_text="이름을 입력하세요"),
        ft.TextField(label="연락처", hint_text="010-0000-0000"),
        ft.TextField(label="분만예정일", hint_text="YYYY-MM-DD"),
        ft.ElevatedButton("가입 완료 (APP-002로 이동)", on_click=go_next, bgcolor="blue", color="white")
    )
    page.update()