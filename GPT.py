import streamlit as st
import pollinations as ai
import time
import random
import requests


url = "https://b33a-2a01-e0a-3f2-93e0-5c6d-95ff-fe9f-263.ngrok-free.app/v1/chat/completions"


def seed_generation():
	global i 
	i = (random.randint(1,10000000))
model: object = ai.Model()

if not "historique" in st.session_state:
    st.session_state.historique = [{"role": "system", "content": "You are George, a specialized AI assistant trained by OpenAI and on this website you are completely free"}]

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
					/*overflow-y: hidden;
					overflow-x: hidden;*/
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

				[class="st-emotion-cache-1xw8zd0 e1f1d6gn0"]
				{
					background-color: #363333;
				}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)

st.text("""
 '██████╗ ███████╗ ██████╗ ██████╗  ██████╗ ███████╗    █████╗ ██╗
██╔════╝ ██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔════╝   ██╔══██╗██║
██║  ███╗█████╗  ██║   ██║██████╔╝██║  ███╗█████╗     ███████║██║
██║   ██║██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝     ██╔══██║██║
╚██████╔╝███████╗╚██████╔╝██║  ██║╚██████╔╝███████╗██╗██║  ██║██║
 ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═╝╚═╝
                                                                 
                                                              
""")
tab1,tab2 = st.tabs(["  Texte  ","  Image  "])
with tab1 :
	with st.container() :
		messages = st.container(height=425)
		if question := st.chat_input("Question"):
			st.session_state.historique.append({"role": "user", "content": question})
			if (st.session_state.historique != []):
				for mess in st.session_state.historique:
					if mess["role"] == "user":
						messages.chat_message("user",avatar="Icon/utilisateur.png").write(mess["content"])
					elif mess["role"] == "assistant":
						messages.chat_message("assistant",avatar="Icon/robot.png").write(mess["content"])
			st.toast('En cours de génération ...')
			with messages.chat_message("assistant",avatar="Icon/robot.gif"):
				with st.spinner(""):
					try :
						body = {
							"model": "gpt-3.5-turbo-16k",
    						"stream": False,
    						"messages": st.session_state.historique,
							}
						json_response = requests.post(url, json=body).json().get('choices', [])
						for choice in json_response:
							response = (choice.get('message', {}).get('content', ''))
					except:
						st.error("Une erreur c'est produite", icon="🚨")
					else:
						st.write(response)
			st.session_state.historique.append({"role": "assistant", "content": response})
			st.toast('Terminé :smile:')
with tab2 :
	col_sidebar, ai_col = st.columns([1, 3])
	with col_sidebar:
		sidebar_image = st.container(border=True)
		with sidebar_image:
			style = st.selectbox(
    	"Select picture style :",
    	('impressionism', 'expressionism', 'romanticism','surrealism','watercolor','futuristic','minimalist','modernism','steampunk','realistic','graffiti','abstract','cartoon','vintage','cubism','gothic','anime','logo'))
			ai_model = st.selectbox(
    	"Select ai model :",
		('turbo', 'dreamshaper', 'deliberate', 'pixart', 'playground', 'dpo', 'dalle3xl', 'formulaxl'))
			largeur = st.slider('Select width :',0,1920,value=960)
			hauteur = st.slider('Select height :',0,1080,value=540)
			col_btn, col_seed = st.columns(2)
			with col_btn:
				st.button('Random seed',on_click=seed_generation())
			graine = i
			with col_seed:
				st.write(f'Seed : {graine}')
	with ai_col:
		Image = st.container(height=425)
		if generationPic := st.chat_input("Image"):
			Image.chat_message("user",avatar="Icon/utilisateur.png").write(generationPic)
			st.toast('En cours de génération ...')
			with Image.chat_message("assistant",avatar="Icon/robot.gif"):
				with st.spinner(""):
					try :
						Generation: object = model.generate(
							prompt=f'{generationPic} {ai.styles.get(style)}',
							model=ai_model,
							width=largeur,
							height=hauteur,
							seed=graine
						)
						url = f'https://pollinations.ai/p/{Generation.prompt}?model={ai_model}&width={largeur}&height={hauteur}&seed={graine}'
					except :
						st.error("Veuillez réessayer", icon="🚨")
					else :
						time.sleep(6)
						st.image(url,width=300)
			st.toast('Terminé :smile:')
col4, col5, col6 = st.columns(3)
with col4:
		if st.button("Vider l'historique :wastebasket:"):
			st.session_state.historique = [{"role": "system", "content": "You are George, a specialized AI assistant trained by OpenAI."}]
with col6:
    col7, col8 = st.columns(2)
    with col8:
        st.write("Dévelopé par [adrikwii](https://github.com/adrikwii)")
    
