import flet as ft

def show_screen_2(page, go_next, go_back):
    page.clean()
    
    bmi_result = ft.Text("키와 몸무게를 입력하면 BMI가 자동 계산됩니다.", color="gray")
    
    def calculate_bmi(e):
        try:
            if height_input.value and weight_input.value:
                h = float(height_input.value) / 100
                w = float(weight_input.value)
                bmi = w / (h * h)
                
                status = ""
                if bmi < 18.5: status = " (저체중)"; bmi_result.color = "blue"
                elif bmi < 23: status = " (정상)"; bmi_result.color = "green"
                elif bmi < 25: status = " (과체중)"; bmi_result.color = "orange"
                else: status = " (비만)"; bmi_result.color = "red"
                    
                bmi_result.value = f"BMI: {bmi:.1f}{status}"
            else:
                bmi_result.value = "키와 몸무게를 입력하면 BMI가 자동 계산됩니다."
                bmi_result.color = "gray"
        except ValueError:
            bmi_result.value = "숫자만 정확히 입력해주세요."
            bmi_result.color = "red"
        page.update()

    height_input = ft.TextField(label="키 (cm)", on_change=calculate_bmi)
    weight_input = ft.TextField(label="몸무게 (kg)", on_change=calculate_bmi)

    page.add(
        ft.AppBar(title=ft.Text("APP-002: 인적정보"), bgcolor="green"),
        height_input,
        weight_input,
        bmi_result,
        ft.ElevatedButton("다음 단계 (APP-003로 이동)", on_click=go_next, bgcolor="blue", color="white"),
        ft.TextButton("뒤로 가기", on_click=go_back)
    )
    page.update()