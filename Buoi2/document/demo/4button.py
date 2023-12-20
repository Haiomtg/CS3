import customtkinter


root = customtkinter.CTk()


root.title("hello techX")

root.geometry("600x400")


def eventClick(param):
    print(param)


button = customtkinter.CTkButton(
    root, text="hãy chạm tôi", hover_color="red", command=lambda: eventClick("hehe"))
button.pack()

root.resizable(width=True, height=False)

root.mainloop()
