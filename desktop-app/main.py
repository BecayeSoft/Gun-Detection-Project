import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import cv2

from GunDetector import GunDetector

root = tk.Tk()

root.title('Artificial Vision')

root.geometry("800x600")

model = GunDetector()
model.load('model/model.pt')


def select_image():
    filetypes = (('All files', '*.*'), ('PNG', '*.png'), ('JPEG', '*.jpeg'), ('JPG', '*.jpg'))

    filename = fd.askopenfilename(title='Open an image', initialdir='/', filetypes=filetypes)

    # Check if a file was selected
    if filename:

        # Read image and convert to array
        img = Image.open(filename)
        img_arr = np.array(img)

        #  Predict and resize to the size of the window
        pred_img = model.predict_image(img_arr)
        resized_img = cv2.resize(pred_img, (800, 600))

        # Create a PhotoImage object from the image
        img = Image.fromarray(resized_img)
        photo_img = ImageTk.PhotoImage(img)

        # Create a Label widget to display the image
        label_img = tk.Label(root, image=photo_img)
        label_img.image = photo_img  # Keep a reference to the image to prevent garbage collection

        # Pack the Label widget into the window
        label_img.pack()


def select_video():
    filetypes = (('MP4', '*.mp4'), ('All files', '*.*'))

    video_path = fd.askopenfilename(title='Open a video', initialdir='/', filetypes=filetypes)

    # Check if a file was selected
    if video_path:
        cap = cv2.VideoCapture(video_path)
        ret, frame = cap.read()

        resized_frame = cv2.resize(frame, (800, 600))
        rgb_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)

        # Create a PhotoImage object from the image
        img = Image.fromarray(rgb_frame)
        photo_img = ImageTk.PhotoImage(img)

        # Create a Label widget to display the image
        label_img = tk.Label(root, image=photo_img)
        label_img.image = photo_img  # Keep a reference to the image to prevent garbage collection
        label_img.pack()


        def update_video():
            # Read a frame from the video
            success, frame = cap.read()
            if success:
                # Predict the image and resize it to the size of the window
                pred_frame = model.predict_image(frame)
                resized_frame = cv2.resize(pred_frame, (800, 600))
                rgb_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)


                # Update the PhotoImage object with the new image
                img = Image.fromarray(rgb_frame)
                photo_img.paste(img)
                label_img.configure(image=photo_img)

                # Call this function again after 30 milliseconds
                root.after(30, update_video)
            else:
                # Release the video capture object and close the display window
                cap.release()

        # Call the update_video function after 30 milliseconds
        root.after(30, update_video)




open_image_button = ttk.Button(root, text='Open an Image', command=select_image)
open_image_button.pack(expand=True)

open_video_button = ttk.Button(root, text='Open a video', command=select_video)
open_video_button.pack(expand=True)

root.mainloop()
