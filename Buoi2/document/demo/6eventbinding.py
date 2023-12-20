import customtkinter


root = customtkinter.CTk()


root.title("hello techX")

root.geometry("600x400")


def eventClick(e, param):
    print(param)
    entry.insert(0, param)
    entry.insert("end", param)


def eventEnter(e):
    print("vô")


def eventLeave(e):
    print("ra")


def eventFocusIn(e):
    print("focus")
# button


def entryRelease(e):
    print(entry.get())


button = customtkinter.CTkButton(root, text="hãy chạm em")
button.pack()


entry = customtkinter.CTkEntry(root, placeholder_text="nhập vào đây")
entry.pack()
button.bind("<Button-1>", lambda e: eventClick(e, "ấn--"))

# vào diện tích của button
# button.bind("<Enter>", eventEnter)

# ra khỏi button
# button.bind("<Leave>", eventLeave)

# button.bind("<FocusIn>", eventFocusIn)

entry.bind("<KeyRelease>", entryRelease)


root.resizable(width=True, height=False)

root.mainloop()
