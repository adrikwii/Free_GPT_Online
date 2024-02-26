import streamlit as st
import g4f

if not "historique" in st.session_state:
    st.session_state.historique = []
	
	

    
st.set_page_config(page_title="Free_GPT",page_icon="Icon/Logo.png",layout="wide")
streamlit_style = """
			<style>
				/* Header */
				[data-testID="stHeader"]
				{
					background-color: rgba(0, 0, 0, 0);
					opacity: 25%;
				}
				/* Scroll Bar */
				[class="main st-emotion-cache-uf99v8 ea3mdgi8"]
				{
					overflow-y: hidden;
					overflow-x: hidden;
				}
				/* Body */
				[data-testID="stApp"]
				{
					background-color: #363333;
					opacity: 0.9;
					background-image:  repeating-radial-gradient( circle at 0 0, transparent 0, #363333 23px ), repeating-linear-gradient( #00000055, #000000 );
					margin-top: -80px;
				}

				/* Title */
				[class="st-emotion-cache-183lzff exotz4b0"]
				{
					margin: 0 auto;
				}

				/* Onglet */
				[class="st-af st-ag st-ah st-ai st-aj st-ak st-al st-am st-an st-ao st-ap st-aq st-ar"]
				{
					justify-content: center;
					background-color: #363333;
    				border-radius: 50px;
				}
				[class="st-ca st-af st-c7"]
				{
					opacity: 0%;
				}

				/* Div affichage question-rep */
				[class="st-emotion-cache-g621un e1f1d6gn0"]
				{
					background-color: #363333;
				}

				/* Div Question utilisateur */
				[class="stChatMessage st-emotion-cache-janbn0 eeusbqq4"]
				{
					background-color: rgb(35 37 44);
				}
				/* Sponsor */
				[data-testID="manage-app-button"]
				{
					opacity: 0%;
				}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)

st.text("""
████████████████████████████████████▀█████████████
█▄─▄▄─█▄─▄▄▀█▄─▄▄─█▄─▄▄─█▀▀▀▀▀██─▄▄▄▄█▄─▄▄─█─▄─▄─█
██─▄████─▄─▄██─▄█▀██─▄█▀████████─██▄─██─▄▄▄███─███
▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▀▄▄▄▀▀▀▀▄▄▄▀▀""")
st.divider()
tab1,tab2 = st.tabs([":lower_left_ballpoint_pen: Texte :lower_left_ballpoint_pen:",":camera_with_flash: Image :camera_with_flash:"])
with tab1 :
	with st.container() :
		messages = st.container(height=425)
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
    Image = st.container(height=425)
    if generationPic := st.chat_input("Image"):
        Image.chat_message("user",avatar="Icon/utilisateur.png").write(generationPic)
        st.toast('En cours de génération ...')
        response =  "https://image.pollinations.ai/prompt/"+generationPic
        Image.chat_message("assistant",avatar="Icon/robot.png").image(response,width=300)
        st.toast('Terminé :smile:')
col4, col5, col6 = st.columns(3)
with col6:
    col7, col8 = st.columns(2)
    with col8:
        st.write("Dévelopé par [adrikwii](https://github.com/adrikwii)")
    
