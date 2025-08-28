import streamlit as st
from PIL import Image

# --- 페이지 설정 ---
st.set_page_config(page_title="슈의 제과점", layout="centered")

# --- 타이틀 & 설명 ---
st.title("🍰 슈의 제과점")
st.subheader("당신만의 디저트를 만들어보세요!")
st.markdown("재료를 골라 최고의 디저트를 만들어 보세요. 조합에 따라 결과가 달라집니다!")

# --- 디저트 이름 생성 함수 ---
def generate_dessert_name(flour, sweetener, fat, toppings):
    name_parts = []

    if flour == "박력분":
        name_parts.append("부드러운")
    elif flour == "중력분":
        name_parts.append("클래식한")
    else:
        name_parts.append("쫄깃한")

    if sweetener == "설탕":
        name_parts.append("달콤한")
    elif sweetener == "꿀":
        name_parts.append("자연의")
    else:
        name_parts.append("건강한")

    if fat == "버터":
        name_parts.append("버터향 가득한")
    elif fat == "마가린":
        name_parts.append("고소한")
    else:
        name_parts.append("가벼운")

    if toppings:
        topping_str = ", ".join(toppings)
        name_parts.append(f"{topping_str} 디저트")
    else:
        name_parts.append("심플 디저트")

    return " ".join(name_parts)

# --- 재료 선택 ---
flour = st.selectbox("1. 밀가루 종류를 선택하세요", ["중력분", "박력분", "강력분"])
sweetener = st.selectbox("2. 당류를 선택하세요", ["설탕", "꿀", "스테비아"])
fat = st.selectbox("3. 유지(지방)를 선택하세요", ["버터", "마가린", "식용유"])
topping = st.multiselect("4. 토핑을 골라주세요 (복수 선택 가능)", ["초콜릿칩", "딸기", "크림치즈", "아몬드", "블루베리"])

# --- 디저트 완성 버튼 ---
if st.button("🍽️ 디저트 완성하기!"):

    # 디저트 이름 생성
    dessert_name = generate_dessert_name(flour, sweetener, fat, topping)
    st.markdown(f"### 🧁 오늘 만든 디저트 이름은: **{dessert_name}** 🎉")

    # 결과 분기
    try:
        if flour == "박력분" and sweetener == "설탕" and fat == "버터" and "초콜릿칩" in topping:
            st.image("images/shu_cookies.png", caption="🍪 슈가 초코칩 쿠키를 들고 있어요!", use_column_width=True)
            st.success("✨ 완벽한 초코칩 쿠키 완성!")
            st.markdown("💬 **슈:** 우와! 진짜 진짜 맛있어 보여요! 대박이야~ 🍪")

        elif flour == "강력분" and sweetener == "꿀" and fat == "버터" and "딸기" in topping:
            st.image("images/shu_strawberry.png", caption="🍓 슈가 딸기 브레드를 들고 있어요!", use_column_width=True)
            st.success("🍓 달콤한 딸기 브레드 완성!")
            st.markdown("💬 **슈:** 꺄아~ 딸기 향기가 폴폴~ 나도 한 입만~! 🍓")

        elif flour == "중력분" and sweetener == "스테비아":
            st.image("images/shu_weird.png", caption="🤔 슈가 미심쩍은 빵을 들고 있어요...", use_column_width=True)
            st.warning("🤨 맛이 좀 애매한데요...? 건강빵 완성!")
            st.markdown("💬 **슈:** 어… 이건 건강한 맛이네...? 흠… 다음엔 좀 더 달게 해보자~")

        else:
            st.image("images/shu_fail.png", caption="💥 슈가 망한 반죽을 들고 있어요...", use_column_width=True)
            st.error("😢 뭔가 잘못됐어요... 반죽이 망했어요.")
            st.markdown("💬 **슈:** 꺄악! 반죽이 폭발했어요!! 다시 도전해봐요~ 💦")

    except FileNotFoundError:
        st.warning("⚠ 이미지 파일이 없어요! 'images/' 폴더에 그림을 넣어주세요.")

    st.markdown("### 📦 다시 만들어보고 싶으면 재료를 바꿔보세요!")

