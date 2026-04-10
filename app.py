import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Asistenti Cloud", page_icon="☁️")
st.title("☁️ Asistenti Inteligjent i Fakultetit")
st.write("Ky aplikacion funksionon në Cloud dhe përdor LLM për t'u përgjigjur pyetjeve tuaja.")

try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("Mungon API Key në konfigurimin e Cloud!")

pyetja = st.text_input("Bëni një pyetje:")

if st.button("Dërgo Pyetjen"):
    if pyetja:
        with st.spinner("Po kërkoj në serverat Cloud..."):
            pergjigja = model.generate_content(pyetja)
            st.success("Përgjigja:")
            st.write(pergjigja.text)
    else:
        st.warning("Ju lutem shkruani një pyetje!")