import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="点数早見表",
    page_icon="🀐",
)

DATA_DIR = 'data/'
KO_RON_DF = pd.read_csv(DATA_DIR+'ko_ron.csv', index_col=0, dtype='str').T
KO_TUMO_DF = pd.read_csv(DATA_DIR+'ko_tumo.csv', index_col=0, dtype='str').T
OYA_RON_DF = pd.read_csv(DATA_DIR+'oya_ron.csv', index_col=0, dtype='str').T
OYA_TUMO_DF = pd.read_csv(DATA_DIR+'oya_tumo.csv', index_col=0, dtype='str').T
OYA_TUMO_DF = OYA_TUMO_DF.fillna('0').applymap(lambda x: '<NA>' if x == '0' else str(x)+' all')

### UI
st.title("点数早見表")

transpose = st.checkbox('行と列を入れ替える')

if transpose:
    KO_RON_DF = KO_RON_DF.T
    KO_TUMO_DF = KO_TUMO_DF.T
    OYA_RON_DF = OYA_RON_DF.T
    OYA_TUMO_DF = OYA_TUMO_DF.T

st.header("子の点数")
st.subheader("ロン和了")
st.caption('まずはここから覚えましょう')
st.dataframe(KO_RON_DF,use_container_width=True)

st.subheader("ツモ和了")
st.caption('子のロンを2で割ると親への請求, 4で割ると子への請求になります')
st.dataframe(KO_TUMO_DF,use_container_width=True)

st.header("親の点数")
st.subheader("ロン和了")
st.caption('子のロンのおおよそ1.5倍です')
st.dataframe(OYA_RON_DF,use_container_width=True)

st.subheader("ツモ和了")
st.caption('親のツモ和了は子のツモの親被りと同じだけ子全員に請求します')

st.dataframe(OYA_TUMO_DF,use_container_width=True)
st.sidebar.success("Select a demo above.")

