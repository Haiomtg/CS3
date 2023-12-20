import customtkinter


root = customtkinter.CTk()


root.title("hello techX")

root.geometry("600x400")


def getValue():
    value = entry.get()
    print(value)


entry = customtkinter.CTkEntry(master=root, placeholder_text="xin chào")
entry.pack(fill="x")


button = customtkinter.CTkButton(
    master=root, text="get value entry", command=getValue)
button.pack()
root.resizable(width=True, height=False)

root.mainloop()
