import tkinter as tk


class MyWindow:
    def __init__(self, master):
        self.img = None
        self.master = master
        self.canvas = tk.Canvas(self.master, width=400, height=400, bg='black')
        self.set()

    def set(self):
        self.master.geometry('1200x699')
        self.create_canvas("gif/changed.gif")

    def create_canvas(self, path):
        self.canvas.place(x=50, y=50)  # 使用place方法将Canvas放置到窗口上
        self.img = tk.PhotoImage(file=path)
        self.canvas.create_image(100, 100, image=self.img)  # 使用create_image方法在Canvas上添加图片
        self.canvas.create_line(0, 0, 200, 200, fill='blue')
        self.canvas.create_rectangle(50, 50, 150, 150, fill='red')


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Window")

    my_window = MyWindow(root)

    root.mainloop()
