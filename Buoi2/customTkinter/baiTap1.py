import customtkinter

root = customtkinter.CTk()

root.title("tech X")

# Tao chieu dai chieu cao cho ung dung
root.geometry("600x400")
framTop = customtkinter.CTkFrame(master=root, fg_color="gray")
framTop.pack(expand=True, fill="both")

framBot = customtkinter.CTkFrame(master=root, fg_color="yellow")
framBot.pack(expand=True, fill="both")

framTop1 = customtkinter.CTkFrame(master=framTop, fg_color="yellow")
framTop1.pack(side="left", expand=True, fill="both")
framTop2 = customtkinter.CTkFrame(master=framTop, fg_color="red")
framTop2.pack(side="left", expand=True, fill="both")

framBot1 = customtkinter.CTkFrame(master=framBot, fg_color="gray")
framBot1 .pack(side="left", expand=True, fill="both")
framBot2 = customtkinter.CTkFrame(master=framBot, fg_color="blue")
framBot2.pack(side="left", expand=True, fill="both")

root.resizable(width=True, height=False)

root.mainloop()
#pip3 install packaging