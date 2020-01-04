from tkinter import *
from tkinter import messagebox
import time

var = messagebox.askquestion("Dikkat!", "Siberdeyiz'e Kayıtlımısın")
if var == "yes":
    messagebox.showinfo("Bilgilendirme!", "Profilim'e Bakmayı Unutmayın\n\tProfil Kullanıcı Adım : Mugo")
else:
    messagebox.showwarning("Uyarı!", "Siberdeyiz'e Kayıtlı Olmadan Kullanmanızı Önermem\n\tHem Efsane Site :D")
    exit()
defuser = "root"
defpass = "toor"
window = Tk()
window.title("Mugo Crack Tools | Giriş Yap")
window.geometry("500x250+400+250")


def destroy():
    label1.destroy()
    label2.destroy()
    label3.destroy()
    buton.destroy()
    stat.destroy()
    getuser.destroy()
    getpass.destroy()

def buttons():
    cikis = Button(window, text="Çıkış Yap", width="7", height="4", fg="white", bg="grey", command=lambda: exit())
    cikis.grid(row=0, column=0)
def mainpage():
    messagebox.showinfo("Bilgilendirme!", "Kodlayan Kişi (CODER): Mugo")
    window.title("Mugo Crack Tools | AnaSayfa")
    destroy()
    buttons()



def girisyap():
    ipass = getpass.get()
    iuser = getuser.get()
    if defuser == iuser and defpass == ipass:
        stat.config(text="Giriş Başarılı!", fg="green")
        time.sleep(0.5)
        mainpage()
    else:
        stat.config(text="Bilgiler Yanlış Tekrar Deneyin!", fg="red")
        time.sleep(0.5)


label1 = Label(window, text="Kullanıcı Adınızı Giriniz :   ")
getuser = Entry(window, width="20")
label2 = Label(window, text="Şifrenizi Giriniz :   ")
getpass = Entry(window, width="20", show="●")
buton = Button(window, text="      Giriş Yap      ", fg="Green", bg="Black", command=girisyap)
label3 = Label(window, text="Kullanıcı Adı ve Şifre Öğrenmek İçin Siberdeyiz Profilim'e Bakın!\nProfil İsmim : Mugo",
               fg="white", bg="black")
label1.grid(row=0, column=2)
getuser.grid(row=0, column=3)
label2.grid(row=1, column=2)
getpass.grid(row=1, column=3)
stat = Label(window, text="")
stat.grid(row=3, column=3)
buton.grid(row=3, column=2)
label3.grid(row=5, column=3)

window.mainloop()