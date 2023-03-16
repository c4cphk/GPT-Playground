import streamlit as st
import openai
from datetime import datetime
from streamlit.components.v1 import html

st.set_page_config(page_title="Chat with GPT")

html_temp = """
                <div style="background-color:{};padding:1px">
                
                </div>
                """
with st.sidebar:
    st.markdown("""
    ## About 
    GPT Response Generator is an easy-to-use tool that quickly generates meaningful responses to any given topic. 
    """)
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    
    st.markdown("""
    ## How does it work?
    Simply enter the topic of interest into the text field and the GPT algorithm will use its vast knowledge of language to generate relevant responses.
    """)
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    
    st.markdown("""
    ## Options 
    """)
    engine = st.selectbox('Engine:', ('text-davinci-003', 'text-davinci-002', 'text-davinci-001', 'text-curie-001', 'text-babbage-001', 'text-ada-001'))
    temperature = st.slider('Temperature:', min_value=0.0, max_value=2.0, value=0.7, step=0.1)
    top_p = st.slider('Top P:', min_value=0.0, max_value=1.0, value=0.5, step=0.1)
    max_tokens = st.slider('Max Tokens:', min_value=100, max_value=4096, value=200, step=50)
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    
    st.markdown("""
    Made by Raymond Ng
    """,
    unsafe_allow_html=True,
    )


input_text = None
apikey = None

st.markdown("""
# OpenAI GPT Playground
""")

apikey = st.text_input("Your API Key", disabled=False, type="password", placeholder="API Key?")
input_text = st.text_area("Topic of interest (press Ctrl-Enter once you have completed your inquiry)", disabled=False, placeholder="What topic you would like to ask?")

if input_text:
    prompt = str(input_text)
    if prompt:
        if st.button('Submit'):
            openai.api_key = apikey
            response = openai.Completion.create(engine=engine, prompt=prompt, temperature=temperature, max_tokens=max_tokens, top_p=top_p)
            output = response['choices'][0]['text']
            today = datetime.today().strftime('%Y-%m-%d')
            topic = input_text+"\n@Date: "+str(today)+"\n"+output
        
            st.info(output)
            filename = "Response_"+str(today)+".txt"
            btn = st.download_button(
                label="Download Text",
                data=topic,
                file_name=filename
            )

#####################################################
# Parameters for the Completion
#####################################################
# engine: text-davinci-003 (default)
#         text-davinci-002
#         text-davinci-001
#         text-curie-001
#         text-babbage-001
#         text-ada-001
# 
# temperature: 0 to 2 (default to 1)
# max_tokens: 100 to 4096 (default to 2048)
# top_p: 0 to 1 (default to 0.5)
# frequency_penalty: -2.0 to 2.0 (default to 0.0)
# presence_penalty: -2.0 to 2.0 (default to 0.0)
# stop: (default to "###")





