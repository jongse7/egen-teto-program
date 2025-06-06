from tkinter import filedialog
import customtkinter as ctk

# 다양한 유틸 함수들을 정의하는 파일입니다.

# 페이지 초기화 함수
def page_set(root):
    for widget in root.winfo_children():
        widget.destroy()

# 중앙 정렬용 프레임 생성 함수
def create_center_frame(root):
    # 전체를 채우는 메인 프레임 생성
    frame = ctk.CTkFrame(root)
    frame.pack(fill="both", expand=True)
    center_frame = ctk.CTkFrame(frame, fg_color="transparent")
    center_frame.place(relx=0.5, rely=0.5, anchor="center")
    return center_frame

# 다운로드 함수 정의
def download_image(result_key, pil_img):
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG 파일", "*.png")],
        initialfile=f"{result_key}.png"
    )
    if file_path:
        pil_img.save(file_path)