import streamlit as st

st.title("Einstein Puzzle")

st.session_state.disabled = False

color = ["-", "노란색", "파란색", "빨간색", "초록색", "하얀색"]
world = ["-", "노르웨이", "덴마크", "영국", "독일", "스웨덴"]
drink = ["-", "생수", "차", "우유", "커피", "주스"]
veget = ["-", "양배추", "토마토", "당근", "양파", "브로콜리"]
anima = ["-", "고양이", "말", "새", "금붕어", "강아지"]

col0, col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 2, 2, 2])

with col0:
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown("색상")
    st.markdown(" ")
    st.markdown("국적")
    st.markdown(" ")
    st.markdown("음료")
    st.markdown(" ")
    st.markdown("채소")
    st.markdown(" ")
    st.markdown("동물")

C1, C2, C3, C4, C5 = "-", "-", "-", "-", "-"
W1, W2, W3, W4, W5 = "-", "-", "-", "-", "-"
D1, D2, D3, D4, D5 = "-", "-", "-", "-", "-"
V1, V2, V3, V4, V5 = "-", "-", "-", "-", "-"
A1, A2, A3, A4, A5 = "-", "-", "-", "-", "-"

for i in range(1, 6):
    with globals()[f'col{i}']:
        st.markdown(f'{i}번째 집')
        globals()[f'C{i}'] = st.selectbox(options=color, index=0, label=f'C{i}',
                                          label_visibility="collapsed", disabled=st.session_state.disabled)
        globals()[f'W{i}'] = st.selectbox(options=world, index=0, label=f'W{i}',
                                          label_visibility="collapsed", disabled=st.session_state.disabled)
        globals()[f'D{i}'] = st.selectbox(options=drink, index=0, label=f'D{i}',
                                          label_visibility="collapsed", disabled=st.session_state.disabled)
        globals()[f'V{i}'] = st.selectbox(options=veget, index=0, label=f'V{i}',
                                          label_visibility="collapsed", disabled=st.session_state.disabled)
        globals()[f'A{i}'] = st.selectbox(options=anima, index=0, label=f'A{i}',
                                          label_visibility="collapsed", disabled=st.session_state.disabled)

colorA = ["-", C1, C2, C3, C4, C5]
worldA = ["-", W1, W2, W3, W4, W5]
drinkA = ["-", D1, D2, D3, D4, D5]
vegetA = ["-", V1, V2, V3, V4, V5]
animaA = ["-", A1, A2, A3, A4, A5]

col01, col02 = st.columns(2)

# Q1
Q1_1 = [i for i in range(6) if "영국" in worldA[i]]
Q1_2 = [i for i in range(6) if "빨간색" in colorA[i]]
Q1 = Q1_1 == Q1_2 and Q1_1

# Q2
Q2_1 = [i for i in range(6) if "덴마크" in worldA[i]]
Q2_2 = [i for i in range(6) if "차" in drinkA[i]]
Q2 = Q2_1 == Q2_2 and Q2_1

# Q3
Q3_1 = [i for i in range(6) if "커피" in drinkA[i]]
Q3_2 = [i for i in range(6) if "초록색" in colorA[i]]
Q3 = Q3_1 == Q3_2 and Q3_1

# Q4
Q4_1 = [i for i in range(6) if "양배추" in vegetA[i]]
Q4_2 = [i for i in range(6) if "노란색" in colorA[i]]
Q4 = Q4_1 == Q4_2 and Q4_1

# Q5
Q5 = W1 == "노르웨이"

# Q6
Q6_1 = animaA.index("말") if "말" in animaA else False
Q6_2 = vegetA.index("양배추") if "양배추" in vegetA else False
Q6 = (Q6_1 and Q6_2) and Q6_1 == Q6_2-1 or Q6_1 == Q6_2+1

# Q7
Q7_1 = [i for i in range(6) if "독일" in worldA[i]]
Q7_2 = [i for i in range(6) if "양파" in vegetA[i]]
Q7 = Q7_1 == Q7_2 and Q7_1

