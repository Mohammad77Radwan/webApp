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

questions = [
    ("1. Vous aimez :", ["Créer des sites web et des applications", "Configurer des réseaux", "Ni l'un ni l'autre"]),
    ("2. Vous préférez :", ["Résoudre des problèmes de code", "Assembler des matériels", "Je ne sais pas"]),
    ("3. Les bases de données vous semblent :", ["Fascinantes", "Compliquées", "Inintéressantes"]),
    ("4. Vous aimez apprendre en :", ["Pratiquant avec des projets", "Écoutant des cours théoriques", "Je ne sais pas"]),
    ("5. Vous êtes :", ["Curieux des nouvelles technologies", "Intéressé par la logistique", "Sans préférence"]),
    ("6. Travailler en équipe pour développer une application vous semble :", ["Motivant", "Stressant", "Neutre"]),
    ("7. Les langages de programmation sont pour vous :", ["Passionnants", "Compliqués", "Ennuyeux"]),
    ("8. Vous aimez résoudre des problèmes :", ["Logiques", "Pratiques", "Aucun des deux"]),
    ("9. L'innovation technologique vous :", ["Inspire", "Ne vous intéresse pas", "Vous laisse neutre"]),
    ("10. Vous préférez travailler :", ["Sur ordinateur", "Avec des outils manuels", "Sans préférence"]),
    ("11. Gérer des bases de données vous semble :", ["Utile", "Fastidieux", "Inutile"]),
    ("12. Vous aimez participer à des projets :", ["Collaboratifs", "Individuels", "Je ne sais pas"]),
    ("13. Développer des algorithmes vous paraît :", ["Amusant", "Difficile", "Inutile"]),
    ("14. Vous vous sentez à l'aise avec :", ["Les logiciels", "Le matériel", "Aucun des deux"]),
    ("15. Vous aimez explorer :", ["Les nouvelles technologies", "Les techniques traditionnelles", "Je ne sais pas"]),
    ("16. Vous préférez :", ["Créer des solutions logicielles", "Utiliser des outils existants", "Aucun des deux"]),
    ("17. Vous êtes motivé par :", ["La résolution de problèmes", "L'organisation", "Autre"]),
    ("18. Apprendre de nouveaux langages de programmation vous semble :", ["Excitant", "Stressant", "Inutile"]),
    ("19. Travailler sur des projets innovants vous :", ["Passionne", "Laisse indifférent", "Ennuie"]),
    ("20. Être à jour sur les dernières technologies vous semble :", ["Essentiel", "Optionnel", "Inutile"]),
]

for i, (question, options) in enumerate(questions):
    answer = st.radio(question, options, key=i)
    if answer in ["Créer des sites web et des applications", "Résoudre des problèmes de code", "Fascinantes", "Pratiquant avec des projets", "Curieux des nouvelles technologies", "Motivant", "Passionnants", "Logiques", "Inspire", "Sur ordinateur", "Utile", "Collaboratifs", "Amusant", "Les logiciels", "Les nouvelles technologies", "Créer des solutions logicielles", "La résolution de problèmes", "Excitant", "Passionne", "Essentiel"]:
        score += 1

if st.button("Voir les résultats"):
    if score >= 15:
        st.success("Vous avez un profil idéal pour l'option SLAM !")
    elif score >= 10:
        st.info("Vous pourriez bien réussir dans l'option SLAM, avec un peu d'investissement !")
    else:
        st.warning("L'option SLAM pourrait être un défi intéressant pour vous, mais explorez aussi d'autres options.")

# QR Code
st.header("Ressource complémentaire")
st.write("Scannez ce QR code pour savoire plus sur l'option SLAM !")

qr_data = "https://www.onisep.fr/ressources/univers-formation/formations/post-bac/bts-services-informatiques-aux-organisations-option-b-solutions-logicielles-et-applications-metiers"
qr_code = generate_qr_code(qr_data)
st.image(qr_code, caption="Scannez-moi !", width=200)

st.write("[Cliquez ici si vous ne pouvez pas scanner le QR code.](https://www.onisep.fr/ressources/univers-formation/formations/post-bac/bts-services-informatiques-aux-organisations-option-b-solutions-logicielles-et-applications-metiers)")
