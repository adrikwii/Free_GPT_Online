import streamlit as st
import g4f


st.set_page_config(page_title="Free_GPT",page_icon=":robot_face:",layout="wide")
col1, col2, col3 = st.columns(3)
with col2:
    st.text("""
████████████████████████████████████▀█████████████
█▄─▄▄─█▄─▄▄▀█▄─▄▄─█▄─▄▄─█▀▀▀▀▀██─▄▄▄▄█▄─▄▄─█─▄─▄─█
██─▄████─▄─▄██─▄█▀██─▄█▀████████─██▄─██─▄▄▄███─███
▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▀▄▄▄▀▀▀▀▄▄▄▀▀""")
st.divider()
tab1,tab2 = st.tabs([":lower_left_ballpoint_pen: Text :lower_left_ballpoint_pen:",":camera_with_flash: Image :camera_with_flash:"])
with tab1 :
    with st.container() :
        messages = st.container(height=300)
        if prompt := st.chat_input("Say something"):
            messages.chat_message("user").write(prompt)
            response = g4f.ChatCompletion.create(
                    model=g4f.models.gpt_4,
                    provider=g4f.Provider.You,
                    messages=[{"role": "user", "content": prompt}],
                    stream=True,
                    )
            messages.chat_message("assistant").write(response)
with tab2 :
    Image = st.container(height=550)
    if generationPic := st.chat_input("Image"):
        Image.chat_message("user").write(generationPic)
        response =  "https://image.pollinations.ai/prompt/"+generationPic
        Image.chat_message("assistant").image(response,width=400)
col4, col5, col6 = st.columns(3)
st.divider()
with col6:
    st.text("Dévelopée par A/M['https://github.com/adrikwii']")
    
