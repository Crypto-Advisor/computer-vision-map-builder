import cv2
import os
import tkinter as tk
from tkinter import messagebox
import datetime
from PIL import Image, ImageTk

class WebcamGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Webcam Photo Capture")
        self.cap = cv2.VideoCapture(0)
        self.width, self.height = 640, 480
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        self.current_folder = None
        
        self.frame = tk.Frame(self.root, bg='#2c3e50', padx=10, pady=10)
        self.frame.pack(expand=True, fill='both')
        
        self.canvas = tk.Canvas(self.frame, width=self.width, height=self.height)
        self.canvas.pack(side='left', padx=10, pady=10)
        
        self.button1 = tk.Button(self.frame, text='Blocked', bg='#3498db', fg='black', font=('Arial', 12), command=self.save_to_blocked)
        self.button1.pack(side='top', fill='x', padx=10, pady=5)
        
        self.button2 = tk.Button(self.frame, text='Free', bg='#e74c3c', fg='black', font=('Arial', 12), command=self.save_to_free)
        self.button2.pack(side='top', fill='x', padx=10, pady=5)
        
        self.root.bind('<Escape>', lambda e: self.root.quit())
        
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        
        self.show_frame()
    
    def save_to_blocked(self):
        self.current_folder = os.getcwd() + '/data/blocked'
    
    def save_to_free(self):
        self.current_folder = os.getcwd() + '/data/free'
    
    def show_frame(self):
        _, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = cv2.resize(frame, (self.width, self.height))
        photo = ImageTk.PhotoImage(image=Image.fromarray(img))
        self.canvas.delete('all')
        self.canvas.image = photo
        self.canvas.create_image(0, 0, image=photo, anchor='nw')
        self.root.after(10, self.show_frame)
        if self.current_folder:
            filename = f'{self.current_folder}/{datetime.datetime.now().strftime("%Y%m%d-%H%M%S")}.jpg'
            cv2.imwrite(filename, frame)
            self.current_folder = None
            messagebox.showinfo('Saved', f'Image saved to {filename}')
    
    def close(self):
        self.cap.release()
        self.root.destroy()

if __name__ == '__main__':
    app = WebcamGUI()
    app.root.mainloop()
