from random import randint
import string, random
from pystyle import *
import os

def main():
    os.system("title Toolise")
    banner = """
      ███      ▄██████▄   ▄██████▄   ▄█        ▄█     ▄████████    ▄████████
  ▀█████████▄ ███    ███ ███    ███ ███       ███    ███    ███   ███    ███
     ▀███▀▀██ ███    ███ ███    ███ ███       ███▌   ███    █▀    ███    █▀
      ███   ▀ ███    ███ ███    ███ ███       ███▌   ███         ▄███▄▄▄
      ███     ███    ███ ███    ███ ███       ███▌ ▀███████████ ▀▀███▀▀▀
      ███     ███    ███ ███    ███ ███       ███           ███   ███    █▄
      ███     ███    ███ ███    ███ ███▌    ▄ ███     ▄█    ███   ███    ███
    ▄████▀    ▀██████▀   ▀██████▀  █████▄▄██ █▀    ▄████████▀    ██████████
                                   ▀
    """
    Anime.Fade(Center.Center(banner), Colors.black_to_white, Colorate.Vertical, enter=True)
def intop():
    white = Col.white
    gray = Col.gray
    top = """
      ███      ▄██████▄   ▄██████▄   ▄█        ▄█     ▄████████    ▄████████
  ▀█████████▄ ███    ███ ███    ███ ███       ███    ███    ███   ███    ███
     ▀███▀▀██ ███    ███ ███    ███ ███       ███▌   ███    █▀    ███    █▀
      ███   ▀ ███    ███ ███    ███ ███       ███▌   ███         ▄███▄▄▄
      ███     ███    ███ ███    ███ ███       ███▌ ▀███████████ ▀▀███▀▀▀
      ███     ███    ███ ███    ███ ███       ███           ███   ███    █▄
      ███     ███    ███ ███    ███ ███▌    ▄ ███     ▄█    ███   ███    ███
    ▄████▀    ▀██████▀   ▀██████▀  █████▄▄██ █▀    ▄████████▀    ██████████
                                   ▀
    """
    print(Colorate.Vertical(Colors.DynamicMIX((Col.gray, Col.white)), Center.XCenter(top)))
    tool = f"""
                                            ╔════════════════════════════╗
                                            ║ {white}[{gray}1{white}]Générateur              ║ 
                                            ║ {white}[{gray}2{white}]Cryter                  ║
                                            ╚════════════════════════════╝
    """
    print(Center.XCenter(tool))
    choix = int(input(f"""{white} [{gray}?{white}] Entrer votre choix {gray}-> """).replace('"','').replace("'",""))
    if choix == 1:
        def spawn():
            os.system("title Lock")
            blue = Col.gray
            lblue = Col.white
            banner = """
                           &&&&&&&&&&&&&                  
                        &&&&&&&&&&&&&&&&&&&               
                      %&&&&&&(       .&&&&&&&             
                     (&&&&&             &&&&&&            
                     &&&&&/              &&&&&            
                     &&&&&/              &&&&&            
                     &&&&&/              &&&&&            
                   &&&&&&&&&&&&&&&&&&&&&&&&&&&&&          
                  &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&(        
                 (&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&        
                 (&&&&&&&&&&&&&     %&&&&&&&&&&&&&        
                 (&&&&&&&&&&&&       &&&&&&&&&&&&&        
                 (&&&&&&&&&&&&&     %&&&&&&&&&&&&&        
                 (&&&&&&&&&&&&&&   %&&&&&&&&&&&&&&        
                 (&&&&&&&&&&&&&&   %&&&&&&&&&&&&&&        
                 (&&&&&&&&&&&&&&   &&&&&&&&&&&&&&&        
                 /&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&        
                  %&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&         
                     ,&&&&&&&&&&&&&&&&&&&&&&&/  
                """
            Anime.Fade(Center.Center(banner), Colors.black_to_white, Colorate.Vertical, enter=True)

            mdp = randint(1, 9)
            mdp2 = randint(1, 9)
            mdp3 = randint(1, 9)
            rstr = random.choice(string.ascii_letters)
            rstr2 = random.choice(string.ascii_letters)
            rstr3 = random.choice(string.ascii_letters)
            rstr4 = random.choice(string.ascii_letters)
            rstr5 = random.choice(string.ascii_letters)

            top = (""" 
        ▄█        ▄██████▄   ▄████████    ▄█   ▄█▄ 
        ███       ███    ███ ███    ███   ███ ▄███▀ 
        ███       ███    ███ ███    █▀    ███▐██▀   
        ███       ███    ███ ███         ▄█████▀    
        ███       ███    ███ ███        ▀▀█████▄    
        ███       ███    ███ ███    █▄    ███▐██▄   
        ███▌    ▄ ███    ███ ███    ███   ███ ▀███▄ 
        █████▄▄██  ▀██████▀  ████████▀    ███   ▀█▀ 
        ▀                                 ▀   

              ╔════════════════════════════╗
              ║ [1]Générer un mdp [2]Exit  ║
              ╚════════════════════════════╝
                    """)
            print(Colorate.Vertical(Colors.DynamicMIX((Col.gray, Col.white)), Center.XCenter(top)))
            choix = int(input(f"""{lblue} [{blue}?{lblue}] {blue} Votre choix  {lblue}-> """).replace('"', '').replace("'",
                                                                                                                   ""))
            if choix == 1:
                result1 = (f""" Votre Mot de Passe est --> {rstr}{rstr2}{rstr3}{rstr4}{rstr5}{mdp}{mdp2}{mdp3} """)
                print(result1)
                rep = input(
                    f"""{lblue} [{blue}?{lblue}] {blue} Voulez-vous creer un fichier [O/N]  {lblue}-> """).replace('"',
                                                                                                                   '')
                if rep == "O":
                    repcrypter = input(f"""{lblue} [{blue}?{lblue}] {blue} Voulez-vous creer un fichier crypter [O/N]  {lblue}-> """)
                    if repcrypter == "O":
                        Name = input(f"""{lblue} [{blue}?{lblue}] {blue} Entrer le nom du fichier final {lblue}-> """)
                        message = ([(ord(i) - 8) for i in result1])
                        message_décodé = [chr(i) for i in message]
                        final = "".join(message_décodé)
                        file = open(Name, "w+")
                        file.write(final)
                    if repcrypter == "N":
                        Name = input(f"""{lblue} [{blue}?{lblue}] {blue} Entrer le nom du fichier final {lblue}-> """)
                        file = open(Name, "w+")
                        file.write(result1)
                if rep == "N":
                    input()
                    exit()
            if choix == 2:
                exit()
            elif choix >= 3:
                input(f""" {Col.Symbol('!', blue, lblue)} {Col.light_red}Choix Invalide!{Col.reset}""")
                spawn()
        spawn()
    if choix == 2:
        os.system("@title HOTO")

        def start():
            blue = Col.light_blue
            lblue = Colors.StaticMIX((Col.light_blue, Col.white, Col.white))
            banner = """
               ▄█    █▄     ▄██████▄      ███      ▄██████▄  
              ███    ███   ███    ███ ▀█████████▄ ███    ███ 
              ███    ███   ███    ███    ▀███▀▀██ ███    ███ 
             ▄███▄▄▄▄███▄▄ ███    ███     ███   ▀ ███    ███ 
            ▀▀███▀▀▀▀███▀  ███    ███     ███     ███    ███ 
              ███    ███   ███    ███     ███     ███    ███ 
              ███    ███   ███    ███     ███     ███    ███ 
              ███    █▀     ▀██████▀     ▄████▀    ▀██████▀ 

            """
            Anime.Fade(Center.Center(banner), Colors.blue_to_cyan, Colorate.Vertical, enter=True)
            hoto = """
               ▄█    █▄     ▄██████▄      ███      ▄██████▄  
              ███    ███   ███    ███ ▀█████████▄ ███    ███ 
              ███    ███   ███    ███    ▀███▀▀██ ███    ███ 
             ▄███▄▄▄▄███▄▄ ███    ███     ███   ▀ ███    ███ 
            ▀▀███▀▀▀▀███▀  ███    ███     ███     ███    ███ 
              ███    ███   ███    ███     ███     ███    ███ 
              ███    ███   ███    ███     ███     ███    ███ 
              ███    █▀     ▀██████▀     ▄████▀    ▀██████▀  

                     ╔════════════════════════════╗
                     ║  [1]Crypter [2]Décrypter   ║
                     ╚════════════════════════════╝
            """
            print(Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.cyan)), Center.XCenter(hoto)))
            print("\n")
            choix = input(f"""{lblue} [{blue}?{lblue}] {blue} Votre choix  {lblue}-> """).replace('"', '').replace("'",
                                                                                                                   "")
            if choix == "1":
                crypter = +1
            if choix == "2":
                crypter = +2
            if choix > "2":
                input(f""" {Col.Symbol('!', blue, lblue)} {Col.light_red}Choix Invalide!{Col.reset}""")
                start()
            text = input(f"""{lblue} [{blue}?{lblue}] {blue} Entrer votre text {lblue}-> """).replace('"', '').replace(
                "'", "")
            os.system("cls")
            print(Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.cyan)), Center.XCenter(hoto)))
            print("\n")
            counter = 0
            if crypter == 2:
                lock = input(
                    f"""{lblue} [{blue}?{lblue}] {blue} Voulez vous décrypter un mot de passe lock [O/N] {lblue}-> """)
                if lock.lower()[0:1] == "o":
                    counter = 1
            rep = input(f"""{lblue} [{blue}?{lblue}] {blue} Voulez-vous creer un fichier [O/N]  {lblue}-> """).replace(
                '"', '').replace("'", "")
            if rep == "O":
                finnom = input(
                    f"""{lblue} [{blue}?{lblue}] {blue} Entrer le nom du fichier final  {lblue}-> """)
                if counter == 0:
                    key = int(input(f"""{lblue} [{blue}?{lblue}] {blue} Entrer la clé de criptage {lblue}-> """))
                    if crypter == 1:
                        message = ([(ord(i) - key) for i in text])
                    if crypter == 2:
                        message = ([(ord(i) + key) for i in text])
                    message_décodé = [chr(i) for i in message]
                    final = "".join(message_décodé)
                    file = open(finnom, "w+")
                    file.write(final)
                    file.write("votre clée est :")
                    file.write(str(key))
                if counter == 1:
                    message = ([(ord(i) + 8) for i in text])
                    message_décodé = [chr(i) for i in message]
                    final = "".join(message_décodé)
                    file = open(finnom, "w+")
                    file.write(final)
            if rep == "N":
                if counter == 0:
                    key = int(
                        input(f"""{lblue} [{blue}?{lblue}] {blue} Entrer la clé de criptage {lblue}-> """).replace('"',
                                                                                                               '').replace(
                            "'", ""))
                    if crypter == 1:
                        message = ([(ord(i) - key) for i in text])
                    if crypter == 2:
                        message = ([(ord(i) + key) for i in text])
                    message_décodé = [chr(i) for i in message]
                    final = "".join(message_décodé)
                    input(final)
                    start()
                if counter == 1:
                    message = ([(ord(i) + 8) for i in text])
                    message_décodé = [chr(i) for i in message]
                    final = "".join(message_décodé)
                    input(final)
        start()
    elif choix >= 3:
        blue = Col.gray
        lblue = white
        input(f""" {Col.Symbol('!', blue, lblue)} {Col.light_red}Choix Invalide!{Col.reset}""")
        intop()
main()
intop()
