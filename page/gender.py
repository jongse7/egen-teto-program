# 성별 선택 페이지 함수입니다.

import customtkinter as ctk
from style import LABEL_FONT
import state
from utils import page_set, create_center_frame
from components.button import button
from style import PINK_COLOR, PINK_HOVER_COLOR

def show_gender_page(root, to_next_page):
    # 기존 위젯 제거
    page_set(root)

    # 가운데 정렬 프레임 생성
    center_frame = create_center_frame(root)

    # 안내 문구 + 버튼 모두 center_frame 안에 넣기
    label = ctk.CTkLabel(center_frame, text="성별을 선택해주세요.", font=LABEL_FONT)
    label.pack(pady=(0, 40))

    # 버튼 클릭 시 실행할 함수
    def select_gender(gender):
        state.selected_gender = gender
        to_next_page()

    # 남자 버튼
    male_button = button(center_frame, text="남자", command=lambda: select_gender("남자"))
    male_button.pack(pady=10)

    # 여자 버튼
    female_button = button(center_frame, text="여자", command=lambda: select_gender("여자"),
                           fg_color=PINK_COLOR, hover_color=PINK_HOVER_COLOR)
    female_button.pack(pady=10)
