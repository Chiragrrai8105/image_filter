from tkinter import *
from tkinter import filedialog
import cv2
from PIL import Image

root = Tk()

def upload():
    file = filedialog.askopenfilename()
    print("Selected file:", file)
    cv2.imshow(file)


button = Button(root, text="Upload Image", command=upload)
button.pack()

root.mainloop()