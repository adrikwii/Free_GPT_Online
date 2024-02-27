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
					color: rgb(215 82 77);
				}

				/* Onglet */
				[class="st-af st-ag st-ah st-ai st-aj st-ak st-al st-am st-an st-ao st-ap st-aq st-ar"]
				{
					justify-content: center;
					margin: 0 auto;
					width: 350px;
				}
				.st-emotion-cache-sh2krr p
				{
					font-size:25px;
				}
				[class="st-as st-at st-au st-av st-aw st-ax st-ay st-az st-b0 st-b1 st-b2 st-b3 st-b4 st-b5 st-b6 st-b7 st-b8 st-b9 st-ba st-bb st-bc st-bd st-be st-bf st-bg st-bh st-bi st-bj st-bk st-bl st-bm st-bn st-bo st-bp st-bq st-br st-bs st-bt st-bu st-bv st-bw st-bx st-by st-bz st-c0"]
				{
					padding: 10px; 
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
				/* Img Bot User */
				[class="st-emotion-cache-p4micv eeusbqq0"]
				{
					width: 2.5rem;
    				height: 2.5rem;
				}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)

st.text("""
████████████████████████████████████▀█████████████
█▄─▄▄─█▄─▄▄▀█▄─▄▄─█▄─▄▄─█▀▀▀▀▀██─▄▄▄▄█▄─▄▄─█─▄─▄─█
██─▄████─▄─▄██─▄█▀██─▄█▀████████─██▄─██─▄▄▄███─███
▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▀▄▄▄▀▀▀▀▄▄▄▀▀""")
tab1,tab2 = st.tabs(["  Texte  ","  Image  "])
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
			with messages.chat_message("assistant",avatar="Icon/robot.gif"):
				with st.spinner(""):
					response = g4f.ChatCompletion.create(
						model=g4f.models.gpt_4,
						provider=g4f.Provider.Bing,
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
        Image.chat_message("assistant",avatar="Icon/robot.gif").image(response,width=300)
        st.toast('Terminé :smile:')
col4, col5, col6 = st.columns(3)
with col4:
		if st.button("Vider l'historique :wastebasket:"):
			st.session_state.historique = []
with col6:
    col7, col8 = st.columns(2)
    with col8:
        st.write("Dévelopé par [adrikwii](https://github.com/adrikwii)")
    
