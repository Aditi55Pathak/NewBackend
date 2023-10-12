from flask import render_template
from flask_login import current_user, login_required
import app

# Serve the capture.html page
@app.route("/dashboard/capture_image_page")
@login_required
def capture_image_page():
    return render_template("capture.html")


# capturing image routing
@app.route("/dashboard/capture_image", methods=["POST"])
@login_required
def capture_image():
    if current_user.role in ("developer", "teacher"):
        # put your code of capturing image here
        # Example code to capture an image using OpenCV
        import cv2

        # Open the webcam
        cap = cv2.VideoCapture(0)

        # Read and display the captured image
        ret, frame = cap.read()
        cv2.imshow('Captured Image', frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Perform any required image processing or saving logic here

        return "Image captured successfully!"  # Return a success message
    else:
        return "You are not authorized to capture an image."
