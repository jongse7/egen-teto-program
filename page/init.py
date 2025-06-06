# 설문 시작 페이지 함수입니다.

import customtkinter as ctk
from style import LABEL_FONT, BUTTON_FONT, BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_CORNER_RADIUS
from utils import page_set
from utils import create_center_frame

def show_init_page(root, next_page_callback):
    # 기존 위젯 제거
    page_set(root)

    # 가운데 정렬 프레임 생성
    center_frame = create_center_frame(root)

    # 안내 문구
    label = ctk.CTkLabel(center_frame, text="나는 에겐일까? 테토일까?\n시작하려면 아래 버튼을 눌러주세요.", font=LABEL_FONT)
    label.pack(pady=40)

    # 시작 버튼
    start_button = ctk.CTkButton(
        center_frame,
        text="시작하기",
        width=BUTTON_WIDTH,
        height=BUTTON_HEIGHT,
        corner_radius=BUTTON_CORNER_RADIUS,
        font=BUTTON_FONT,
        command=next_page_callback  # 다음 페이지로 이동하는 콜백 함수
    )
    start_button.pack(pady=20)