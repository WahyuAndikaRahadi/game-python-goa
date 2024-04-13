import random

welcome_message = "WELCOME TO CUYPY GAMES!!"
cuy_position = random.randint(1, 4)

print("******************************")
print(f"** {welcome_message} **")
print("******************************")

name_user = input("masukan nama anda : ")

bentuk_goa = "|___|"
goa = [bentuk_goa] * 4
goa_null = goa.copy()
goa[cuy_position - 1] = "|😁👋|"


goa = ' '.join(goa)
goa_null = ' '.join(goa_null)

print(f'''Halo {name_user}! Coba Perhatikan goa dibawah ini
{goa_null}
      ''')
pilihan_user = int(input("Menurut kamu, goa yang aku tempati yang mana? [1 / 2 / 3 / 4]:  "))
if pilihan_user > 4:
      print("Sudah Kubilang pilih dari 1-4 maaf program dihentikan silahkan ulangi lagi")
      exit()

konfirmasi = input(f"Apakah Anda Yakin Memilih goa nomor {pilihan_user} [Y/N] : ")

if konfirmasi == "N":
      print("maaf kamu memilih N Program akan dihentikan silahkan ulangi lagi..")
      exit()
elif konfirmasi == "Y":
      if pilihan_user == cuy_position:
            print(f"Selamat {name_user} Kamu Menang! kamu menemukan goa yang aku tempati berada di goa nomor {cuy_position} dan pilihanmu adalah goa nomor {pilihan_user} 🏆🏆 \n {goa} ")
            exit()
      elif pilihan_user != cuy_position:
            print(f"Maaf {name_user} Kamu kalah! kamu menebak goa nomor {pilihan_user} tetapi saya berada di goa nomor {cuy_position}.Coba Lagi Lain kali ☠️☠️ \n {goa} ")
            exit()
      
else:
      print("maaf silahkan ulangi programnya lagi")
      exit()

      
