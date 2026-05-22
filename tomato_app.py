import streamlit as st
import pandas as pd
import joblib  # 또는 pickle (모델을 불러오기 위해 필요합니다)

rf_model = joblib.load('tomato_model.pkl')

# --- 웹 페이지 UI 구성 ---
st.title("착과율 예측 프로그램")
st.write("외부 온도, 내부 온도, 내부 습도를 입력하여 예측 착과율을 확인하세요.")

st.markdown("---")

# 1. 사용자 입력 받기 (사이드바 또는 메인 화면에 배치 가능)
st.subheader("데이터 입력")
out_temp = st.number_input("외부온도 입력 :", value=0.0, step=0.1, format="%.1f")
in_temp = st.number_input("내부온도 입력 :", value=0.0, step=0.1, format="%.1f")
humidity = st.number_input("내부습도 입력 :", value=0.0, step=0.1, format="%.1f")

st.markdown("---")

# 예측 버튼 생성
if st.button("착과율 예측하기"):
    if rf_model is not None:
        # 2. DataFrame으로 변환 (2차원 배열 형태로 입력)
        input_data = pd.DataFrame(
            [[out_temp, in_temp, humidity]], 
            columns=['외부온도', '내부온도', '내부습도']
        )
        
        # 3. 예측
        predicted = rf_model.predict(input_data)
        
        # 4. 결과 출력
        st.subheader("예측 결과")
        st.success(f"예측 착과율 : **{predicted[0]:.1f}%**")
    else:
        st.warning("모델이 정상적으로 로드되지 않아 예측을 수행할 수 없습니다.")