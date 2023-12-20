import customtkinter

root = customtkinter.CTk()

root.title("tech X")

# master phu thuoc vao ai
# pack de dua frame hoac widget len giao dien 
# expand cho phep mo rong, fillx chiem het chieu ngang, filly chiem het chieu doc 
# fill = "both" chiem het 2 chieu 
frame = customtkinter.CTkFrame(master=root, fg_color="yellow")
frame.pack()
frame = customtkinter.CTkFrame(master=root, fg_color="red")
frame.pack()

# Tao chieu dai chieu cao cho ung dung
root.geometry("600x400")

root.resizable(width=True, height=False)

root.mainloop()
#pip3 install packaging