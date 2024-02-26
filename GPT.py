import streamlit as st
import g4f
historique = []
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
            if (historique != []):
                for ligne in historique:
                    i = 0
                    for colonne in ligne:
                        if i == 0:
                            messages.chat_message("user",avatar="Icon/utilisateur.png").write(colonne)
                        else:
                            messages.chat_message("assistant",avatar="Icon/robot.png").write(colonne)
                        i += 1
            messages.chat_message("user",avatar="Icon/utilisateur.png").write(prompt)
            st.toast('En cours de génération ...')
            response = g4f.ChatCompletion.create(
                    model=g4f.models.gpt_4,
                    provider=g4f.Provider.You,
                    messages=[{"role": "user", "content": prompt}],
                    stream=True,
                    ) 
            messages.chat_message("assistant",avatar="Icon/robot.png").write(response)
            st.toast('Terminé :smile:')
            historique.append([prompt,response])
with tab2 :
    Image = st.container(height=550)
    if generationPic := st.chat_input("Image"):
        Image.chat_message("user").write(generationPic)
        st.toast('En cours de génération ...')
        response =  "https://image.pollinations.ai/prompt/"+generationPic
        Image.chat_message("assistant").image(response,width=400)
        st.toast('Terminé :smile:')
col4, col5, col6 = st.columns(3)
with col6:
    col7, col8 = st.columns(2)
    with col8:
        st.write("Dévelopé par [adrikwii](https://github.com/adrikwii)")
    
