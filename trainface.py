import face_recognition
import os
import pickle

# Đường dẫn đến thư mục chứa các hình ảnh khuôn mặt mẫu
dataset_dir = "trainimage/"

# Tạo danh sách các hình ảnh khuôn mặt mẫu
image_files = [os.path.join(dataset_dir, f) for f in os.listdir(dataset_dir) if f.endswith(".jpg")]

# Tạo danh sách khuôn mặt đã train
known_faces = []

# Duyệt qua từng hình ảnh
for image_file in image_files:
    # Đọc hình ảnh
    image = face_recognition.load_image_file(image_file)

    # Phát hiện khuôn mặt trong hình ảnh
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)

    # Kiểm tra xem có tìm thấy ít nhất một khuôn mặt hay không
    if len(face_encodings) > 0:
        # Lấy mã hóa khuôn mặt đầu tiên
        face_encoding = face_encodings[0]

        # Lấy tên file ảnh (loại bỏ phần đuôi .jpg)
        name = "Bach"

        # Thêm khuôn mặt và tên vào danh sách đã train
        known_faces.append({
            "name": name,
            "encoding": face_encoding
        })

# Lưu danh sách khuôn mặt đã train vào file PKL
with open("bachface.pkl", "wb") as f:
    pickle.dump(known_faces, f)
