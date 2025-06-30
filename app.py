import streamlit as st
from encryption import generate_key_from_password, encrypt_message, decrypt_message
from image_steganography import encode_image, decode_image
from audio_steganography import hide_message_audio, extract_message_audio

st.title("🔐 Steganography Web App")
password = st.text_input("🔐 Enter a password for encryption/decryption", type="password")
if not password:
    st.warning("Please enter a password to continue.")
    st.stop()

key = generate_key_from_password(password)

mode = st.sidebar.selectbox("Choose Mode", ["Hide in Image", "Extract from Image", "Hide in Audio", "Extract from Audio"])

if mode == "Hide in Image":
    image = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

    text = st.text_area("Enter your secret message")
    if st.button("Hide Message") and image and text:
        encrypted = encrypt_message(text, key)
        stego_img = encode_image(image, encrypted)
        st.image(stego_img)
        st.download_button("Download Image", stego_img, file_name="secret_image.png")

elif mode == "Extract from Image":
    image = st.file_uploader("Upload PNG Image with Hidden Data", type=["png"])
    if st.button("Extract Message") and image:
        encrypted = decode_image(image)
        try:
            message = decrypt_message(encrypted, key)
            st.success(f"Hidden Message: {message}")
        except:
            st.error("Failed to decrypt message.")

elif mode == "Hide in Audio":
    audio = st.file_uploader("Upload WAV Audio", type=["wav"])
    text = st.text_area("Enter your secret message")
    if st.button("Hide in Audio") and audio and text:
        encrypted = encrypt_message(text, key)
        output_audio_path = hide_message_audio(audio, encrypted)
        with open(output_audio_path, "rb") as f:
            st.download_button("Download Audio", f, file_name="secret_audio.wav")

elif mode == "Extract from Audio":
    audio = st.file_uploader("Upload WAV Audio with Hidden Data", type=["wav"])
    if st.button("Extract from Audio") and audio:
        encrypted = extract_message_audio(audio)
        try:
            message = decrypt_message(encrypted, key)
            st.success(f"Hidden Message: {message}")
        except:
            st.error("Failed to decrypt audio.")
