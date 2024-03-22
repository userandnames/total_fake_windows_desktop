import tkinter as tk
import os
import json
from PIL import Image, ImageTk

img = None


class Fake_Win:
    def __init__(self, main_window):
        self.root_path = ''
        self.setting_path = ''
        self.settings = dict()
        self.background_photo = None

        self.init_settings()  # 初始化路径设置

        self.root = main_window
        self.size = [self.root.winfo_screenwidth(), self.root.winfo_screenheight()]
        self.canvas_root = tk.Canvas(self.root, width=int(self.size[0]), height=int(self.size[1]), bg="black")
        self.canvas_root.place(x=0, y=0)
        if self.set():
            self.set_background(self.settings["background_pic"])

    def init_settings(self):
        self.root_path = os.getcwd()
        self.setting_path = self.root_path + "\\settings"
        subdir = os.listdir(self.setting_path)
        for i in subdir:
            if os.path.isdir(self.setting_path + "\\" + i):
                self.settings[i] = os.listdir(self.setting_path + "\\" + i)

    def set(self):
        # self.root.attributes('-fullscreen', True)
        self.root.geometry('1200x699')
        file1 = self.setting_path + "\\settings.json"
        if os.path.exists(file1) and os.path.isfile(file1):
            with open(file1, 'r') as f:
                data = json.load(f)
                background_pic = self.setting_path + "\\desktop_backgrounds\\" + data['background']
                self.settings["background_pic"] = background_pic
        else:
            print("File " + str(file1) + " does not exist\n"+"in path "+str(file1))
            self.shutdown()
            return 0

    def set_background(self, background_pic):
        self.background_photo = tk.PhotoImage(file=background_pic)
        self.canvas_root.place(x=0, y=0)

        self.canvas_root.create_line(0, 0, 200, 200, fill='blue')
        self.canvas_root.create_rectangle(50, 50, 150, 150, fill='blue', outline='green', width=2)

        self.canvas_root.create_image(int(self.size[0])/2, int(self.size[1])/2, image=self.background_photo)

    def maintain(self):
        self.root.mainloop()

    def shutdown(self):
        self.root.quit()


if __name__ == '__main__':
    win = tk.Tk()
    a = Fake_Win(win)
    a.maintain()
