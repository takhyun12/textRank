# -*- coding: utf-8 -*-
from textrankr import TextRank
from tkinter import *

def Text_Summary():
    text_2.delete('1.0', END) # 재사용을 위해 초기화
    sentence = text_1.get("1.0","end-1c") # 사용자가 입력한 문자열을 받아옴
    textrank = TextRank(sentence) # 사용자가 입력한 문자열을 요약 모듈에 할당함
    summary_result = textrank.summarize(3) # 3줄 요약 후 결과를 받아옴
    text_2.insert("1.0", summary_result) # 요약 결과를 출력함

if __name__ == '__main__':
    root = Tk() # 프로그램 메인을 구동함

    title_label = Label(root, text="3줄 요약 봇 프로토 타입 버전", font=(None, 18, 'bold'), height=2)
    title_label.grid(row=0, column=1) # 그리드 1행에 첫번째 라벨 삽입

    label_1 = Label(root, text="사용자 입력", width=14) # 첫번째 라벨 정의
    label_1.grid(row=1) # 그리드 1행에 첫번째 라벨 삽입

    empty_label = Label(root, text="", width=14) # 두번째 라벨 정의
    empty_label.grid(row=2) # 그리드 2행에 두번째 라벨 삽입

    label_3 = Label(root, text="요약 결과", width=14) # 두번째 라벨 정의
    label_3.grid(row=3) # 그리드 2행에 두번째 라벨 삽입

    text_1 = Text(root, width=150) # 사용자 입력 텍스트 입력란 정의
    text_2 = Text(root, width=150, height=15) # 요약 결과 텍스트 입력란 정의

    text_1.grid(row=1, column=1) # 텍스트 입력란을 그리드 1행에 할당
    text_2.grid(row=3, column=1) # 요약 결과란을 그리드 2행에 할당

    button_1 = Button(root, text="요약하기", width=18, height=5, command=Text_Summary, ) # 버튼 정의
    button_1.grid(row=1, column=2) # 버튼을 그리드 1행에 할당

    copylight_title = Label(root, text="군수전산소 하사 정택현", height=2)
    copylight_title.grid(row=4, column=2) # 그리드 2행에 2열에 저작권 표시 할당

    root.mainloop() # 프로그램 구동



