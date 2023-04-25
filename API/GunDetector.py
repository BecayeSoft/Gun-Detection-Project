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

    def predict_image(self, image, color=None):
        """
        Show the image with the predicted boxes.

        :param color: the color used to draw the predictions
        :param image: the image used to make inference.
        :return: pred_image: an image with predicted bounding boxes.
        """

        if color in self.COLORS.keys():
            color = self.COLORS.get(color)
        else:
            color = self.COLORS.get('red')

        pred_results = self.model.predict(source=image)
        # pred_image = pred_results[0].plot()

        # print('\n\n-------------pred_results---------------\n\n', pred_results[0].boxes)
        # pred_image = self.draw_predicted_boxes(pred_results, color=color)
        pred_image = pred_results[0].plot()

        return pred_image

    def predict_video(self, video_path, title='Predicted Video', color=None):
        """
        TODO: Save the video just like you do with the images

        Make inference on a video and draw predicted bounding boxes.

        :param color:
        :param title: the title of the frame used to show the video.
        :param video_path: a video
        """

        if color in self.COLORS.keys():
            color = self.COLORS.get(color)
        else:
            color = self.COLORS.get('red')

        cap = cv2.VideoCapture(video_path)

        # Loop through the video frames
        while cap.isOpened():
            # Read a frame from the video
            success, frame = cap.read()

            if success:
                # Run YOLOv8 inference on the frame

                results = self.model.predict(source=frame)

                # get the predicted image with annotations
                # annotated_frame = results[0].plot()
                annotated_frame = self.draw_predicted_boxes(results, color=color)

                # Display the annotated frame
                cv2.imshow(title, annotated_frame)

                # Break the loop if 'q' is pressed
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            else:
                # Break the loop if the end of the video is reached
                break

        # Release the video capture object and close the display window
        cap.release()
        cv2.destroyAllWindows()

    def draw_predicted_boxes(self, pred_results, color=None):
        """
        TODO check if predicted boxes are not null
        Draw the predicted bounding boxes on the image.
        Note that predicted boxes can be retrieved with `pred_results[i].plot()`.

        :param color:
        :param pred_results: the results of the prediction. They are returned by `modelpredict()`
        :return: predicted_image: the image with predicted boxes.
        """
        if color in self.COLORS.keys():
            color = self.COLORS.get(color)
        else:
            color = self.COLORS.get('red')

        predicted_image = None

        # draw the predicted bounding boxes in the image
        for pred in pred_results:
            # bbox = pred.boxes.xywh.tolist()
            # if not bbox:
            #     print('bbox\n------------------------------------------- empty', )
            #     return pred.orig_img

            # get bounding box coordinates
            bbox = pred.boxes.xywh.tolist()[0]
            bbox = np.array(bbox, dtype=int)

            original_image = pred.orig_img

            # x and y are the center of the box, so we put the at them top left
            w = bbox[2]
            h = bbox[3]
            x = int(bbox[0] - w / 2)
            y = int(bbox[1] - h / 2)

            # draw the bounding box
            predicted_image = cv2.rectangle(original_image, (x, y), (x + w, y + h), color, 2)

            # draw class name and confidence
            class_name = pred.names.get(0)
            confidence = np.array(pred.boxes.conf)[0]
            confidence = np.round(confidence * 100, 2)
            text = class_name + ': ' + str(confidence)

            # draw text above box:
            # if the box reaches the top of the image, we draw the text below the box adn add padding to the left
            x_test = x
            y_text = y - 10

            if y < 15:
                x_test = x + 2
                y_text = y + 15

            cv2.putText(img=predicted_image, text=text, org=(x_test, y_text), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.5, color=color, thickness=1, lineType=cv2.LINE_AA)

        return predicted_image
