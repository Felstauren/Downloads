import os, shutil

alter_pfad = r"C:\Users\janni\Downloads"
neuer_pfad_pdf = r"C:\Users\janni\OneDrive\Documents\pdf-Ordner"
neuer_pfad_png = r"C:\Users\janni\OneDrive\Documents\png-Ordner"
neuer_pfad_txt = r"C:\Users\janni\OneDrive\Documents\txt-Ordner"
neuer_pfad_csv = r"C:\Users\janni\OneDrive\Documents\csv-Ordner"
neuer_pfad_jar = r"C:\Users\janni\OneDrive\Documents\jar-Ordner"
neuer_pfad_doc = r"C:\Users\janni\OneDrive\Documents\doc-Ordner"
neuer_pfad_mp4 = r"C:\Users\janni\OneDrive\Documents\mp4-Ordner"
neuer_pfad_mp3 = r"C:\Users\janni\OneDrive\Documents\mp3-Ordner"
neuer_pfad_zip = r"C:\Users\janni\OneDrive\Documents\zip-Ordner"
neuer_pfad_pptx = r"C:\Users\janni\OneDrive\Documents\pptx-Ordner"
neuer_pfad_software = r"C:\Users\janni\OneDrive\Documents\software-Ordner"



while True:
    if len(os.listdir(alter_pfad)) > 0:
        for i in os.listdir(alter_pfad):
            dateiendung3 = i[-3:].lower()
            dateiendung4 = i[-4:].lower()

            if dateiendung3 == "pdf":
                shutil.move(f"{alter_pfad}\\{i}", f"{neuer_pfad_pdf}\\{i}")

            if dateiendung3 == "png" or dateiendung3 == "jpg" or dateiendung4 =="jpeg":
                shutil.move(f"{alter_pfad}\\{i}", f"{neuer_pfad_png}\\{i}")
            
            if dateiendung3 == "txt":
                shutil.move(f"{alter_pfad}\\{i}", f"{neuer_pfad_txt}\\{i}")
            
            if dateiendung3 == "csv":
                shutil.move(f"{alter_pfad}\\{i}", f"{neuer_pfad_csv}\\{i}")

            if dateiendung3 == "jar":
                shutil.move(f"{alter_pfad}\\{i}", f"{neuer_pfad_csv}\\{i}")

            if dateiendung4 == "docx" or dateiendung3 == "doc":
                shutil.move(f"{alter_pfad}\\{i}", f"{neuer_pfad_doc}\\{i}")

            if dateiendung3 == "mp4":
                shutil.move(f"{alter_pfad}\\{i}", f"{neuer_pfad_mp4}\\{i}")

            if dateiendung3 == "mp3":
                shutil.move(f"{alter_pfad}\\{i}", f"{neuer_pfad_mp3}\\{i}")

            if dateiendung3 == "exe" or dateiendung3 == "msi" or dateiendung4 =="webp" or dateiendung3 == "iso" or dateiendung4 =="temp" or dateiendung4 == "msix":
                shutil.move(f"{alter_pfad}\\{i}", f"{neuer_pfad_software}\\{i}")

            if dateiendung3 == "zip":
                shutil.move(f"{alter_pfad}\\{i}", f"{neuer_pfad_zip}\\{i}")

            if dateiendung4 == "ppsx" or dateiendung4 == "pptx":
                shutil.move(f"{alter_pfad}\\{i}", f"{neuer_pfad_pptx}\\{i}")