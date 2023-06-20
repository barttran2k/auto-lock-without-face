import cv2
import face_recognition,numpy
import os,time
import pickle
import ctypes
# Load danh sách khuôn mặt đã train từ file PKL
with open("bachface.pkl", "rb") as f:
    known_faces = pickle.load(f)

# Khởi tạo camera
video_capture = cv2.VideoCapture(0)

while True:
    # Đọc frame từ camera
    ret, frame = video_capture.read()

    # Chuyển đổi frame từ BGR sang RGB để sử dụng với thư viện face_recognition
    rgb_frame = numpy.ascontiguousarray(frame[:, :, ::-1])

    # Phát hiện khuôn mặt trong frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    # Kiểm tra nếu không có khuôn mặt trong khung hình
    if len(face_locations) == 0:
        time.sleep(5)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        if len(face_locations) == 0:
            ctypes.windll.user32.LockWorkStation()
        else:
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    # Duyệt qua các khuôn mặt đã phát hiện
    for face_encoding in face_encodings:
        # So sánh encoding của khuôn mặt đã phát hiện với danh sách encoding đã train
        match = face_recognition.compare_faces([kf["encoding"] for kf in known_faces], face_encoding)
        name = "Unknown"  # Mặc định là "Unknown" nếu không có khuôn mặt khớp

        if any(match):
            name = known_faces[match.index(True)]["name"]
        # Vẽ hộp giữa khuôn mặt và hiển thị tên
        top, right, bottom, left = face_locations[0]
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # Hiển thị frame
    cv2.imshow('Video', frame)

    # Thoát vòng lặp nếu nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
video_capture.release()
cv2.destroyAllWindows()
