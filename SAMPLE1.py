from customtkinter import *
from PIL import Image
import fileanalysis
import threading 
from tkinter import filedialog

def upload_file():
    file_name = filedialog.askopenfilename(
        title="Select a file",
        filetypes=(("Capture Files", "*.pcap .cap")),
    )

    if file_name:
        try:
            with open(file_name, 'r') as file:
                file_content = file.read()
                print(f"File content:\n{file_content}")

                file_label.configure(text=f"✓ Loaded: {filename.split('/')[-1]}", 
                               text_color="green")
        except:
            False

        print(f"Selected file: {file_name}")
        # Do something with the file
        #file_label.configure(text=f"Selected: {filename}")

def start_ui():
    btn.grid_forget()
    progress.grid(row=8, column=0, padx=10, pady=10)
    progress.set(0.1)
    progress.start()

    thread = threading.Thread(target=run_backend, daemon=True)
    thread.start()

def run_backend():
    success_label.configure(text="")
    output_label.configure(text="")

    try:
        num = int(input_email_count)
        if num <= 0:
            app.after(0, lambda: error_label.configure(
                text="Please enter a positive integer"
            ))
            app.after(0, stop_ui)
            return

        service = fileanalysis.establish_gmail_token()
        filtered_emails = fileanalysis.clean_messages(service, input_label_name, input_email_count)

        app.after(0, lambda: finish_program(filtered_emails, input_label_name))

    except ValueError:
        app.after(0, lambda: error_label.configure(
            text="Please enter a valid integer"
        ))
        app.after(0, stop_ui)

def stop_ui():
    progress.stop()
    progress.grid_forget()
    btn.grid(row=5, column=0, padx=10, pady=10)

def finish_program(result, label_name):
    stop_ui()
    error_label.configure(text="")
    success_label.configure(text="Inbox Cleaned!")
    output_label.configure(
        text=f"Over {result} emails were filtered into {label_name}!"
    )

#set up initial app window parameters
app = CTk()
app.geometry("1000x800")
app.title("SharkScope")
app.grid_columnconfigure(0, weight=1)
set_appearance_mode("dark")

'''
#window icon
icon = Image.open("mail_icon_sienna.png")
icon.save("icon.ico", format="ICO", sizes=[(32, 32)])
app.iconbitmap("icon.ico")
'''

#Top Title Label
label = CTkLabel(master=app, text="SharkScope", font=("Roboto", 28, "bold"), text_color="#029cff")
label.grid(row=0, column=0, padx=10, pady=10)

# Number of emails label
label = CTkLabel(master=app, text="Submit the file you want to analyze (must be .pcap or .cap)", font=("Roboto", 16), text_color="#029cff")
label.grid(row=1, column=0, padx=10, pady=10)

# Submit button
#img = Image.open("mail_icon_white.png")
btn = CTkButton(master=app, text="Upload File!", font=("Roboto", 20), corner_radius=32, fg_color="#029cff", hover_color="#eba37f", width=300, height=50, command=start_ui) #image=CTkImage(dark_image=img, light_image=img),
btn.grid(row=5, column=0, padx=10, pady=10)

#Loading animation creation & start
progress = CTkProgressBar(master=app, orientation="horizontal", mode="indeterminate", width=300, progress_color="#ef8450") 

# Displays an error label if conditions are met
error_label = CTkLabel(master=app, text="", font=("Roboto", 14), text_color="red")
error_label.grid(row=6, column=0, padx=10, pady=5)

# Displays a success label if program runs successfully
success_label = CTkLabel(master=app, text="", font=("Roboto", 14), text_color="green")
success_label.grid(row=6, column=0, padx=10, pady=5)

# Output Label (displays after program runs successfully)
output_label = CTkLabel(master=app, text="", font=("Roboto", 18, "bold"), text_color="white")
output_label.grid(row=7, column=0, padx=10, pady=5)

app.mainloop()



import pyshark

#use either scapy, pyshark, or dkpt
#want to create a traffic report OR stream of traffic

#imports the specific file
cap = pyshark.FileCapture("./sample_capture_files/telnet-cooked.pcap") # put input statement here

#analyzes the specific packet count, and subtracts by one so that people only enter integers
packet_number = int(input("Which packet # do you want to examine? "))
packet_number -= 1
selected_packet = print(cap[packet_number])

selected_packet['ip']