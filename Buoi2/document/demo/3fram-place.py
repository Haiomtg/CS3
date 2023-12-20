import customtkinter


root = customtkinter.CTk()


root.title("hello techX")

root.geometry("600x400")


frame1 = customtkinter.CTkFrame(master=root, fg_color="yellow")
frame1.place(relwidth=0.5, relheight=1, relx=0, rely=0)
root.mainloop()
