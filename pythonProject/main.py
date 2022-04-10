from tkinter import *
from random import *
from PIL import Image
import subprocess

tk=Tk()

canvas = Canvas(tk, width=128, height=128)
for i in range(0,100):
    canvas.pack()
    rand_int=randint(20, 50)
    rand_int1=randint(60,90)
    image = canvas.create_rectangle(rand_int,rand_int,rand_int1,rand_int1,fill='red')

    canvas.postscript(file=rf'C:\Users\kombu\PycharmProjects\ps\bcsdqw{i}.ps')

    path=rf'C:\Users\kombu\PycharmProjects\pythonProject\ImageMagick-7.1.0-portable-Q16-x64\magick.exe C:\Users\kombu\PycharmProjects\ps\bcsdqw{i}.ps C:\Users\kombu\PycharmProjects\jpg\bcsdqw{i}.jpg'

    p = subprocess.Popen(path,stdout=subprocess.PIPE,shell=True)
    result = p.communicate()[0]
    tk.update()
    canvas.delete('all')
