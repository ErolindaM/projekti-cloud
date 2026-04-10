import streamlit as st
import google.generativeai as genai

try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception as e:
    st.error("Gabim: Nuk u gjet 'GEMINI_API_KEY' te Secrets e Streamlit.")

st.set_page_config(page_title="Asistenti AI", page_icon="☁️")
st.title("☁️ Asistenti Inteligjent i Fakultetit")
st.write("Ky aplikacion përdor fuqinë e Gemini 3 Flash në Cloud.")

pyetja = st.text_input("Pyet diçka rreth teknologjisë ose mësimit:", placeholder="Shkruaj këtu...")

if st.button("Dërgo Pyetjen"):
    if pyetja:
        with st.spinner("Duke procesuar kërkesën në Cloud..."):
            try:
                model = genai.GenerativeModel('gemini-3-flash-preview')
                
                pergjigja = model.generate_content(pyetja)
                
                if pergjigja.text:
                    st.success("Përgjigja nga AI:")
                    st.write(pergjigja.text)
                else:
                    st.warning("AI nuk ktheu një përgjigje. Provo të ndryshosh pyetjen.")
                    
            except Exception as e:
                try:
                    model_fallback = genai.GenerativeModel('gemini-1.5-flash')
                    pergjigja = model_fallback.generate_content(pyetja)
                    st.success("Përgjigja (Backup):")
                    st.write(pergjigja.text)
                except Exception as e2:
                    st.error(f"Gabim teknik: {str(e2)}")
                    st.info("Këshillë: Kontrollo nëse API Key është kopjuar saktë te Secrets.")
    else:
        st.warning("Ju lutem shkruani një pyetje para se të klikoni butonin.")

st.divider()
st.caption("Punuar nga Grupi i Studentëve - Projekti Cloud Computing 2026")
