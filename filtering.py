import cv2
import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os

# ---------- Create folder if not exists ----------
save_path = r"D:\image_filter\Edited photos"
os.makedirs(save_path, exist_ok=True)

# ---------- Upload function ----------
def upload_image():
    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
    )
    return file_path


# ---------- BLUR ----------
def blur_image():
    path = upload_image()
    if not path:
        return

    img = cv2.imread(path)
    if img is None:
        print("Error loading image")
        return

    img = cv2.resize(img, (800, 700))
    blurred = cv2.blur(img, (20, 20))

    cv2.imshow("Blurred Image", blurred)

    cv2.imwrite(os.path.join(save_path, "Blurred_Image.jpg"), blurred)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# ---------- CROP ----------
def crop_image():
    path = upload_image()
    if not path:
        return

    img = cv2.imread(path)
    if img is None:
        print("Error loading image")
        return

    img = cv2.resize(img, (800, 700))

    h, w, _ = img.shape
    crop = img[0:h//2, 0:w//2]

    cv2.imshow("Cropped Image", crop)

    cv2.imwrite(os.path.join(save_path, "Cropped_Image.jpg"), crop)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# ---------- OVERLAY ----------
def overlay_image():
    print("Select first image")
    path1 = upload_image()
    if not path1:
        return

    print("Select second image")
    path2 = upload_image()
    if not path2:
        return

    img1 = Image.open(path1).resize((800, 500)).convert("RGBA")
    img2 = Image.open(path2).resize((800, 500)).convert("RGBA")

    blended = Image.blend(img1, img2, alpha=0.5)

    blended.show()

    blended.convert("RGB").save(os.path.join(save_path, "Blended_Image.jpg"))


# ---------- ROTATE ----------
def rotate_image():
    path = upload_image()
    if not path:
        return

    img = cv2.imread(path)
    if img is None:
        print("Error loading image")
        return

    rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    rotated = cv2.resize(rotated, (800, 600))

    cv2.imshow("Rotated Image", rotated)

    cv2.imwrite(os.path.join(save_path, "Rotated_Image.jpg"), rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# ---------- GRADIENT ----------
def gradient_image():
    path = upload_image()
    if not path:
        return

    img = cv2.imread(path)
    if img is None:
        print("Error loading image")
        return

    img = cv2.resize(img, (400, 400))

    h, w, _ = img.shape

    gradient = np.linspace(0, 1, h).reshape(h, 1)
    gradient = np.repeat(gradient, w, axis=1)
    gradient = cv2.cvtColor(gradient.astype(np.float32), cv2.COLOR_GRAY2BGR)

    result = img.astype(np.float32) * gradient
    result = np.uint8(result)

    cv2.imshow("Gradient Effect", result)

    cv2.imwrite(os.path.join(save_path, "Gradient_Image.jpg"), result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# ---------- GUI ----------
root = tk.Tk()
root.title("Image Editor")
root.geometry("300x300")

tk.Label(root, text="Image Editor", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="Blur", width=20, command=blur_image).pack(pady=5)
tk.Button(root, text="Crop", width=20, command=crop_image).pack(pady=5)
tk.Button(root, text="Overlay", width=20, command=overlay_image).pack(pady=5)
tk.Button(root, text="Rotate", width=20, command=rotate_image).pack(pady=5)
tk.Button(root, text="Gradient", width=20, command=gradient_image).pack(pady=5)

root.mainloop()