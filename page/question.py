# 질문 페이지 함수입니다.

import customtkinter as ctk
from const import questions, question_parts
from style import LABEL_FONT, QUESTION_FONT, CHOICE_FONT
import state
from utils import page_set
from components.button import button

def show_question_page(root, page_index, to_next_page):
    # 기존 위젯 제거
    page_set(root)

    QUESTIONS_PER_PAGE = 10
    start_index = page_index * QUESTIONS_PER_PAGE
    end_index = start_index + QUESTIONS_PER_PAGE

    # 사용자의 선택을 저장할 리스트 (10문항 각각에 대해 1~5 선택값 저장)
    selected_values = [ctk.IntVar(value=0) for _ in range(QUESTIONS_PER_PAGE)]

    # 스크롤 가능한 프레임 생성 (질문과 선택지를 담음)
    question_frame = ctk.CTkScrollableFrame(root, width=700, height=600)
    question_frame.pack(pady=(20, 10))

    # 파트 제목 표시
    part_label = ctk.CTkLabel(
        question_frame,
        text=f"PART {page_index + 1}: {question_parts[page_index]}",
        font=LABEL_FONT,
        anchor="w",
        justify="left"
    )
    part_label.pack(anchor="w", padx=30, pady=(10, 20))

    # 각 문항 출력
    for i in range(start_index, end_index):
        q_num = i + 1
        question_label = ctk.CTkLabel(
            question_frame,
            text=f"🔹 Q{q_num}. {questions[i]['question']}",
            font=QUESTION_FONT,
            anchor="w",
            wraplength=600,
            justify="left"
        )
        question_label.pack(anchor="w", padx=30, pady=(15, 5))

        for j, choice in enumerate(questions[i]['choices']):
            rb = ctk.CTkRadioButton(
                question_frame,
                text=f"{choice}",
                variable=selected_values[i - start_index],
                value=j + 1,
                font=CHOICE_FONT
            )
            rb.pack(anchor="w", padx=60, pady=2)

    # 선택지를 모두 골랐는지 확인 후 다음으로 넘어가는 함수
    def submit_answers():
        scores = [var.get() for var in selected_values]
        state.answer_scores.extend(scores)
        to_next_page()

    # 다음 버튼 생성 (초기에는 비활성화)
    next_button = button(
        root,
        text="다음",
        command=submit_answers,
        fg_color="gray",
        state="disabled",
    )
    next_button.pack(pady=10)

    # 값이 바뀔 때마다 전체 체크해서 버튼 활성화
    def check_all_selected():
        all_selected = True
        for var in selected_values:
            if var.get() == 0:
                all_selected = False
                break
        if all_selected:
            next_button.configure(state="normal", fg_color="#1f6aa5")
        else:
            next_button.configure(state="disabled", fg_color="gray")

    # trace 콜백 함수 (*args는 trace 시스템에서 자동으로 전달됨)
    # → 실제로는 변수 이름, 인덱스, 변경 타입 등이 들어옴 (우리는 쓰지 않음)
    def on_change(*args):
        check_all_selected()

    # 각 IntVar에 trace 걸기
    for var in selected_values:
        var.trace_add("write", on_change)