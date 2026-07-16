# 1. Phân tích dữ liệu đầu vào và đầu ra
# Dữ liệu từ Request Body (POST /enrollments):
# student_id (Integer): Mã số sinh viên đăng ký.
# course_id (Integer): Mã số khóa học muốn đăng ký.
# Dữ liệu cần truy vấn từ Cơ sở dữ liệu (Database):
# Thông tin Sinh viên (Student): Lấy theo student_id để kiểm tra sự tồn tại và trạng thái (status).
# Thông tin Khóa học (Course): Lấy theo course_id để kiểm tra sự tồn tại, 
# trạng thái (status), và số lượng tối đa (max_students).
# Danh sách đăng ký hiện tại (Enrollment):
# Kiểm tra xem bản ghi có trùng student_id và course_id hay chưa.
# Đếm tổng số sinh viên đã đăng ký khóa học đó để so sánh với max_students.

# Dưới đây là sơ đồ được rút gọn thành dạng gạch đầu dòng tuần tự, dễ đọc và dễ copy-paste:
# BƯỚC 1: Kiểm tra tồn tại (Thất bại ➔ 404 Not Found)
# Không tìm thấy Sinh viên ➔ "Student not found"Không tìm thấy Khóa học ➔ "Course not found"
# BƯỚC 2: Kiểm tra trạng thái (Thất bại ➔ 400 Bad Request)
# Sinh viên là INACTIVE ➔ "Student is inactive"Khóa học là CLOSED ➔ "Course is closed"
# BƯỚC 3: Kiểm tra trùng lặp (Thất bại ➔ 400 Bad Request)
# Đã trùng student_id và course_id ➔ "Student is already enrolled in this course"
# BƯỚC 4: Kiểm tra giới hạn (Thất bại ➔ 400 Bad Request)
# Số lượng đăng ký hiện tại max_students ➔ "Course has reached maximum capacity"