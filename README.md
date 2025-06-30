# 🕵️‍♂️ Steganography Web App (with Encryption)

A beginner-friendly web app to **hide and extract secret messages** inside images or audio files — with password-based encryption! 🔐  
Built using Python, Streamlit, and Cryptography.

---

## 🚀 Features

- 🔐 **Password Protection** – Messages are encrypted before hiding
- 🖼️ **Image Steganography** – Hide messages inside `.png` images
- 🎵 **Audio Steganography** – Hide messages inside `.wav` files
- 🧪 **Message Extraction** – Recover hidden messages using the same password
- 🌐 **Web Interface** – Powered by Streamlit

---

## 🔧 How to Use

1. Go to the [Live App](https://your-url.streamlit.app)
2. Enter a strong password
3. Upload a `.png` image or `.wav` audio file
4. Type a secret message
5. Click **"Hide Message"** to download a secret file  
6. Later, upload the secret file and password to **extract** the hidden message

---

## 🛠️ Local Setup (Optional)

```
# Clone this repo
git clone https://github.com/ManjunathM202/SteganographyWebApp.git
cd SteganographyWebApp

# Create virtual environment (optional)
python -m venv venv
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```
---

## 📁 File Structure

```
SteganographyWebApp/
│
├── app.py                     # Streamlit Web App
├── encryption.py              # Password-based encryption
├── image_steganography.py    # Functions for image steganography
├── audio_steganography.py    # Functions for audio steganography
├── requirements.txt           # Python dependencies
└── README.md
```
---

## 📦 Dependencies

```

streamlit

pillow

pydub

cryptography
```
---

# Install with:
```

pip install -r requirements.txt
```
---

## 📜 License

This project is open-source and free to use under the MIT License.

---

## 🙌 Acknowledgments
Thanks to the Python and Streamlit community. Inspired by basic steganography and cryptography techniques.

---

### Developed  by  MATTAM MANJUNATH
