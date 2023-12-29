import customtkinter

root = customtkinter.CTk()

root.title("tech X")

# Tao chieu dai chieu cao cho ung dung
root.geometry("600x400")

root.columnconfigure((0, 1), weight=1)
root.rowconfigure(0, weight=1)

framTop1 = customtkinter.CTkFrame(master=root, fg_color="yellow")
framTop1.grid(column=0, row=0, sticky="nswe")
framTop2 = customtkinter.CTkFrame(master=root, fg_color="red")
framTop2.grid(column=1, row=0, sticky="nswe")

framBot1 = customtkinter.CTkFrame(master=root, fg_color="gray")
framBot1 .grid(column=0, row=1, sticky="nswe")
framBot2 = customtkinter.CTkFrame(master=root, fg_color="blue")
framBot2.grid(column=1, row=1, sticky="nswe")

root.resizable(width=True, height=False)

root.mainloop()
#pip3 install packaging