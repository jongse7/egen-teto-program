# 전체 설문 플로우를 정의하는 메인 실행 파일입니다.

import customtkinter as ctk
from page.init import show_init_page
from page.gender import show_gender_page
from page.question import show_question_page
from page.result import show_result_page
from const import question_parts

# customtkinter 테마 설정
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# 창 설정
root = ctk.CTk()
root.title("TEP")

# 원하는 창 크기
window_width = 800
window_height = 720

# 화면 크기 가져오기
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 가운데 위치 계산
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# 창 크기 + 위치 설정
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# 현재 페이지 인덱스 (질문 페이지용)
question_page_index = 0

# 페이지 전환 함수들
def to_gender_page():
    show_gender_page(root, to_question_page)

def to_question_page():
    global question_page_index
    if question_page_index < len(question_parts):
        show_question_page(root, question_page_index, to_question_page)
        question_page_index += 1
    else:
        show_result_page(root)

# 첫 페이지 호출
show_init_page(root, to_gender_page)

# 루프 시작
root.mainloop()
