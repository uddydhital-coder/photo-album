 import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def show_info():
    """Displays an alert popup message."""
    messagebox.showinfo("Image Info", "This is a photo album app built with Python and Tkinter!")

def open_details_window():
    """Opens a new Toplevel window showing photo details."""
    details_window = tk.Toplevel(root)
    details_window.title("Photo Details")
    details_window.geometry("300x200")
    
    label_title = tk.Label(details_window, text="Photo Details", font=("Arial", 14, "bold"))
    label_title.pack(pady=10)
    
    details_text = "Name: Sample Image\nFormat: JPEG / PNG\nResolution: High Quality"
    label_info = tk.Label(details_window, text=details_text, justify="left")
    label_info.pack(pady=10)
    
    close_btn = tk.Button(details_window, text="Close", command=details_window.destroy)
    close_btn.pack(pady=10)

root = tk.Tk()
root.title("My Photo Album")
root.geometry("400x500")


title_label = tk.Label(root, text="My Photo Album", font=("Arial", 18, "bold"))
title_label.pack(pady=10)


try:
    
    original_img = Image.open("sample.jpg")
    resized_img = original_img.resize((300, 250))
    photo = ImageTk.PhotoImage(resized_img)
    
    img_label = tk.Label(root, image=photo)
    img_label.image = photo  # Keep a reference to prevent garbage collection
    img_label.pack(pady=10)
except Exception as e:
    # Fallback if image path is invalid
    img_label = tk.Label(root, text="[ Image Placeholder ]\nAdd a valid image path to display", bg="lightgray", width=35, height=12)
    img_label.pack(pady=10)


btn_info = tk.Button(root, text="Show Info Popup", command=show_info, bg="#4CAF50", fg="white", font=("Arial", 11))
btn_info.pack(pady=5)

btn_details = tk.Button(root, text="View Photo Details", command=open_details_window, bg="#2196F3", fg="white", font=("Arial", 11))
btn_details.pack(pady=5)


root.mainloop()
