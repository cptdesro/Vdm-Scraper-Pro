# Vdm Scraper Pro
Ce processus vérifié à toutes les 12 heures si de nouvelles offres d'emplois ont été affichées sur le site des TI de la ville de Montréal.
 - Si de nouvelles offres sont présentes, un courriel est envoyé pour notifer l'utilisateur
 - Le processus recommencera dans 12 heures


# To run - Production
    1. S'assurer que la ligne productionServerStart(message) dans smtp.py est décommenté et que le debug est commenté
    2. Lancer le main 


# To run - DEBUG
    1. Ouvrir le server SMTP en local 
    - $ python -m smtpd -c DebuggingServer -n localhost:1025
    2. Dans le fichier smtp.py, décommenter # debugServerStart(message) et commenter productionServerStart(message)
    3. Lancer le main
    

# Todos
    - Faire rouler le processus dans le cloud
    - Encrypter les credentials
    - Si les nouvelles offres ont déjà été vues, ne pas envoyer de courriel
