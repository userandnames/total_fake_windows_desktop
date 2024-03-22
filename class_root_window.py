import tkinter as tk
import os
import json
from PIL import Image, ImageTk


class Fake_Win:
    def __init__(self):
        self.root_path = ''
        self.setting_path = ''
        self.settings = dict()
        self.root = tk.Tk()
        self.init_settings()
        self.set()
        self.root.mainloop()

    def init_settings(self):
        self.root_path = os.getcwd()
        self.setting_path = self.root_path + "\\settings"
        subdir = os.listdir(self.setting_path)
        for i in subdir:
            if os.path.isdir(self.setting_path + "\\" + i):
                self.settings[i] = os.listdir(self.setting_path + "\\" + i)

    def set(self):
        self.root.attributes('-fullscreen', True)
        print(self.setting_path)
        file1 = self.setting_path + "\\settings.json"
        if os.path.exists(file1) and os.path.isfile(file1):
            with open(file1, 'r') as f:
                data = json.load(f)
                background_pic = self.setting_path + "\\desktop_backgrounds\\" + data['background']
                self.set_background(background_pic)
                print("background set" + background_pic)
        else:
            print("File" + str(file1) + " does not exist")
            self.shutdown()

    def set_background(self, background_pic):
        img = ImageTk.PhotoImage(file=background_pic)
        size = [self.root.winfo_width(), self.root.winfo_height()]
        canvas_root = tk.Canvas(self.root, width=size[0], height=size[1], bd=0)
        canvas_root.create_image(500, 300, image=img)
        canvas_root.pack()

    def shutdown(self):
        self.root.quit()


if __name__ == '__main__':
    Fake_Win()