# Q8
Q8_1 = drinkA.index("생수") if "생수" in drinkA else False
Q8_2 = vegetA.index("토마토") if "토마토" in vegetA else False
Q8 = (Q8_1 and Q8_2) and (Q8_1 == Q8_2-1 or Q8_1 == Q8_2+1)

# Q9
Q9_1 = [i for i in range(6) if "스웨덴" in worldA[i]]
Q9_2 = [i for i in range(6) if "강아지" in animaA[i]]
Q9 = Q9_1 == Q9_2 and Q9_1

# Q10
Q10_1 = colorA.index("초록색") if "초록색" in colorA else False
Q10_2 = colorA.index("하얀색") if "하얀색" in colorA else False
Q10 = (Q10_1 and Q10_2) and Q10_1 == Q10_2-1

# Q11
Q11_1 = [i for i in range(6) if "당근" in vegetA[i]]
Q11_2 = [i for i in range(6) if "새" in animaA[i]]
Q11 = (Q11_1 and Q11_2) and Q11_1 == Q11_2

# Q12
Q12 = D3 == "우유"

# Q13
Q13_1 = vegetA.index("토마토") if "토마토" in vegetA else False
Q13_2 = animaA.index("고양이") if "고양이" in animaA else False
Q13 = (Q13_1 and Q13_2) and (Q13_1 == Q13_2-1 or Q13_1 == Q13_2+1)

# Q14
Q14_1 = [i for i in range(6) if "브로콜리" in vegetA[i]]
Q14_2 = [i for i in range(6) if "주스" in drinkA[i]]
Q14 = (Q14_1 and Q14_2) and Q14_1 == Q14_2 and Q14_1

# Q15
Q15_1 = worldA.index("노르웨이") if "노르웨이" in worldA else False
Q15_2 = colorA.index("파란색") if "파란색" in colorA else False
Q15 = (Q15_1 and Q15_2) and (Q15_1 == Q15_2-1 or Q15_1 == Q15_2+1)

with col01:
    st.markdown("* **자동으로 체크** 됩니다. :a 오류는 확인 못해줍니다.")
    st.checkbox("* 1. 영국 사람은 빨간색 집에 산다.", value=Q1, key=1)
    st.checkbox("* 2. 덴마크 사람은 차를 마신다.", value=Q2, key=2)
    st.checkbox("* 3. 초록색 집에 사는 사람은 커피를 마신다.", value=Q3, key=3)
    st.checkbox("* 4. 노란색 집에 사는 사람은 양배추를 먹는다.", value=Q4, key=4)
    st.checkbox("* 5. 노르웨이 사람은 첫 번째 집에 산다.", value=Q5, key=5)
    st.checkbox("* 6. 말을 기르는 사람은 :a 양배추를 먹는 사람의 옆집에 산다.", value=Q6, key=6)
    st.checkbox("* 7. 독일 사람은 양파를 먹는다.", value=Q7, key=7)

with col02:
    st.checkbox("* 8. 토마토를 먹는 사람은 :a 생수를 마시는 사람과 이웃이다.", value=Q8, key=8)
    st.checkbox("* 9. 스웨덴 사람은 강아지를 기른다.", value=Q9, key=9)
    st.checkbox("* 10. 초록색 집은 하얀색 집의 왼쪽 집이다.", value=Q10, key=10)
    st.checkbox("* 11. 당근을 먹는 사람은 새를 기른다.", value=Q11, key=11)
    st.checkbox("* 12. 한가운데 집에 사는 사람은 우유를 마신다.", value=Q12, key=12)
    st.checkbox("* 13. 토마토를 먹는 사람은 :a 고양이를 기르는 사람의 옆집에 산다.", value=Q13, key=13)
    st.checkbox("* 14. 브로콜리를 먹는 사람은 주스를 마신다.", value=Q14, key=14)
    st.checkbox("* 15. 노르웨이 사람은 파란색 집 옆집에 산다.", value=Q15, key=15)


if colorA == color and worldA == world and drinkA == drink and vegetA == veget and animaA == anima:
    st.balloons()