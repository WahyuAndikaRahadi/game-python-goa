import random

welcome_message = "WELCOME TO CUYPY GAMES!!"
cuy_position = random.randint(1, 4)

print("******************************")
print(f"** {welcome_message} **")
print("******************************")

name_user = input("masukan nama anda : ")

bentuk_goa = "|___|"
goa = [bentuk_goa] * 3
goa_null = goa.copy()
goa[cuy_position - 1]= "|🤖🔪|"


goa = ' '.join(goa)
goa_null = ' '.join(goa_null)

print(f'''Halo {name_user}! Coba Perhatikan goa dibawah ini
{goa_null}
      ''')
pilihan_user = int(input("Menurut kamu, goa yang aman untuk bersembunyi yang mana ? [1 / 2 / 3 ]:  "))
if pilihan_user > 4:
      print("Sudah Kubilang pilih dari 1-4 maaf program dihentikan silahkan ulangi lagi")
      exit()

konfirmasi = input(f"Apakah Anda Yakin Memilih goa nomor {pilihan_user} [Y/N] : ")

if konfirmasi == "N":
      print("maaf kamu memilih N Program akan dihentikan silahkan ulangi lagi..")
      exit()
elif konfirmasi == "Y":
      if pilihan_user != cuy_position:
            print(f"Selamat {name_user} Kamu Menang! posisi kamu saat ini aman untuk ditempati.beruntungnya kamu tidak memilih goa nomor {cuy_position} dan pilihanmu adalah goa nomor {pilihan_user} 🏆🏆 \n {goa} ")
            exit()
      elif pilihan_user == cuy_position:
            print(f"Maaf {name_user} Kamu kalah! kamu menebak goa nomor {pilihan_user} aman untuk ditempati tetapi goa nomor {cuy_position}  tidak selamat untuk ditinggali.Coba Lagi Lain kali {pilihan_user} ☠️☠️ \n {goa} ")
            exit()
      
else:
      print("maaf silahkan ulangi programnya lagi")
      exit()

      
