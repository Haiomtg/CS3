import customtkinter


root = customtkinter.CTk()


root.title("hello techX")

root.geometry("600x400")

# Check box --------------------------------------------------


def checkbox_event():
    print("checkbox toggled, current value:", check_var.get())


check_var = customtkinter.BooleanVar(value=True)
checkbox = customtkinter.CTkCheckBox(root, text="CTkCheckBox", command=checkbox_event,
                                     variable=check_var, onvalue=True, offvalue=False)
checkbox.pack(pady=(0, 50))

# Combo box --------------------------------------------------


def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)


combobox = customtkinter.CTkComboBox(root, values=["option 1", "option 2"],
                                     command=combobox_callback)
combobox.set("option 2")

combobox.pack(pady=(0, 50))

# OptionMenu --------------------------------------------------


def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)


optionmenu = customtkinter.CTkOptionMenu(root, values=["option 1", "option 2"],
                                         command=optionmenu_callback)
optionmenu.set("option 2")

optionmenu.pack(pady=(0, 50))

# process bar --------------------------------------------------
progressbar = customtkinter.CTkProgressBar(root, orientation="horizontal")
progressbar.pack(pady=(0, 50))

progressbar.set(0.3)

print("progressbar", progressbar.get())

# radio button --------------------------------------------------


def radiobutton_event():
    print("radiobutton toggled, current value:", radio_var.get())


radio_var = customtkinter.IntVar(value=0)
radiobutton_1 = customtkinter.CTkRadioButton(root, text="CTkRadioButton 1",
                                             command=radiobutton_event, variable=radio_var, value=1)
radiobutton_2 = customtkinter.CTkRadioButton(root, text="CTkRadioButton 2",
                                             command=radiobutton_event, variable=radio_var, value=2)

radiobutton_1.pack(side="left")
radiobutton_2.pack(side="left")

# SegmentedButton  --------------------------------------------------


def segmented_button_callback(value):
    print("segmented button clicked:", value)


segemented_button = customtkinter.CTkSegmentedButton(root, values=["Value 1", "Value 2", "Value 3"],
                                                     command=segmented_button_callback)
segemented_button.set("Value 1")

segemented_button.pack(side="top")

# Slider  --------------------------------------------------


def slider_event(value):
    print(value)


slider = customtkinter.CTkSlider(root, from_=0, to=100, command=slider_event)
slider.pack()

# Switch  --------------------------------------------------


def switch_event():
    print("switch toggled, current value:", switch_var.get())


switch_var = customtkinter.StringVar(value="on")
switch = customtkinter.CTkSwitch(root, text="CTkSwitch", command=switch_event,
                                 variable=switch_var, onvalue="on", offvalue="off")

switch.pack()

# tab view  --------------------------------------------------

tabview = customtkinter.CTkTabview(master=root)
tabview.pack(padx=20, pady=20)

frame1 = tabview.add("tab 1")  # add tab at the end
frame2 = tabview.add("tab 2")  # add tab at the end
tabview.set("tab 2")  # set currently visible tab

button = customtkinter.CTkButton(frame1, text="thuộc frame 1")
button.pack(padx=20, pady=20)

# text box
textbox = customtkinter.CTkTextbox(root)

textbox.insert("0.0", "new text to insert")  # insert at line 0 character 0
# get text from line 0 character 0 till the end
text = textbox.get("0.0", "end")
textbox.delete("0.0", "end")  # delete all text
# textbox.configure(state="disabled")  # configure textbox to be read-only

textbox.pack()

root.mainloop()
