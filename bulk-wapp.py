#!/usr/bin/env python
# coding: utf-8

 
import time
import pyautogui as pg
import keyboard
import tkinter as tk
from tkinter import messagebox
import tkinter.filedialog as filedialog
import pandas as pd
from pynput.keyboard import Key, KeyCode, Listener

def exit_program(root):
    print("ejecutando destrucción de app")
    root.destroy()
    root.quit()

def wait_for_key():
    print("Program paused. Press SHIFT to continue...")
    keyboard.wait('shift')
    print("Continuing program execution.")    

# Function to display a pop-up message
def show_popup(message):
    root = tk.Tk()
    root.withdraw()
    root.wm_attributes("-topmost", 1)  # Set the window as topmost
    messagebox.showinfo("Instructions", message)
    root.destroy()

def get_coordinates(num_coordinates):
    #Function to capture multiple sets of mouse coordinates
    global image_flag
    print(f"Click on {num_coordinates} items...")
    coordinates = []
    if len(coordinates) == 0:
        show_popup("Pon tu cursor sobre el chat pineado y toca la tecla SHIFT, sin hacer click")
    
    while len(coordinates) <= num_coordinates:     
        if keyboard.is_pressed("shift"):
            print("Click detected...")
            x, y = pg.position()
            coordinates.append((x, y))
            print(f"Coordinate {len(coordinates)} captured: ({x}, {y})")

            if len(coordinates) == 1:
                show_popup("Abre un chat cualquiera, y posiciona el cursor sobre el chat para escribir, y toca la tecla SHIFT, sin hacer click")
            if len(coordinates) == 2:
                show_popup("Pon tu cursor sobre el link api y toca la tecla SHIFT, sin hacer click")
            if len(coordinates) == 3:
                if image_flag:
                    show_popup("Pon tu cursor sobre el botón de ADJUNTAR y toca la tecla SHIFT, sin hacer click")
            if len(coordinates) == 4:
                show_popup("Pon tu cursor sobre el botón de FOTOS Y VIDEOS y toca la tecla SHIFT, sin hacer click")

            # Pause for a moment to avoid detecting the same click multiple times
            time.sleep(0.5)

    return coordinates
    
    
def use_images(boolean):
    global image_flag
    global app
    app.destroy()
    image_flag = boolean
    print(image_flag , "antes crash")

    # ====== Basic settings ===========
    message = 'Line 1%0aLine 2'
    counter = 0
    num_coordinates = 2

    #Load excel file
    show_popup("Presione aceptar y seleccione el excel con los datos de contacto en la ventana emergente a continuación")
    excel_file = tk.Tk()
    excel_file.withdraw()
    excel_file.wm_attributes("-topmost", 1)
    excel_file_path = tk.filedialog.askopenfilename()
    excel_file.destroy()
    # print(excel_file_path)
    
    if image_flag:
        #Load image file
        num_coordinates = 5
#         show_popup("Presione aceptar y seleccione la imagen a utilizar en la ventana emergente a continuación")
#         image_file = tk.Tk()
#         image_file.withdraw()
#         image_file.wm_attributes("-topmost", 1)
#         image_file_path = tk.filedialog.askopenfilename()
#         image_file.destroy()
#         print(image_file_path)

        image_file_path = 'foto'
    
    # Convert excel to a list
    df = pd.read_excel(excel_file_path)
    col1, col2 = df.columns[:]
    int_phone_numbers = df[col1].to_list().copy()
    phone_numbers = list(map(str, int_phone_numbers))
    names = df[col2].to_list().copy()
    
    #Load .txt file
    show_popup("Seleccione su archivo .txt que contiene el mensaje para sus clientes")
    txt_file = tk.Tk()
    txt_file.withdraw()
    txt_file.wm_attributes("-topmost", 1)
    txt_file_path = tk.filedialog.askopenfilename()
    txt_file.destroy()
    with open(txt_file_path, encoding="utf8") as chat:
        chat_text = chat.read()

    
    # ===================== Open WAPP ====================
    # Call the function to display the pop-up message
    show_popup("Abre tu navegador de internet, y luego toca la tecla SHIFT")
    # Call the function to pause the program until SHIFT is pressed
    wait_for_key()
    time.sleep(1)

    # Open the tab and wait for it to load
    pg.hotkey('ctrl', 't')
    time.sleep(2)
    pg.typewrite('https://web.whatsapp.com/')
    pg.press('backspace')
    pg.press('enter')
    time.sleep(6)

    # Load image for the first time
    if image_flag:
        show_popup("Abre un chat cualquiera y envía la imagen que enviarás a tus clientes. Cuando termines de hacerlo, presiona SHIFT")
        wait_for_key()
    
    
    coords = get_coordinates(num_coordinates)
    
    #======== Bulk messaging ====================
    while True:
        for names, phone_number in zip(names, phone_numbers):
            
            if keyboard.is_pressed('shift'): 
                print("tocaste la tecla SHIFT")
                break 
            else:

                # Click on Chrome address bar then wait 1 second and click again to edit
                pg.click(coords[0])  # Open the pinned chat
                time.sleep(1)
                pg.click(coords[1])  # Prepare to write the API code

                # Type in the message, press enter, then wait for the page to load (8 sec) and click enter again to send the message
                pg.typewrite('https://api.whatsapp.com/send?phone=+' + phone_number)
                pg.press('enter')
                time.sleep(1)
                pg.click(coords[2])  # Open the link
                time.sleep(1)

                # Type the customized message
                pg.typewrite('Hola ' + names + ' ,¿como estás? Espero que bien!! ')
                pg.press('enter')
                pg.typewrite(chat_text)
                pg.press('enter')
                time.sleep(1)
                
                if keyboard.is_pressed('shift'): 
                    print("tocaste la tecla SHIFT")
                    break 
                
               # attach and send image
                if image_flag:                  
                    pg.click(coords[3])  # Click on the attachment button
                    time.sleep(1)
                    pg.click(coords[4])  # Click on the 'File' option
                    time.sleep(1)
                    pg.typewrite(image_file_path)  # Type the image file path
                    pg.press('enter')
                    time.sleep(1)
                    pg.press('enter')
                    time.sleep(1)

        # Close the tab
        pg.hotkey('ctrl', 'w')
        print("finished")
        # break loop
        break


#main
image_flag = None
app = tk.Tk()
app.geometry("500x300")
app.attributes("-topmost", 1)
app.title("Frich 'n Fries - Messenger'")
label = tk.Label(app, text ="Bulk messaging app - Frich 'n Fries'", font=('Arial',18))
label.pack(padx=20, pady=20)

yes_image = tk.Button(app, text="Utilizaré IMÁGENES+TEXTO", command=lambda: use_images(True))
yes_image.pack(padx=20, pady=20)

no_image = tk.Button(app, text="Utilizaré SOLO TEXTO", command=lambda: use_images(False))
no_image.pack(padx=20, pady=20)

exit_button = tk.Button(app, text="Cerrar", command=lambda: exit_program(app))
exit_button.pack(padx=20, pady=20)

app.mainloop()