# Application de découverte SLAM

Bienvenue dans l'application interactive de découverte de l'option SLAM (Solutions Logicielles et Applications Métiers) ! Cette application a pour objectif de présenter le domaine SLAM, ses compétences clés et de vous aider à découvrir si cette option est faite pour vous à travers un quiz interactif.

## Fonctionnalités principales

### 1. **Présentation de l'option SLAM**
L'application commence par une introduction à l'option SLAM, mettant en avant :
- Les compétences clés comme l'analyse des besoins, le développement logiciel, et la gestion de bases de données.
- Les outils utilisés, comme Python.

### 2. **Quiz interactif**
Un quiz composé de 20 questions permet de déterminer votre affinité avec l'option SLAM. Chaque question propose plusieurs choix, et votre score final vous donne une indication :
- **15 points ou plus** : Vous avez un profil idéal pour l'option SLAM.
- **Entre 10 et 14 points** : Vous pourriez réussir avec un peu d'effort.
- **Moins de 10 points** : Vous pouvez envisager d'autres options.

### 3. **QR Code**
Un QR code est généré dynamiquement pour vous rediriger vers une page complémentaire contenant plus d'informations sur l'option SLAM et les opportunités qu'elle offre.

## Installation et exécution

### Prérequis
- Python 3.8 ou une version ultérieure
- Les bibliothèques suivantes :
  - `streamlit`
  - `pyqrcode`

### Installation
1. Clonez le dépôt ou copiez le code source.
2. Installez les dépendances en utilisant pip :
   ```bash
   pip install streamlit pyqrcode
   ```

### Exécution
1. Lancez l'application Streamlit :
   ```bash
   streamlit run app.py
   ```
2. Ouvrez votre navigateur à l'adresse [http://localhost:8501](http://localhost:8501).

## Structure du code

### Génération de QR Code
La fonction `generate_qr_code(data)` utilise la bibliothèque `pyqrcode` pour créer un QR code à partir d'une URL.

### Interface utilisateur
- **Streamlit** : Le framework Streamlit est utilisé pour créer une interface interactive avec des titres, des images, et des boutons.
- **Questions du quiz** : Les questions sont affichées dynamiquement avec des options, et les réponses augmentent le score selon l'affinité avec l'option SLAM.

### Résultats du quiz
Les résultats sont affichés à l'utilisateur sous forme de messages de succès, d'informations ou d'avertissements en fonction du score obtenu.

## Contribuer
Si vous souhaitez améliorer cette application, n'hésitez pas à proposer des modifications ou à ajouter des fonctionnalités comme :
- Plus de questions dans le quiz.
- Des graphiques pour visualiser les résultats.
- Un contenu plus détaillé sur les compétences SLAM.

## Auteur
Cette application a été développée pour aider les étudiants à découvrir l'option SLAM de manière interactive et ludique.

## Licence
Ce projet est sous licence MIT. Vous êtes libre de l'utiliser et de le modifier selon vos besoins.

