import streamlit as st
import replicate
import os

# Tvoj API token pre Replicate
os.environ["REPLICATE_API_TOKEN"] = "R8_UlI9xgBbAGvQqRRMtpXuEmdpGQag3hy0Jtwda"

st.set_page_config(page_title="AI Video Animátor", layout="centered")

st.title("🎬 AI Animátor")
st.write("Nahraj fotku a AI ju premení na krátke video.")

# 1. Nahrávanie obrázka
uploaded_file = st.file_uploader("Vyber obrázok (jpg, png)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Tvoj obrázok", use_container_width=True)
    
    if st.button("Spustiť animáciu ✨"):
        with st.spinner("Pracujem na tom... Trvá to asi 60 sekúnd."):
            try:
                # Dočasné uloženie obrázka
                with open("temp_img.jpg", "wb") as f:
                    f.write(uploaded_file.getbuffer())

                # Volanie AI modelu
                output = replicate.run(
                    "stability-ai/stable-video-diffusion:3f045751",
                    input={
                        "input_image": open("temp_img.jpg", "rb"),
                        "video_length": "14_frames_with_svd",
                        "fps": 6
                    }
                )

                video_url = output[0] if isinstance(output, list) else output
                
                # Zobrazenie výsledku
                st.success("Hotovo!")
                st.video(video_url)

            except Exception as e:
                st.error(f"Nastal problém: {e}")
