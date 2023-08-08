import ultralytics
from IPython import display

display.clear_output()
ultralytics.checks()

from ultralytics import YOLO
import cv2


# Load a model
model = YOLO("./best.pt")  # load a pretrained model

save_path = "./Results/"
test_path = "./Test/13651880464_2847bb6e5c_o.jpg"
video_path = "./Test/pexels-edie-reed-6291972-1280x720-25fps.mp4"

#IMAGE/VIDEO DETECTION
model.predict(source=video_path,project=save_path, save=True, show=True)


# # REAL TIME DETECTION
# cap = cv2.VideoCapture(0)
#
# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     # Perform object detection on the frame
#     model.predict(source=frame, show=True)
#
#     # Check for the 'q' key press to quit
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # Release the video capture and close any OpenCV windows
# cap.release()
# cv2.destroyAllWindows()




