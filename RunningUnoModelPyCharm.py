import cv2
import PySimpleGUI as sg
from ultralytics import YOLO


# Define the YOLO model path
model_path = "/Users/mukhtarrabayev/Downloads/content/runs/detect/train8/weights/best.pt"

# Load the YOLO model
model = YOLO(model_path, task='detect')

# Define the layout of the GUI
layout = [
    [sg.Text("UNO Card Detection", font=("Helvetica", 20))],
    [sg.Image(key="-IMAGE-")],
    [sg.Button("Browse"), sg.Button("Exit")],

]

# Create the window
window = sg.Window("UNO Card Detection", layout, resizable=True, finalize=True)

def browse_image():
    file_path = sg.popup_get_file("Select Image", file_types=(("Image Files", "*.png;*.jpg"),))
    if file_path:
        return file_path




def detect_and_display_cards(image_path):
    image = cv2.imread(image_path)
    results = model(image, show=True)

# Event loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        break

    elif event == "Browse":
        image_path = browse_image()

        # Perform detection and display immediately after selecting an image
        if image_path:
            detect_and_display_cards(image_path)

# Close the window
window.close()
