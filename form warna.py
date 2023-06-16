import tkinter
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo

#inisialisasi
window = tkinter.Tk()
window.configure(bg="#00ffff")
icon_img = PhotoImage(file='C:\\xampp2\\htdocs\\warna phyton\\asset\\cruelty-free.png')
window.iconphoto(False, icon_img)
window.geometry("400x350")
window.resizable(False,False)
window.title("DAFTAR")

# Header
header_label = ttk.Label(window,text="pengisian formulir",font=(16),background="pink",foreground="black") 
header_label.pack(pady=13)

#variabel dan function
NAMA_LENGKAP = tkinter.StringVar()
ALAMAT_RUMAH = tkinter.StringVar()
MAKANAN_FAVORIT = tkinter.StringVar()
MINUMAN_FAVORIT = tkinter.StringVar()
EMAIL = tkinter.StringVar()
PASSWORD = tkinter.StringVar()
password_confirmation = tkinter.StringVar()

# fungsi tombol
def tombol_click():
    if not NAMA_LENGKAP.get() or not ALAMAT_RUMAH.get() or not MAKANAN_FAVORIT.get() or not MINUMAN_FAVORIT.get() or not EMAIL.get() or not PASSWORD.get() or not password_confirmation.get():
        showinfo (title="Error",message="mohon di isi dengan benar!!!")
    else:
        pesan = f"Hallo {NAMA_LENGKAP.get()} Anda Telah Terdaftar Menjadi Member situs togel!!!"
        showinfo (title="Selamat jp",message=pesan)
# frame input
style = ttk.Style()
style.configure(style="TEntry", fieldbackground="#00fff")
input_frame = ttk.Frame(window)
# penempatan Grid, Pack, Place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)
# komponen)
nama_depan_label = ttk.Label(input_frame,text="NAMA LENGKAP : ")
nama_depan_label.pack(padx=10,fill="x",expand=True)
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_LENGKAP,style="costum.TEntry")
nama_depan_entry.pack(padx=10,fill="x",expand=True)

nama_depan_label = ttk.Label(input_frame,text="ALAMAT RUMAH : ")
nama_depan_label.pack(padx=10,fill="x",expand=True)
nama_depan_entry = ttk.Entry(input_frame,textvariable=ALAMAT_RUMAH,style="costum.TEntry")
nama_depan_entry.pack(padx=10,fill="x",expand=True)

nama_depan_label = ttk.Label(input_frame,text="MAKANAN FAVORIT : ")
nama_depan_label.pack(padx=10,fill="x",expand=True)
nama_depan_entry = ttk.Entry(input_frame,textvariable=MAKANAN_FAVORIT,style="costum.TEntry")
nama_depan_entry.pack(padx=10,fill="x",expand=True)

nama_depan_label = ttk.Label(input_frame,text="MINUMAN FAVORIT : ")
nama_depan_label.pack(padx=10,fill="x",expand=True)
nama_depan_entry = ttk.Entry(input_frame,textvariable=MINUMAN_FAVORIT,style="costum.TEntry")
nama_depan_entry.pack(padx=10,fill="x",expand=True)

nama_depan_label = ttk.Label(input_frame,text="EMAIL : ")
nama_depan_label.pack(padx=10,fill="x",expand=True)
nama_depan_entry = ttk.Entry(input_frame,textvariable=EMAIL,style="costum.TEntry")
nama_depan_entry.pack(padx=10,fill="x",expand=True)

nama_depan_label = ttk.Label(input_frame,text="PASSWORD : ")
nama_depan_label.pack(padx=10,fill="x",expand=True)
nama_depan_entry = ttk.Entry(input_frame,textvariable=PASSWORD,style="costum.TEntry")
nama_depan_entry.pack(padx=10,fill="x",expand=True)

nama_depan_label = ttk.Label(input_frame,text="Password Confirmation : ")
nama_depan_label.pack(padx=10,fill="x",expand=True)
nama_depan_entry = ttk.Entry(input_frame,textvariable=password_confirmation,style="costum.TEntry")
nama_depan_entry.pack(padx=10,fill="x",expand=True)

# tombol
tombol_daftar = ttk.Button(input_frame,text="Submit",command=tombol_click)
tombol_daftar.pack(fill="x",expand=True,padx=100,pady=10)

window.mainloop()
