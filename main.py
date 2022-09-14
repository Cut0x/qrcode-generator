# Ici on import les modules que nous avons besoin
import pyqrcode;
import random;
from print_color import print;

# Ici on choisit le lien que l'on veut transformer en QR Code
choice = str(input('Entrez le lien que vous voulez mettre en QR Code : '));

# Ici on génère un identifiant pour le fichier du QR Code
id = random.randint(100,900)

# Ici on crée l'image
image = pyqrcode.create(choice)

# Ici on import l'image dans le dossier du code
image.png("QRCode-" + str(id) + ".png" ,scale=8)

# Ici on envoie un message de succès
print("QRCode-" + str(id) + ".png installé !", tag='SUCCES', tag_color='green', color='magenta')