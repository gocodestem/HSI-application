#hsi mesuring script by yusuf bouaouina

import customtkinter as ctk

screen = ctk.CTk()

records = []


def main():
    screen.geometry('600x600')
    daynum = ctk.CTkTextbox(screen ,40,40)
    daynum.config()
    tempinput = ctk.CTkEntry(screen, placeholder_text= 'your temperatures go here')
    tempinput.pack()
    screen.mainloop()


if __name__ == "__main__":
    main()
