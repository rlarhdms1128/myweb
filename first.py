import streamlit as st

st.set_page_config(
    page_title='공동교육과정'
)

menu=st.sidebar.selectbox('MENU',["BMI 지수 계산기",'원의 넓이 계산기','합격/불합격 판단'])

if menu=='BMI 지수 계산기':
    st.subheader('BMI 지수 계산기')

    키=st.number_input('키를 입력하세요.(cm)', step=1)
    체중=st.number_input('몸무게를 입력하세요.(kg)', step=1)
    btn=st.button('계산하기')
    키=키/100

    if btn:
        st.write('당신의 BMI는',체중/(키*키), '입니다.')
        if 체중/(키*키)<18.5:
            st.write("저체중입니다")
        elif 18.5<=체중/(키*키)<=24.9:
            st.write("정상입니다")
        elif 25<=체중/(키*키)<=29.9:
            st.write("경도비만입니다")
        else:
            st.write("고도비만입니다")

elif menu=='원의 넓이 계산기':
    st.subheader('원의 넓이 계산기')
    반지름=st.number_input('원의 반지름을 입력하세요.(cm)', step=1)
    btn=st.button('계산하기')
    if btn:
        st.write('원의 넓이는',반지름*반지름*3.14, '(cm2)입니다.')

elif menu=="합격/불합격 판단":
    st.subheader('합격/불합격 판단(90점이상시 합격)')
    점수=st.number_input('점수를 입력하세요.', step=1)
    btn=st.button('계산하기')
    if btn:
        if 점수<0 or 점수>100:
            st.write('점수를 다시 입력하세요')
        else:
            if 100>점수>=90:
                st.write("합격입니다")
            elif 점수==100:
                st.write("축하합니다 만점입니다!")
            else:
                st.write("불합격입니다")

