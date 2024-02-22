import streamlit as st
import g4f


st.set_page_config(page_title="Ma page de test",page_icon=":tada:",layout="wide")
col1, col2, col3 = st.columns(3)
with col2 :
    col4,col5,col6 = st.columns(3)
    with col5:
        st.title("Free_GPT",anchor=False)
tab1,tab2 = st.tabs(["Text","Image"])
with tab1 :
    with st.container() :
        messages = st.container(height=300)
        if prompt := st.chat_input("Say something"):
            messages.chat_message("user").write(prompt)
            response = g4f.ChatCompletion.create(
                    model=g4f.models.gpt_4,
                    provider=g4f.Provider.Bing,
                    messages=[{"role": "user", "content": prompt}]
                    )
            messages.chat_message("assistant").write(response)
with tab2 :
    Image = st.container(height=550)
    if generationPic := st.chat_input("Image"):
        Image.chat_message("user").write(generationPic)
        response =  "https://image.pollinations.ai/prompt/"+generationPic
        Image.chat_message("assistant").image(response,width=400)
