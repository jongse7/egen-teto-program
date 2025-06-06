import customtkinter as ctk
from style import BUTTON_FONT, BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_CORNER_RADIUS

#커스텀 버튼 생성 함수, 인자에 따라 스타일과 상태를 조정할 수 있습니다.

def button(root, text, command, fg_color=None, hover_color=None, state=None):
    return ctk.CTkButton(
        root,
        text=text,
        width=BUTTON_WIDTH,
        height=BUTTON_HEIGHT,
        corner_radius=BUTTON_CORNER_RADIUS,
        font=BUTTON_FONT,
        command=command,
        fg_color=fg_color,
        hover_color=hover_color,
        state=state
    )