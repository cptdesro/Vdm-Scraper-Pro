# Vdm Scraper Pro
Ce processus vérifié à toutes les 12 heures si de nouvelles offres d'emplois ont été affichées sur le site des TI de la ville de Montréal.
 - Si de nouvelles offres sont présentes, un courriel est envoyé pour notifer l'utilisateur
 - Le processus recommencera dans 12 heures


# To run - Production (Google Cloud Plateform)
    1. S'assurer que la ligne productionServerStart(message) dans smtp.py est décommenté et que le debug est commenté
        2.1 S'assurer que la version de pip est à jour : 
            $ curl https://bootstrap.pypa.io/get-pip.py | python
        2.2 Installer les dépendences du fichier requirements :
            $ pip install -r requirements.txt
        2.3 Pour que le script roule à l'infini dans la VM, le faire rouler dans tmux:
            $ tmux
            2.3.1 Rouler l'environnement python virtuel : $ source venv/bin/activate
            $ python3 main.py
        2.4 Ce détaché du processus tmux:
            $ CRTL + B and type :detach
            Fermer la console ssh, le processus roule.
        2.5 Si on veut revoir le processus : 
            2.5.1 Reconnection à la console ssh de la VM
            2.5.2 $ tmux attach
            2.5.3 si on veut kill : CTRL + B and type :kill-session
    
            
     


# To run - DEBUG
    1. Ouvrir le server SMTP en local 
    - $ python -m smtpd -c DebuggingServer -n localhost:1025
    2. Dans le fichier smtp.py, décommenter # debugServerStart(message) et commenter productionServerStart(message)
    3. Lancer le main
    

# Todos
    - plugger le github dans le cloud ssh
    - Si les nouvelles offres ont déjà été vues, ne pas envoyer de courriel
