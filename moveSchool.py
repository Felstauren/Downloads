# move file from downloads to ...

import os, shutil, time
import os.path 
from os import path

alter_pfad = r"C:\Users\janni\Downloads"
neuer_pfad_Biologie = r"D:\Schule\Bio\Moodle\2024\\"
neuer_pfad_Chemie = r"D:\Schule\Chemie\Moddle\2024\\"
neuer_pfad_Deutsch = r"D:\Schule\Deutsch\Moddle\2024\\"
neuer_pfad_Englisch = r"D:\Schule\Englisch\Moddle\2024\\"
neuer_pfad_Italienisch = r"D:\Schule\Italienisch\Moodle\2024\\"
neuer_pfad_Mathematik = r"D:\Schule\Mathe\Moodle\2024\\"
neuer_pfad_Geschichte = r"D:\Schule\Geschichte\Moodle\2024\\"

date = (time.strftime("%d.%m.%Y"))


while True:
    if len(os.listdir(alter_pfad)) > 0:
        for i in os.listdir(alter_pfad):

            if i.startswith("Bio"):
                if path.exists(neuer_pfad_Biologie + date):
                    shutil.move(f"{alter_pfad}\\{i}", f"{neuer_pfad_Biologie + date}\\{i}")
                else:
                    os.makedirs( neuer_pfad_Biologie + date)
                    shutil.move(f"{alter_pfad}\\{i}", f"{neuer_pfad_Biologie + date}\\{i}")

            if i.startswith("Che"):
                if path.exists(neuer_pfad_Chemie + date):
                    shutil.move(f"{alter_pfad}\\{i}", f"{neuer_pfad_Chemie + date}\\{i}")
                else: 
                    os.makedirs( neuer_pfad_Chemie + date)
                    shutil.move(f"{alter_pfad}\\{i}", f"{neuer_pfad_Chemie + date}\\{i}")
            
            if i.startswith("Deu"):
                if path.exists(neuer_pfad_Deutsch + date):
                    shutil.move(f"{alter_pfad}\\{i}", f"{neuer_pfad_Deutsch + date}\\{i}")
                else:
                    os.makedirs(neuer_pfad_Deutsch + date)
                    shutil.move(f"{alter_pfad}\\{i}", f"{neuer_pfad_Deutsch + date}\\{i}")
            
            if i.startswith("Eng"):
                if path.exists(neuer_pfad_Englisch + date):
                    shutil.move(f"{alter_pfad}\\{i}", f"{neuer_pfad_Englisch + date}\\{i}")
                else:
                    os.makedirs(neuer_pfad_Englisch + date)
                    shutil.move(f"{alter_pfad}\\{i}", f"{neuer_pfad_Englisch + date}\\{i}")

            if i.startswith("Ital"):
                if path.exists(neuer_pfad_Italienisch + date):
                    shutil.move(f"{alter_pfad}\\{i}", f"{neuer_pfad_Italienisch + date}\\{i}")
                else:   
                    os.makedirs(neuer_pfad_Italienisch + date)
                    shutil.move(f"{alter_pfad}\\{i}", f"{neuer_pfad_Italienisch + date}\\{i}")

            if i.startswith("Math"):
                if path.exists(neuer_pfad_Mathematik + date):
                    shutil.move(f"{alter_pfad}\\{i}", f"{neuer_pfad_Mathematik + date}\\{i}")
                else:
                    os.makedirs(neuer_pfad_Mathematik + date)
                    shutil.move(f"{alter_pfad}\\{i}", f"{neuer_pfad_Mathematik + date}\\{i}")

            if i.startswith("Ges"):
                if path.exists(neuer_pfad_Geschichte + date):
                    shutil.move(f"{alter_pfad}\\{i}", f"{neuer_pfad_Geschichte + date}\\{i}")
                else:
                    os.makedirs(neuer_pfad_Geschichte + date)
                    shutil.move(f"{alter_pfad}\\{i}", f"{neuer_pfad_Geschichte + date}\\{i}")



