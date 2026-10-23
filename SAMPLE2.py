from customtkinter import *
from PIL import Image
import fileanalysis
from tkinter import filedialog

def upload_file():
    file_name = filedialog.askopenfilename(
        title="Select a file",
        filetypes=(
            ("Capture Files", "*.pcap"), ("Capture Files", "*.cap"), ("Capture Files", "*.pcapng"),
        )
    )

    if file_name:
        try:
            with open(file_name, 'rb') as file:
                file_content = file.read()
                print(f"File content:\n{file_content}")

                file_label.configure(text=f"File Loaded: {file_name.split('/')[-1]} ✓", text_color="green")

                #put in analyze button and then call backend_fileanalysis
                
        except Exception as e:
            file_label.configure(text=f"Error: {str(e)}", text_color="red")

def save_file():
    output_filename = dil

#creates initial app window
app = CTk()
app.geometry("1000x800")
app.title("SharkScope")
app.grid_columnconfigure(0, weight=1)
set_appearance_mode("dark")


tcp_connection = BooleanVar()
udp_connection = BooleanVar()
icmp_connection = BooleanVar()
http_connection = BooleanVar()
https_tls_connection = BooleanVar()

#program window icon
icon = Image.open("sharkscope_logo.png")
icon.save("icon.ico", format="ICO", sizes=[(32, 32)])
app.iconbitmap("icon.ico")


#Top Title Label
label = CTkLabel(master=app, text="SharkScope", font=("Roboto", 28, "bold"), text_color="#029cff")
label.grid(row=4, column=0, padx=10, pady=10)

# Sub-Text label
label = CTkLabel(master=app, text="Submit the capture file you want to analyze:", font=("Roboto", 16), text_color="#029cff")
label.grid(row=5, column=0, padx=10, pady=10)

# Upload File button
img = Image.open("fileicon_white.png")
btn = CTkButton(master=app, text="Upload File", font=("Roboto", 20), corner_radius=32, image=CTkImage(dark_image=img, light_image=img), fg_color="#029cff", hover_color="#007ACC", width=300, height=50, command=upload_file)
btn.grid(row=6, column=0, padx=10, pady=10)

# File Text label
file_label = CTkLabel(master=app, text="", font=("Roboto", 16), text_color="#FFFFFF")
file_label.grid(row=7, column=0, padx=10, pady=10)


tcp_connection = CTkCheckBox(master=app, text="TCP", font=("Roboto", 16), variable=tcp_connection, text_color="#029cff")
tcp_connection.grid(row=8, column=0, padx=10, pady=10)

udp_connection = CTkCheckBox(master=app, text="UDP", font=("Roboto", 16), variable=udp_connection, text_color="#029cff")
udp_connection.grid(row=9, column=0, padx=10, pady=10)

icmp_connection = CTkCheckBox(master=app, text="ICMP", font=("Roboto", 16), variable=icmp_connection, text_color="#029cff")
icmp_connection.grid(row=10, column=0, padx=10, pady=10)

http_connection = CTkCheckBox(master=app, text="HTTP", font=("Roboto", 16), variable=http_connection, text_color="#029cff")
http_connection.grid(row=11, column=0, padx=10, pady=10)

https_tls_connection = CTkCheckBox(master=app, text="HTTPS/TLS", font=("Roboto", 16), variable=https_tls_connection, text_color="#029cff")
https_tls_connection.grid(row=12, column=0, padx=10, pady=10)

app.mainloop()