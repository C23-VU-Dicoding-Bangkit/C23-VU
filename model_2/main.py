import cv2
from mtcnn.mtcnn import MTCNN

def predict_condition():
    detector = MTCNN()
    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()

        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            faces = detector.detect_faces(frame_rgb)
            num_faces = len(faces)

            if num_faces > 0:
                for idx, result in enumerate(faces):
                    x, y, width, height = result['box']
                    color = (255, 0, 0)
                    thickness = 2
                    start = (x, y)
                    stop = (x + width, y + height)
                    frame = cv2.rectangle(frame, start, stop, color, thickness)

                    cv2.putText(frame, f"Face {idx + 1}", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, thickness=2)

                    for key, value in result['keypoints'].items():
                        radius = 5
                        cv2.circle(frame, (int(value[0]), int(value[1])), radius, color, -1)

            else:
                cv2.putText(frame, "Gak ada mukanya bang", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            cv2.imshow('Real-time Face Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    predict_condition()
