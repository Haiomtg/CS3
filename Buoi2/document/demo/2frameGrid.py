import customtkinter


root = customtkinter.CTk()


root.title("hello techX")

# root.geometry("600x400")


root.columnconfigure((0, 1), weight=1)

frame1 = customtkinter.CTkFrame(master=root, fg_color="yellow")
frame1.grid(row=0, column=0, sticky="nswe")

frame2 = customtkinter.CTkFrame(master=root, fg_color="red")
frame2.grid(row=1, column=1, sticky="nswe")


frame3 = customtkinter.CTkFrame(master=root, fg_color="blue")
frame3.grid(row=2, column=1, sticky="nswe")

root.mainloop()
