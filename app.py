import streamlit as st

st.set_page_config(
    page_title="연애 코칭 앱",
    page_icon="💘"
)

st.title("💘 연애 코칭 앱")

st.write("현재 고민을 입력해보세요.")

user_input = st.text_area("연애 고민 입력")

if st.button("코칭 받기"):

    if user_input == "":
        st.warning("고민을 입력해주세요.")
    else:

        # 아주 단순한 답변 로직
        if "고백" in user_input:
            answer = "너무 완벽한 타이밍만 기다리지 말고 자연스럽게 표현해보세요."

        elif "연락" in user_input:
            answer = "상대 반응에 집착하기보다 본인 페이스를 유지하는 게 중요해요."

        elif "이별" in user_input:
            answer = "억지로 잊으려 하기보다 감정을 충분히 정리할 시간을 주세요."

        else:
            answer = "상대보다 먼저 자신의 감정을 솔직하게 이해하는 게 중요해요."

        st.success("코칭 결과")
        st.write(answer)
