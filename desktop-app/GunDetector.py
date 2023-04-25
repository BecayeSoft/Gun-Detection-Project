import cv2
from ultralytics import YOLO
import numpy as np


class GunDetector:

    def __init__(self):
        self.model = None
        self.COLORS = {'red': (0, 0, 255), 'green': (0, 255, 0), 'blue': (255, 0, 0)}

    def load(self, path):
        """
        Load a model's weights.
        This is useful to load for example the last trained model directly
        instead of retraining it again.
        E.g.: path='runs/detect/train18/weights/best.pt'

        :param path:
        :return:
        """
        self.model = YOLO(path)

    def predict_image(self, image):
        """
        Show the image with the predicted boxes.

        :param image: the image used to make inference.
        :return: pred_image: an image with predicted bounding boxes.
        """

        pred_results = self.model.predict(source=image)
        pred_image = pred_results[0].plot()

        return pred_image


    def predict_video(self, video_path, title='Predicted Video', output_filename='predicted_video.mp4'):
        """
        Make inference on a video, display and save it.

        :param title: the title of the frame used to show the video.
        :param video_path: a video
        """

        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

        # Create a video writer object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        writer = cv2.VideoWriter(output_filename, fourcc, fps, frame_size)

        print('DEBUG')

        # Loop through the video frames
        while cap.isOpened():
            # Read a frame from the video
            success, frame = cap.read()

            if success:
                # Run YOLOv8 inference on the frame

                results = self.model.predict(source=frame)

                # get the predicted image with annotations
                annotated_frame = results[0].plot()

                # Write the annotated frame to the video writer object
                writer.write(annotated_frame)

                # Display the annotated frame
                # cv2.imshow(title, annotated_frame)

                # Break the loop if 'q' is pressed
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            else:
                # Break the loop if the end of the video is reached
                break

        # Release the video capture object and close the display window
        cap.release()
        writer.release()
        cv2.destroyAllWindows()
