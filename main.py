import flet as ft
import app001
import app002

def main(page: ft.Page):
    page.title = "맘스세이프 산모 앱"

    def show_screen_3(go_next, go_back):
        page.clean()
        
        # 1. 3번 화면에 들어왔을 때만 파일 선택기 생성
        file_picker = ft.FilePicker()
        selected_files = ft.Text("선택된 파일이 없습니다.", color="gray")
        
        def on_dialog_result(e: ft.FilePickerResultEvent):
            if e.files:
                selected_files.value = f"업로드 완료: {e.files[0].name}"
                selected_files.color = "blue"
            else:
                selected_files.value = "업로드가 취소되었습니다."
                selected_files.color = "red"
            page.update()
            
        file_picker.on_result = on_dialog_result
        
        # 2. 오버레이에 추가 (여기서만 추가됨) 
        upload_box = ft.Container(
            content=ft.Column(
                [
                    ft.Text("이 박스를 클릭하여 진단서(이미지)를 선택하세요", weight="bold"),
                    selected_files
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            width=400,
            height=200,
            bgcolor="lightblue",
            border_radius=10,
            on_click=lambda _: file_picker.pick_files(allow_multiple=False)
        )

        page.add(
            ft.AppBar(title=ft.Text("APP-003: 진료정보입력"), bgcolor="orange"),
            upload_box,
            ft.Divider(),
            ft.ElevatedButton("다음 단계 (APP-004)", on_click=go_next, bgcolor="blue", color="white"),
            ft.TextButton("뒤로 가기", on_click=go_back)
        )
        page.update()

    # 화면 이동 함수들 (다른 화면으로 갈 때는 오버레이를 싹 비워줍니다)
    def go_to_screen_1(e=None): 
        page.overlay.clear() 
        app001.show_screen_1(page, go_next=go_to_screen_2)
        
    def go_to_screen_2(e=None): 
        page.overlay.clear()
        app002.show_screen_2(page, go_next=lambda _: show_screen_3(go_to_screen_4, go_to_screen_2), go_back=go_to_screen_1)
        
    def go_to_screen_4(e=None): 
        page.clean()
        page.overlay.clear()
        page.add(ft.AppBar(title=ft.Text("APP-004: 홈 대시보드"), bgcolor="blue"), ft.Text("결과 표시 화면"))
        page.update()

    # 앱 시작
    go_to_screen_1()

if __name__ == "__main__":
    ft.app(target=main)