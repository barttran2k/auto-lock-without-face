import cv2
import dlib,ctypes

# Load bộ nhận diện khuôn mặt dlib's face recognition
detector = dlib.get_frontal_face_detector()

# Load bộ nhận diện facial landmarks (nếu cần thiết)
# predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# Load model nhận diện khuôn mặt (ví dụ: dlib's model hoặc OpenCV's Haar cascades)

# Hàm nhận diện khuôn mặt từ ảnh
def detect_face(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    return faces


# Hàm khoá máy tính
def lock_computer():
    ctypes.windll.user32.LockWorkStation()
    
# lock_computer()