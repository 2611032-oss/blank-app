import streamlit as st

# 웹 페이지 제목
st.title("🏫 교실 전등 관리 및 에너지 절약 캠페인")
st.write("각 반의 현재 전등 상태를 선택하고 아래 버튼을 눌러주세요.")

rooms = ["1반", "2반", "3반", "4반", "5반"]

# 사용자 입력을 저장할 딕셔너리
room_states = {}

# 1. 각 반별로 전등 상태 입력 받기 (라디오 버튼 활용)
st.subheader("💡 반별 전등 상태 체크")
for room in rooms:
    # '선택하세요'를 기본값으로 두어 사용자가 올바르게 선택하도록 유도
    state = st.radio(
        f"{room}의 현재 전등 상태:",
        options=["선택하세요", "on", "off"],
        key=room,
        horizontal=True  # 가로로 정렬하여 깔끔하게 배치
    )
    room_states[room] = state

st.markdown("---")

# 2. 결과 확인 버튼
if st.button("결과 확인하기", type="primary"):
    st.subheader("📋 실천 결과 및 피드백")
    
    for room in rooms:
        light = room_states[room]
        
        if light == "on":
            st.warning(f"🔴 **{room}**: 불끄기를 실천하여 에너지 낭비와 지구온난화를 해결합시다.")
        elif light == "off":
            st.success(f"🟢 **{room}**: 잘하고 있습니다. 앞으로도 그렇게 에너지 낭비를 줄여나갑시다!")
        else:
            st.error(f"⚪ **{room}**: on/off 로 상태를 선택해주세요.")