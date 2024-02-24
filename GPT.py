import streamlit as st
import g4f

st.text("hey")
st.set_page_config(page_title="Free_GPT",page_icon=":robot_face:",layout="wide")
col1, col2, col3 = st.columns(3)
with col2:
    st.text("""
████████████████████████████████████▀█████████████
█▄─▄▄─█▄─▄▄▀█▄─▄▄─█▄─▄▄─█▀▀▀▀▀██─▄▄▄▄█▄─▄▄─█─▄─▄─█
██─▄████─▄─▄██─▄█▀██─▄█▀████████─██▄─██─▄▄▄███─███
▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▀▄▄▄▀▀▀▀▄▄▄▀▀""")
st.divider()
st.markdown("""
<style>

	.stTabs [data-baseweb="tab-list"] {
		gap: 2px;
    }

	.stTabs [data-baseweb="tab"] {
		height: 50px;
        white-space: pre-wrap;
		background-color: #F0F2F6;
		border-radius: 4px 4px 0px 0px;
		gap: 1px;
		padding-top: 10px;
		padding-bottom: 10px;
    }

	.stTabs [aria-selected="true"] {
  		background-color: #FFFFFF;
	}

</style>""", unsafe_allow_html=True)
tab1,tab2 = st.tabs([":lower_left_ballpoint_pen: Text :lower_left_ballpoint_pen:",":camera_with_flash: Image :camera_with_flash:"])
with tab1 :
    with st.container() :
        messages = st.container(height=300)
        if prompt := st.chat_input("Say something"):
            messages.chat_message("user").write(prompt)
            st.toast('En cours de génération ...')
            response = g4f.ChatCompletion.create(
                    model=g4f.models.gpt_4,
                    provider=g4f.Provider.You,
                    messages=[{"role": "user", "content": prompt}],
                    stream=True,
                    )
            messages.chat_message("assistant").write(response)
            st.toast('Terminée :smile:')
with tab2 :
    Image = st.container(height=550)
    if generationPic := st.chat_input("Image"):
        Image.chat_message("user").write(generationPic)
        st.toast('En cours de génération ...')
        response =  "https://image.pollinations.ai/prompt/"+generationPic
        Image.chat_message("assistant").image(response,width=400)
        st.toast('Terminée :smile:')
col4, col5, col6 = st.columns(3)
with col6:
    col7, col8 = st.columns(2)
    with col8:
        st.write("Dévelopée par [Adrien Metton](https://github.com/adrikwii)")
    
