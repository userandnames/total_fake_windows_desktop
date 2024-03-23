import tkinter as tk
import os
import json
from PIL import Image, ImageTk
from pynput import mouse, keyboard


class Fake_Win:
    def __init__(self, main_window):
        listener1 = mouse.Listener(
            on_click=self.simulate_left_pressed)
        listener2 = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        listener1.start()


        self.root_path = ''
        self.setting_path = ''
        self.settings = dict()
        self.background_photo = None

        self.pressed_position = []
        self.selected_rectangle = None
        self.press_or_release = False
        self.pressed_key = []

        self.init_settings()  # 初始化路径设置

        self.root = main_window
        self.size = [self.root.winfo_screenwidth(), self.root.winfo_screenheight()]
        self.canvas_root = tk.Canvas(self.root, width=int(self.size[0]), height=int(self.size[1]), bg="black")
        self.canvas_root.place(x=0, y=0)
        self.right_click_bar = None
        if self.set():
            self.set_canvas_and_background_init()
            self.draw()

    def init_settings(self):
        self.root_path = os.getcwd()
        self.setting_path = self.root_path + "\\settings"
        subdir = os.listdir(self.setting_path)
        for i in subdir:
            if os.path.isdir(self.setting_path + "\\" + i):
                self.settings[i] = os.listdir(self.setting_path + "\\" + i)

    def set(self):
        self.root.attributes('-fullscreen', True)
        self.root.overrideredirect(True)
        file1 = self.setting_path + "\\settings.json"
        if os.path.exists(file1) and os.path.isfile(file1):
            with open(file1, 'r') as f:
                data = json.load(f)
                background_pic = self.setting_path + "\\desktop_backgrounds\\gif\\" + data['background']
                self.settings["background_pic"] = background_pic
                print(self.settings["background_pic"])
                return 1
        else:
            print("File " + str(file1) + " does not exist\n"+"in path "+str(file1))
            self.shutdown()
            return 0

    def set_canvas_and_background_init(self):
        print("222"+self.settings["background_pic"])
        self.background_photo = Image.open(self.settings["background_pic"])
        self.background_photo = self.background_photo.resize((self.size[0], self.size[1]))
        self.background_photo = ImageTk.PhotoImage(self.background_photo)
        # self.background_photo = tk.PhotoImage(file=self.settings["background_pic"])
        self.canvas_root.place(x=0, y=0)
        self.canvas_root.config(highlightthickness=0)
        self.canvas_root.create_image(int(self.size[0])/2, int(self.size[1])/2, image=self.background_photo)
        self.canvas_root.bind("<Button-3>", self.simulate_right_click)
        self.canvas_root.bind("<Button-1>", self.simulate_left_click)
        # self.canvas_root.bind("<ButtonPress-1>", self.simulate_left_pressed)

    def simulate_right_click(self, event):
        x = event.widget.winfo_pointerx()
        y = event.widget.winfo_pointery()
        if self.right_click_bar is not None:
            self.right_click_bar.destroy()
        self.right_click_bar = tk.Toplevel(self.canvas_root)
        self.right_click_bar.geometry(f"{200}x{400}+{x}+{y}")
        menu_bar = tk.Menu(self.right_click_bar)

    def simulate_left_click(self, event):
        if self.right_click_bar is not None:
            self.right_click_bar.destroy()

    def simulate_left_pressed(self, x, y, button, pressed):
        if button == mouse.Button.left and pressed:
            self.press_or_release = True
        if button == mouse.Button.left and not pressed:
            self.press_or_release = False

    def on_press(self, key):
        self.pressed_key.append(key)

    def on_release(self, key):
        self.pressed_key.remove(key)

    def draw(self):
        if self.press_or_release:
            if self.selected_rectangle is not None:
                self.canvas_root.delete(self.selected_rectangle)
                # self.pressed_position = []

            x, y = self.canvao,olls_root.winfo_pointerxy()
            if len(self.pressed_position) == 0:
                self.pressed_position.append([x, y])
                self.pressed_position.append([x, y])
            if len(self.pressed_position) >= 2:
                self.pressed_position[-1] = [x, y]
                self.selected_rectangle = self.canvas_root.create_rectangle(
                                                              self.pressed_position[0][0], self.pressed_position[0][1],
                                                              self.pressed_position[-1][0], self.pressed_position[-1][1],
                                                              fill="blue", outline="blue", stipple="gray25")
        else:
            if self.selected_rectangle is not None:
                self.canvas_root.delete(self.selected_rectangle)
                self.pressed_position = []
        self.root.after(100, self.draw)

    def watchdog(self):  #
        pass
    def maintain(self):
        self.root.mainloop()

    def shutdown(self):
        self.root.quit()


if __name__ == '__main__':
    win = tk.Tk()
    a = Fake_Win(win)
    a.maintain()
