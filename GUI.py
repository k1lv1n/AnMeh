from tkinter import *
import json


class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("GUI")
        self.window.geometry('650x350')
        lbl = Label(self.window, text="Тангаж", font=("Times New Roman", 30))
        lbl1 = Label(self.window, text="Рысканье", font=("Times New Roman", 30))
        lbl2 = Label(self.window, text="Крен", font=("Times New Roman", 30))
        lbl3 = Label(self.window, text="угол в градусах [0;360]", font=("Times New Roman", 30))
        lbl.grid(column=0, row=1)
        lbl1.grid(column=0, row=2)
        lbl2.grid(column=0, row=3)
        lbl3.grid(column=1, row=0)
        self.scale_x = Scale(self.window, orient=HORIZONTAL, length=400, from_=0, to=360, tickinterval=45,
                             resolution=0.1)
        self.scale_y = Scale(self.window, orient=HORIZONTAL, length=400, from_=0, to=360, tickinterval=45,
                             resolution=0.1)
        self.scale_z = Scale(self.window, orient=HORIZONTAL, length=400, from_=0, to=360, tickinterval=45,
                             resolution=0.1)
        self.scale_x.grid(column=1, row=1)
        self.scale_y.grid(column=1, row=2)
        self.scale_z.grid(column=1, row=3)
        self.button = Button(self.window, text='ok', width=5, height=1, bg='white', fg='black', font='arial 30',
                             command=self.click_handler)
        self.button.grid(column=1, row=4)

    def begin(self):
        self.window.mainloop()

    def click_handler(self):
        with open("Data.json", "r") as file:
            arr1 = json.load(file)
        arr = [float("{0:.1}".format(self.scale_x.get())), self.scale_y.get(),
               float("{0:.1}".format(self.scale_z.get()))]
        for i in range(3):
            arr[i] += arr1[i]
            arr[i] = arr[i] % 360
        with open("Data.json", "w") as write_file:
            json.dump(arr, write_file)
        self.window.destroy()
        print(arr)
