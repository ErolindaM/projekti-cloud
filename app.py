import streamlit as st
import google.generativeai as genai

# Marrim API Key nga Secrets
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

st.title("☁️ Asistenti Inteligjent i Fakultetit")
st.write("Ky aplikacion përdor Google Gemini AI në Cloud.")

pyetja = st.text_input("Pyet diçka rreth teknologjisë:")

if st.button("Dërgo Pyetjen"):
    if pyetja:
        with st.spinner("Po kërkoj në serverat Cloud..."):
            try:
                # Ky është emri që kërkon versioni v1beta
                model = genai.GenerativeModel('gemini-3-flash-preview')
                pergjigja = model.generate_content(pyetja)
                st.success("Përgjigja:")
                st.write(pergjigja.text)
            except Exception as e:
                try:
                    # Model rezervë nëse i pari dështon
                    model_backup = genai.GenerativeModel('gemini-pro')
                    pergjigja = model_backup.generate_content(pyetja)
                    st.success("Përgjigja (Backup):")
                    st.write(pergjigja.text)
                except Exception as e2:
                    st.error(f"Gabim teknik: {str(e2)}")
    else:
        st.warning("Ju lutem shkruani një pyetje.")
