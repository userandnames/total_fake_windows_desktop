import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
# 背景
canvas = tk.Canvas(root, width=1200, height=699, bd=0, highlightthickness=0)
imgpath = 'changed.gif'
img = Image.open(imgpath)
img = img.resize((1200, 699))
photo = ImageTk.PhotoImage(img)


canvas.create_image(600, 349, image=photo)
canvas.pack()

# canvas.create_window(100, 50, width=100, height=20)

root.mainloop()