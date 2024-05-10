import os, colorama, webbrowser, time; from colorama import *

Görevler = []

class renkler:
    PEMBE = '\033[95m'
    MAVI = '\033[94m'
    CAMGOBEGI = '\033[96m'      ### İş Güzar Renkler :D
    YESIL = '\033[92m'
    SARI = '\033[93m'
    KIRMIZI = '\033[91m'
    DUZ = '\033[0m'
    KALIN = '\033[1m'
    ALTICIZILI = '\033[4m'

def addGörev():
  Görev = input("\nYeni Görevi Gir: ")
  Görevler.append(Görev)
  print(f"\033[92m\nGörev '{Görev}' başarıyla eklendi!.")


def listGörevler():
  if not Görevler:
    print("\033[91m\nGörev Ekledikten Sonra Basacan Emmi Ogli xd!!.")
  else:
    print("\033[92m\nHmm.Az-Çok Birşeyler Var Gibi Gözüküyor :) :")
    for index, Görev in enumerate(Görevler):
      print(f"\033[93m\nGörev #{index}. {Görev}")


def deleteGörev():
  listGörevler()
  try:
    GörevToDelete = int(input("Silmek için # girin: "))
    if GörevToDelete >= 0 and GörevToDelete < len(Görevler):
      Görevler.pop(GörevToDelete)
      print(f"\033[92m\nHelal Olsun! {GörevToDelete} Görevini Hakkınla Yerine Getirdin.")
    else:
      print(f"\033[91m\nBu adda #{GörevToDelete} bir görev bulamadım.")
  except:
    print("\033[91m\nHatalı Yazım.")

    
colors = ["31", "33", "32", "35", "36"]  # Renk Kodları Sağlayıcıları

if __name__ == "__main__":
  ### Uygulamayı Çalıştırmak İçin Bir Döngü Oluşturmak
  os.system('color D')
  
  os.system('cls')
  print("\033[1m\033[94m-==Yapılacaklar Listesine HG==- ")



  while True:
    print("\n")
    print("\033[95mGördüğün Üzere Seçenekler Burada")
    print("\033[92m------------------------------------------")
    print("\033[95m1. \033[93mYeni Görev Ekle!")
    print("\033[95m2. \033[93mGörevi Başarıyla Sil!")
    print("\033[95m3. \033[93mBana Listeyi Göster")
    print("\033[95m4. \033[93mListeyi Kaydet")
    print("\033[95m5. \033[93mÇıkış")

    Seçim = input("\033[92m\nSeçim: ")

    if (Seçim == "1"):
      addGörev()
    elif (Seçim == "2"):
      deleteGörev()
    elif (Seçim == "3"):
      listGörevler()
    elif (Seçim == "4"):
      listGörevler
      with open("Yapılacaklar Listesi.txt", "w") as file:
        for index, Görev in enumerate(Görevler):
          file.write(Görev + '\n')
      print(" \033[92m\nYapılacaklar Listesi Başarıyla Kaydedildi !")     
          
    elif (Seçim == "5"):
      break
    else:
      print("\033[91m\nHatalı Tuş. Mevcut Rakamlardan Birini Seç.")

  print("BayBayy 👋👋")
