import streamlit as st
import pyqrcode
from io import BytesIO

# Fonction pour générer un QR code
def generate_qr_code(data):
    qr = pyqrcode.create(data)
    buffer = BytesIO()
    qr.png(buffer, scale=5)
    return buffer.getvalue()

# Contenu principal de l'application
st.title("Bienvenue sur l'application de découverte SLAM")

st.header("Qu'est-ce que l'option SLAM ?")
st.write(
    "L'option SLAM (Solutions Logicielles et Applications Métiers) forme les étudiants à devenir des spécialistes du développement "
    "logiciel, des bases de données et des applications métiers. Voici quelques compétences clés acquises en SLAM :"
)

st.markdown(
    "- Analyse des besoins et rédaction de cahiers des charges\n"
    "- Conception et développement d'applications logicielles\n"
    "- Gestion de bases de données\n"
    "- Maintenance des solutions logicielles"
)

st.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Python_logo_notext.svg/2048px-Python_logo_notext.svg.png",
    caption="Exemple d'outil utilisé en SLAM : Python",
    width=300,
)

# Section quiz interactif
st.header("Quiz : Êtes-vous fait pour l'option SLAM ?")
st.write("Répondez aux questions ci-dessous pour découvrir votre affinité avec l'option SLAM !")

score = 0

q1 = st.radio("1. Vous aimez :", ["Créer des sites web et des applications", "Configurer des réseaux", "Ni l'un ni l'autre"])
if q1 == "Créer des sites web et des applications":
    score += 1

q2 = st.radio("2. Vous préférez :", ["Résoudre des problèmes de code", "Assembler des matériels", "Je ne sais pas"])
if q2 == "Résoudre des problèmes de code":
    score += 1

q3 = st.radio("3. Les bases de données vous semblent :", ["Fascinantes", "Compliquées", "Inintéressantes"])
if q3 == "Fascinantes":
    score += 1

if st.button("Voir les résultats"):
    if score >= 2:
        st.success("Vous avez un profil idéal pour l'option SLAM !")
    else:
        st.warning("L'option SLAM pourrait être un défi intéressant pour vous, mais explorez aussi d'autres options.")

# QR Code
st.header("Ressource complémentaire")
st.write("Scannez ce QR code pour accéder à des exemples de projets réalisés en SLAM !")

qr_data = "https://www.example.com/projets-slam"
qr_code = generate_qr_code(qr_data)
st.image(qr_code, caption="Scannez-moi !", width=200)

st.write("[Cliquez ici si vous ne pouvez pas scanner le QR code.](https://www.example.com/projets-slam)")
