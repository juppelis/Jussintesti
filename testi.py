sana=input("kerro merkkijono: ")
haettavasana=input("mitä sanaa haetaan: ")
indeksi=sana.find(haettavasana)
if indeksi !=-1:
    print(indeksi)
    print(sana[indeksi:indeksi+len(haettavasana)])
else:
    print("haettavaa sanaa ei löytynyt")


sana[indeksi:indeksi+2]
sana[3]