import streamlit as st
import g4f

if not "historique" in st.session_state:
    st.session_state.historique = []
	
	

    
st.set_page_config(page_title="Free_GPT",page_icon="Icon/Logo.png",layout="wide")
streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');

			html, body, [class*="css"]  {
   				font-family: 'Roboto', sans-serif;
   				margin-top: 0;
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col2:
    st.text("""
████████████████████████████████████▀█████████████
█▄─▄▄─█▄─▄▄▀█▄─▄▄─█▄─▄▄─█▀▀▀▀▀██─▄▄▄▄█▄─▄▄─█─▄─▄─█
██─▄████─▄─▄██─▄█▀██─▄█▀████████─██▄─██─▄▄▄███─███
▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▀▄▄▄▀▀▀▀▄▄▄▀▀""")
st.divider()
tab1,tab2 = st.tabs([":lower_left_ballpoint_pen: Texte :lower_left_ballpoint_pen:",":camera_with_flash: Image :camera_with_flash:"])
with tab1 :
	with st.container() :
		messages = st.container(height=300)
		if prompt := st.chat_input("Question"):
			if (st.session_state.historique != []):
				for ligne in st.session_state.historique:
					i = 0
					for colonne in ligne:
						if i == 0:
							messages.chat_message("user",avatar="Icon/utilisateur.png").write(colonne)
						else:
							messages.chat_message("assistant",avatar="Icon/robot.png").write(colonne)
						i += 1
			messages.chat_message("user",avatar="Icon/utilisateur.png").write(prompt)
			st.toast('En cours de génération ...')
			with messages.chat_message("assistant",avatar="Icon/robot.png"):
				with st.spinner(""):
					response = g4f.ChatCompletion.create(
						model=g4f.models.gpt_4,
						provider=g4f.Provider.You,
						messages=[{"role": "user", "content": prompt}],
					)
				st.write(response)
			st.session_state.historique.append([prompt,response])
			st.toast('Terminé :smile:')
with tab2 :
    Image = st.container(height=550)
    if generationPic := st.chat_input("Image"):
        Image.chat_message("user",avatar="Icon/utilisateur.png").write(generationPic)
        st.toast('En cours de génération ...')
        response =  "https://image.pollinations.ai/prompt/"+generationPic
        Image.chat_message("assistant",avatar="Icon/robot.png").image(response,width=400)
        st.toast('Terminé :smile:')
col4, col5, col6 = st.columns(3)
with col6:
    col7, col8 = st.columns(2)
    with col8:
        st.write("Dévelopé par [adrikwii](https://github.com/adrikwii)")
    
