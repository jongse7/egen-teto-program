# 설문 시작 페이지 함수입니다.

import customtkinter as ctk
from style import LABEL_FONT
from utils import page_set
from utils import create_center_frame
from components.button import button

def show_init_page(root, to_next_page):
    # 기존 위젯 제거
    page_set(root)

    # 가운데 정렬 프레임 생성
    center_frame = create_center_frame(root)

    # 안내 문구
    label = ctk.CTkLabel(center_frame, text="나는 에겐일까? 테토일까?\n시작하려면 아래 버튼을 눌러주세요.", font=LABEL_FONT)
    label.pack(pady=40)

    # 시작 버튼(컴포넌트 사용용)
    start_button = button(
        center_frame,
        text="시작하기",
        command=to_next_page
        )
    start_button.pack(pady=20)
    
    # 시작 버튼(컴포넌트 미사용)
    # start_button = ctk.CTkButton(
    #     center_frame,
    #     text="시작하기",
    #     width=BUTTON_WIDTH,
    #     height=BUTTON_HEIGHT,
    #     corner_radius=BUTTON_CORNER_RADIUS,
    #     font=BUTTON_FONT,
    #     command=to_next_page
    # )
    # start_button.pack(pady=20)


