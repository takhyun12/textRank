# -*- coding: utf-8 -*-
from textrankr import TextRank
from tkinter import *

if __name__ == '__main__':
    if len(sys.argv) is not 1:
        input_text = sys.argv[1] # 첫번째 인수(사용자 입력값)을 변수에 저장
        textrank = TextRank(input_text)  # 사용자가 입력한 문자열을 요약 모듈에 할당함
        summary_result = textrank.summarize(3)  # 3줄 요약 후 결과를 받아옴
        print(summary_result)




