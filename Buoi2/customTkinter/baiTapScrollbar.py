import customtkinter


class Frame(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master=master, fg_color="gray")

        for i in range(0, 1001):
            button = customtkinter.CTkButton(master=self, 
                                             bg_color="green",
                                             text=f"button {i} !")
            button.bind(
                "<Button-1>", lambda e, index=i: self.eventGetNumberButton(e, index))
            button.pack(pady=5)

    def eventGetNumberButton(self, e, id):
        print("id", id)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("techX")
        self.geometry("600x400")
        frame = Frame(self)
        frame.pack(expand=True, fill="both")


app = App()
app.mainloop()
