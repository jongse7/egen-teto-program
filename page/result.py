# 점수와 성별 기반 결과 이미지를 보여주는 페이지입니다.

from PIL import Image
from customtkinter import CTkLabel, CTkImage
import customtkinter as ctk
import state
from style import LABEL_FONT
from utils import page_set
from utils import download_image

def show_result_page(root):
    # 기존 위젯 제거
    page_set(root)

    # 총점 계산
    total_score = sum(state.answer_scores)
    gender = state.selected_gender

    # 최대 점수는 200점 (40문항 * 5점)
    # 기준 점수: 120점 이상 = 테토 성향, 미만 = 에겐 성향
    if total_score >= 120 and gender == "남자":
        result_key = "테토남"
        image_path = "assets/테토남.png"
    elif total_score >= 120 and gender == "여자":
        result_key = "테토녀"
        image_path = "assets/테토녀.png"
    elif total_score < 120 and gender == "남자":
        result_key = "에겐남"
        image_path = "assets/에겐남.png"
    else:
        result_key = "에겐녀"
        image_path = "assets/에겐녀.png"

    # 결과 설명 출력
    label = ctk.CTkLabel(root, text=f"당신의 결과는: {result_key}", font=LABEL_FONT)
    label.pack(pady=20)

    # 이미지 로드 및 표시
    try:
        pil_img = Image.open(image_path)
        pil_img = pil_img.resize((480, 480)) 

        ctk_img = CTkImage(light_image=pil_img, size=(480, 480)) 

        image_label = CTkLabel(root, image=ctk_img, text="")
        image_label.pack(pady=10)

    except Exception as e:
        error_label = CTkLabel(root, text=f"이미지를 불러올 수 없습니다: {e}", font=("Pretendard", 12))
        error_label.pack()

    # 이미지 다운로드 버튼
    download_button = ctk.CTkButton(
        root,
        text="이미지 다운로드",
        command=lambda: download_image(result_key, pil_img),
    )
    download_button.pack(pady=10)

    # 종료 안내
    end_label = ctk.CTkLabel(root, text="설문이 완료되었습니다. 프로그램을 종료해 주세요.", font=("맑은 고딕", 14))
    end_label.pack(pady=20)

    
