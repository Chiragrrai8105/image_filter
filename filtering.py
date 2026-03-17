from tkinter import Tk, filedialog
import cv2
import numpy as np
from PIL import Image
def upload_image():
    root = Tk()
    root.withdraw()  # Hide main window
    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
    )
    root.destroy()
    return file_path
print("1.Blur  2.crop  3.Overlay  4.Rotate  5.Gradient")
n = int(input("Enter the choice: "))

if n == 1:
    file_path = upload_image()
    if not file_path:
        print("No file selected")
        exit()
    img = cv2.imread(file_path)
    img1 = cv2.resize(img, (800, 700))
    img = cv2.blur(img1, (20, 20))
    cv2.imshow('image', img1)
    cv2.imshow("blurrrdimage", img)
    cv2.imwrite("D:\\image_filter\\Edited photos\\Blurred Image.jpg", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

elif n == 2:
    file_path = upload_image()
    if not file_path:
        print("No file selected")
        exit()
    img = cv2.imread(file_path)
    img1 = cv2.resize(img, (800, 700))
    x = 0
    y = 0
    h = 900
    w = 900
    cropimg = img[y:y+h, x:x+w]
    cv2.imshow("Cropped Images", cropimg)
    cv2.imshow("Original Image", img1)
    cv2.imwrite("D:\\image_filter\\Edited photos\\Cropped Image.jpg", cropimg)
    cv2.waitKey(0)

elif n == 3:
    def changeImageSize(width, height, image):
        return image.resize((width, height))
    image1_path = upload_image()
    if not image1_path:
        print("No file selected")
        exit()
    image2_path = upload_image()
    if not image2_path:
        print("No file selected")
        exit()
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)
    image3 = changeImageSize(800, 500, image1)
    image4 = changeImageSize(800, 500, image2)

    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")

    alphaBlended1 = Image.blend(image5, image6, alpha=0.2)
    image1.show()
    image2.show()
    alphaBlended1.show()
    alphaBlended1_rgb = alphaBlended1.convert("RGB")
    alphaBlended1_rgb.save("D:\\image_filter\\Edited photos\\blended_Image.jpg")
    
elif n==4:
    file_path = upload_image()
    if not file_path:
        print("No file selected")
        exit()
    input_image = cv2.imread(file_path)
    resized_image = cv2.resize(input_image, (800, 600))
    
    rotated_image = cv2.rotate(input_image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    rotated_resized_image = cv2.resize(rotated_image, (800, 600))
    
    cv2.imshow('Original Image', resized_image)
    cv2.imshow('Rotated Image', rotated_resized_image)
    cv2.imwrite("D:\\image_filter\\Edited photos\\Cropped Image.jpg", rotated_resized_image)
    
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()
    
elif n==5:
    file_path = upload_image()
    if not file_path:
        print("No file selected")
        exit()
    input_image = cv2.imread(file_path)
    
    resized_image = cv2.resize(input_image, (400, 400))
    
    height, width, _ = resized_image.shape
    
    gradient = np.zeros((height, width), dtype=np.float32)
    
    for i in range(height):
        gradient[i, :] = (i / height)
    gradient = cv2.normalize(gradient, None, 0, 1, cv2.NORM_MINMAX)
    
    gradient = cv2.cvtColor(gradient.astype(np.float32), cv2.COLOR_GRAY2BGR)
    
    shadowed_image = np.multiply(resized_image.astype(np.float32), gradient)
    
    shadowed_image1 = np.uint8(np.clip(shadowed_image, 0, 255))
    
    cv2.imshow('Shadow Effect Image', shadowed_image1)
    cv2.imshow("image", resized_image)
    cv2.imwrite("D:\\image_filter\\Edited photos\\Gradient.jpg", shadowed_image1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
else:
    print("wrong option")


