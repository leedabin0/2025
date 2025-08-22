import streamlit as st
from PIL import Image

st.set_page_config(page_title="슈의 제과점", layout="centered")

st.title("🍰 슈의 제과점")
st.subheader("당신만의 디저트를 만들어보세요!")

st.markdown("재료를 골라 최고의 디저트를 만들어 보세요. 조합에 따라 결과가 달라집니다!")

# --- 재료 선택 ---
flour = st.selectbox("1. 밀가루 종류를 선택하세요", ["중력분", "박력분", "강력분"])
sweetener = st.selectbox("2. 당류를 선택하세요", ["설탕", "꿀", "스테비아"])
fat = st.selectbox("3. 유지(지방)를 선택하세요", ["버터", "마가린", "식용유"])
topping = st.multiselect("4. 토핑을 골라주세요 (복수 선택 가능)", ["초콜릿칩", "딸기", "크림치즈", "아몬드", "블루베리"])

if st.button("🍽️ 디저트 완성하기!"):
    # 조합 결과 판단
    if flour == "박력분" and sweetener == "설탕" and fat == "버터" and "초콜릿칩" in topping:
        st.success("✨ 완벽한 초코칩 쿠키 완성!")
        st.image("cookies.jpg", caption="🍪 초코칩 쿠키", use_column_width=True)

    elif flour == "강력분" and sweetener == "꿀" and fat == "버터" and "딸기" in topping:
        st.success("🍓 달콤한 딸기 브레드 완성!")
        st.image("strawberry_bread.jpg", caption="🍓 딸기 브레드", use_column_width=True)

    elif flour == "중력분" and sweetener == "스테비아":
        st.warning("🤨 맛이 좀 애매한데요...? 건강빵 완성!")
        st.image("weird_bread.jpg", caption="🤔 건강빵(?)", use_column_width=True)

    else:
        st.error("😢 뭔가 잘못됐어요... 반죽이 망했어요.")
        st.image("fail.jpg", caption="💥 망한 빵", use_column_width=True)

    st.markdown("### 📦 다시 만들어보고 싶으면 재료를 바꿔보세요!")

