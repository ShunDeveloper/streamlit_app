import streamlit as st
import pandas as pd
import numpy as np
import random
from question.initialize import initialize

st.set_page_config(
    page_title="点数計算テスト(Normal)",
    page_icon="🀐",
)

GAME_MODE = 'normal'

# textがnaならTrueを返す
def isNA(text):
    flag = False
    if text=='<NA>':
        flag=True
    if type(text)==float:
        flag=True
    return flag

### session
if 'answer_normal' not in st.session_state:
    tmp_question, tmp_answer= initialize(mode=GAME_MODE)
    if isNA(tmp_answer):
        # 存在しない翻と符の組み合わせだった場合やり直す
        # 存在する翻と符の組み合わせが得られるまで試行を繰り返す
        while isNA(tmp_answer):
            tmp_question, tmp_answer= initialize(mode=GAME_MODE)
        # 存在する翻と符の組み合わせが得られたら更新する
        st.session_state['question_normal'], st.session_state['answer_normal'] = tmp_question, tmp_answer
    else:
        # 存在する翻と符の組み合わせが得られたら更新する
        st.session_state['question_normal'], st.session_state['answer_normal'] = tmp_question, tmp_answer

### UI
st.title("点数計算テスト(Normal)")
st.write('Normalでは20符~60符の中から問題が出題されます')
st.write('問題:この手の点数を計算してください')
st.write(st.session_state['question_normal'])
agree = st.checkbox('答えを確認する', key=GAME_MODE)
if agree:
    st.write('チェックボックスを外すと次の問題へ行きます')
    st.write('答え:',st.session_state['answer_normal'])
    tmp_question, tmp_answer= initialize(mode=GAME_MODE)
    
    if isNA(tmp_answer):
        while isNA(tmp_answer):
        # 存在しない翻と符の組み合わせだった場合やり直す
        # 存在する翻と符の組み合わせが得られるまで試行を繰り返す
            tmp_question, tmp_answer= initialize(mode=GAME_MODE)
        # 存在する翻と符の組み合わせが得られたら更新する
        st.session_state['question_normal'], st.session_state['answer_normal'] = tmp_question, tmp_answer
    else:
        # 存在する翻と符の組み合わせが得られたら更新する
        st.session_state['question_normal'], st.session_state['answer_normal'] = tmp_question, tmp_answer