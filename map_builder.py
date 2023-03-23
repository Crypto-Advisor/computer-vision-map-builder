import tkinter as tk
from PIL import Image

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800

def convert_to_image(w):
    w.postscript(file="map.ps", colormode='color')
    img = Image.open("map.ps")
    img.save("map.png", "PNG")

def set_mode(mode, w):
    if mode == 0:
        w.bind("<B1-Motion>", lambda event: draw(event, w))
    elif mode == 1:
        w.bind("<B1-Motion>", lambda event: obstacle(event, w))
        
    
def draw(event, w):
    x, y = event.x, event.y
    w.create_oval(x-5, y-5, x+5, y+5, fill="black", width=0)
    
def obstacle(event, w):
    x, y = event.x, event.y
    w.create_rectangle(x-5, y-5, x+5, y+5, fill="red", width=0)


def main():
    root = tk.Tk()

    root.geometry("800x800")
    root.title("Map Builder")

    w = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    
    label = tk.Label(root, text="Map Builder", font=("Arial", 20))
    label.pack(padx=10, pady=10)

    button = tk.Button(root, bg='white', text="Draw", command=lambda: set_mode(0, w))
    button.pack(padx=10, pady=10)

    button = tk.Button(root, bg='white', text="Obstacle", command=lambda: set_mode(1, w))
    button.pack(padx=10, pady=10)
    
    button = tk.Button(root, bg='white', text="Convert To Image", command=lambda: convert_to_image(w))
    button.pack(padx=10, pady=10)

   
    w.pack(expand=tk.YES, fill=tk.BOTH)


    root.mainloop()
    
main()
