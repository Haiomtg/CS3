import customtkinter


root = customtkinter.CTk()


root.title("hello techX")

root.geometry("600x400")


# master : phụ thuộc vào ai ?
#
frame = customtkinter.CTkFrame(master=root, fg_color="yellow")
# side định vị trí của frame theo thằng cha (root) , khi không khai báo thì mặc định top
# pady
frame.pack(side="left", expand=True, fill="both")


frameSp = customtkinter.CTkFrame(master=root, fg_color="red")
frameSp.pack(side="left", expand=True, fill="both")

root.mainloop()
