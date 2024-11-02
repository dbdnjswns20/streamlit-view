import streamlit as st
st.write('# Upload Photo')
from PIL import Image

# 알레르기 선택 박스
st.header("Allergy Selection")
allergies = ["No", "Nuts", "Dairy products", "Gluten", "Crustaceans", "Eggs", "Beans"]
selected_allergy = st.multiselect("Please select the appropriate allergy", allergies)

if selected_allergy:
    st.write(f"Selected Allergy: {', '.join(selected_allergy)}")
else:
    st.write("No allergies selected.")

# 종교 선택 박스
st.header("Religion Selection")
religions = ["No", "Christianity", "Buddhism", "Islam", "Hinduism", "Judaism", "Other"]
selected_religion = st.selectbox("Please select the appropriate religion", religions)

if selected_religion != "No":
    st.write(f"Selected Religion: {selected_religion}")
else:
    st.write("No religion selected.")

# 이미지 업로드 칸 생성
uploaded_file = st.file_uploader("please upload the picture", type=["jpg", "jpeg", "png"])

# 업로드된 파일이 있는 경우 표시
if uploaded_file is not None:
    # PIL을 사용하여 이미지 열기
    image = Image.open(uploaded_file)
    st.image(image, caption="uploaded image", use_column_width=True)
    st.write("Image upload was successful!")
