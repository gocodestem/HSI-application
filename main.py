#hsi mesuring script by yusuf bouaouina

import customtkinter as ctk

screen = ctk.CTk()

records = []

def casfunc():
    hsi = (0.7 * float(tempinput.get())) + (0.2 * float(humidity.get())) + 5
    if hsi < 40:
        rskl = 'safe'
    elif hsi > 40 and hsi < 59.9:
        rskl = 'caution'
    elif hsi > 60 and hsi < 79.9:
        rskl = 'Danger'
    elif hsi > 80:
        rskl = 'Extreme'    

    with open('recs.txt', 'w') as file:
        file.write(f'{day}, {tempinput.get()}, {humidity.get()}, {hsi}, {rskl}')
        file.close()
    print('succsees')

def main():
    global daynumb
    global tempinput
    global humidity
    screen.geometry('600x600')
    daynumb = ctk.CTkTextbox(screen ,40,40)
    daynumb.pack(pady= 20)
    tempinput = ctk.CTkEntry(screen,200 , placeholder_text= 'your temperatures go here')
    tempinput.pack()
    humidity = ctk.CTkEntry(screen, placeholder_text= 'humidity in percentage')
    humidity.pack(pady= 20)
    cas = ctk.CTkButton(screen, text = 'calculate and store', command=casfunc)
    cas.pack()
    screen.mainloop()





def wanrdow(error):
    newwind = ctk.CTk()
    newwind.geometry('200x200')
    text = ctk.CTkLabel(newwind, 100, 100, text=error)
    newwind.mainloop()

def daynum():
    global day
    day = daynumb.get()
    if daynumb is not int:
      wanrdow('the day number is not an integer please close this window and try again')  
    

if __name__ == "__main__":
    main()
