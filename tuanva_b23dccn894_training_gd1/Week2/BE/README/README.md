# BÁO CÁO THỰC HÀNH BACKEND – SPRING BOOT

# Tuần 2: RESTful API và Tích hợp ORM (JPA + MySQL)

## PHẦN 1. FRAMEWORK VÀ XÂY DỰNG RESTFUL API

### 1. Khái niệm Framework

Framework là bộ khung hoặc nền tảng được xây dựng sẵn giúp lập trình viên phát triển ứng dụng nhanh hơn, có cấu trúc rõ ràng và dễ bảo trì.  
Nó cung cấp sẵn thư viện, công cụ, quy tắc để tiêu chuẩn hóa cách viết mã nguồn và tăng hiệu quả phát triển.

**Một số framework phổ biến:**

- **Spring Boot (Java):** Dùng để xây dựng web và REST API.
- **Express.js (NodeJS):** Nhẹ, linh hoạt, dễ sử dụng với JavaScript.
- **Django (Python):** Mạnh mẽ, tích hợp ORM sẵn.

**Lợi ích của framework:**

- Tăng tốc độ phát triển.
- Giảm lỗi, dễ bảo trì.
- Có sẵn nhiều thư viện hỗ trợ.
- Tổ chức code khoa học, dễ mở rộng.

---

### 2. Giới thiệu Spring Boot

Spring Boot là framework Java hỗ trợ phát triển ứng dụng web và API nhanh chóng mà không cần cấu hình phức tạp.  
Nó dựa trên Spring Framework truyền thống, nhưng được đơn giản hóa giúp khởi chạy ứng dụng chỉ với vài dòng cấu hình.

Dự án Spring Boot thường được khởi tạo qua công cụ **Spring Initializr** tại địa chỉ:  
[https://start.spring.io](https://start.spring.io)

**Một số thành phần chính trong Spring Boot:**

- **Spring Web:** Xây dựng RESTful API.
- **Spring Boot DevTools:** Tự động tải lại khi code thay đổi.
- **Lombok:** Giúp giảm bớt code getter, setter.
- **Spring Data JPA:** Tích hợp ORM với cơ sở dữ liệu.

---

### 3. Khái niệm RESTful API

RESTful API là tiêu chuẩn thiết kế API cho phép client và server giao tiếp qua giao thức HTTP.  
Mỗi endpoint tương ứng với một hành động CRUD trong ứng dụng.

| Phương thức | Mô tả chức năng  | Ví dụ              |
| ----------- | ---------------- | ------------------ |
| **GET**     | Lấy dữ liệu      | /api/students      |
| **POST**    | Thêm mới dữ liệu | /api/students      |
| **PUT**     | Cập nhật dữ liệu | /api/students/{id} |
| **DELETE**  | Xóa dữ liệu      | /api/students/{id} |

---

### 4. Cấu trúc và hoạt động của RESTful API

Spring Boot tổ chức ứng dụng theo mô hình nhiều tầng:

- **Controller:** Tiếp nhận yêu cầu HTTP và trả về phản hồi cho client.
- **Service:** Xử lý nghiệp vụ, tính toán, điều phối dữ liệu.
- **Model:** Đại diện cho đối tượng dữ liệu trong hệ thống.

Luồng hoạt động của API:
Client (Postman / Frontend) → Controller → Service → Repository → Dữ liệu

---

### 5. Kiểm thử API bằng Postman

Postman là công cụ phổ biến để kiểm thử API.  
Người dùng có thể gửi các loại yêu cầu HTTP (GET, POST, PUT, DELETE) đến server và nhận phản hồi ở dạng JSON.  
Mỗi API được định nghĩa với đường dẫn (endpoint) rõ ràng và có thể kiểm tra kết quả trực tiếp.

---

### VIDEO DEMO

**Link video:**
👉 [Phần 1](https://drive.google.com/drive/u/0/folders/1OKaZiGLvATTRUC04BU2i0jQzJgpKZwCh)

---

## PHẦN 2. TÍCH HỢP DATABASE (ORM – JPA + MYSQL)

### 1. Khái niệm ORM

ORM (Object Relational Mapping) là kỹ thuật ánh xạ giữa đối tượng trong ngôn ngữ lập trình và bảng trong cơ sở dữ liệu.  
Thay vì thao tác trực tiếp với câu lệnh SQL, lập trình viên làm việc với các đối tượng Java (Entity).

**Lợi ích của ORM:**

- Giảm thao tác SQL thủ công.
- Dễ bảo trì và mở rộng ứng dụng.
- Dữ liệu được ánh xạ trực tiếp từ đối tượng sang bảng.
- Giúp code gọn gàng, dễ hiểu, tránh lỗi truy vấn.

---

### 2. JPA và Hibernate trong Spring Boot

- **JPA (Java Persistence API):**  
  Là chuẩn giao tiếp giữa Java và cơ sở dữ liệu, định nghĩa các quy tắc và annotation như `@Entity`, `@Id`, `@Table`, giúp ánh xạ đối tượng Java với bảng trong cơ sở dữ liệu.

- **Hibernate:**  
  Là framework triển khai JPA, đảm nhận việc thực thi ánh xạ, tạo truy vấn SQL, quản lý phiên làm việc (_session_), và tự động hóa các thao tác CRUD khi làm việc với cơ sở dữ liệu.

- **Spring Data JPA:**  
  Là thư viện của Spring Boot được xây dựng trên nền **JPA** và **Hibernate**, giúp đơn giản hóa thao tác với cơ sở dữ liệu.  
  Lập trình viên chỉ cần tạo các interface `extends JpaRepository`, là đã có sẵn các phương thức CRUD như `findAll`, `save`, `delete`, ... mà không cần viết SQL hoặc xử lý `EntityManager` thủ công.

Trong Spring Boot, khi thêm dependency `spring-boot-starter-data-jpa`, Hibernate sẽ tự động được cấu hình để kết nối đến cơ sở dữ liệu.

---

### 3. Cấu hình cơ sở dữ liệu trong `application.properties`

Tập tin `application.properties` dùng để khai báo thông tin kết nối đến MySQL.

Các thuộc tính cơ bản:

- `spring.datasource.url`: Đường dẫn tới database MySQL.
- `spring.datasource.username`: Tên người dùng của MySQL.
- `spring.datasource.password`: Mật khẩu.
- `spring.jpa.hibernate.ddl-auto`: Tùy chọn tự động tạo hoặc cập nhật bảng (`update`, `create`, `validate`, ...).
- `spring.jpa.show-sql`: Hiển thị câu SQL trong console khi chạy.

---

### 4. Nguyên lý hoạt động của ORM trong Spring Boot

- Mỗi **Entity** tương ứng với một bảng trong database.
- Mỗi thuộc tính (field) trong class tương ứng với một cột trong bảng.
- Khi gọi các phương thức như `save()`, `findAll()`, `deleteById()`… Hibernate sẽ tự động sinh ra SQL tương ứng để thao tác với cơ sở dữ liệu.

---

### 5. Ưu điểm khi sử dụng JPA & Hibernate

- Tiết kiệm thời gian khi thao tác với dữ liệu.
- Tự động ánh xạ bảng và đối tượng.
- Dễ dàng mở rộng và thay đổi cấu trúc dữ liệu.
- Tích hợp tốt với Spring Boot, chỉ cần cấu hình một lần.

---

### VIDEO DEMO

**Link video:**
👉 [Phần 2](https://drive.google.com/drive/u/0/folders/1OKaZiGLvATTRUC04BU2i0jQzJgpKZwCh)
