import streamlit as st
import replicate
import pydantic

# Oprava pre novú verziu Pythonu
pydantic.class_validators.class_property = lambda x: x

st.title("🎬 AI Animátor")

uploaded_file = st.file_uploader("Nahraj fotku", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Tvoja fotka", use_container_width=True)
    
    if st.button("Animovať"):
        with st.spinner("Generujem video..."):
            try:
                # Tu si to samo vytiahne kľúč zo Secrets
                model = replicate.models.get("lucataco/animate-diff")
                version = model.versions.get("be2271c589fe4371ba3a94cd2f3a69485f7f34c5685df5d13b41d063737b6c5a")
                
                output = version.predict(input={"path": uploaded_file})
                st.video(output)
            except Exception as e:
                st.error(f"Chyba: {e}")
