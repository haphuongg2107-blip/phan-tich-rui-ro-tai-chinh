# 📊 HỆ THỐNG PHÂN TÍCH RỦI RO TÀI CHÍNH BẰNG AI

Ứng dụng web sử dụng Machine Learning để phân tích dữ liệu tài chính doanh nghiệp, đánh giá mức độ rủi ro và xác định độ đáng tin cậy dựa trên các chỉ số tài chính thực tế.

Dự án được xây dựng bằng Python Flask kết hợp với mô hình AI Random Forest nhằm hỗ trợ:
- phân tích dữ liệu tài chính,
- phát hiện doanh nghiệp có nguy cơ rủi ro,
- hỗ trợ đánh giá độ ổn định tài chính,
- trực quan hóa dữ liệu thông qua dashboard web.

---

# 🎯 Mục Tiêu Dự Án

Trong lĩnh vực tài chính, việc đánh giá doanh nghiệp có mức độ rủi ro cao hay thấp là vô cùng quan trọng đối với:
- ngân hàng,
- công ty tài chính,
- nhà đầu tư,
- tổ chức tín dụng.

Dự án này được xây dựng nhằm mô phỏng một hệ thống AI hỗ trợ:
- đánh giá mức độ rủi ro tài chính,
- phân tích độ đáng tin cậy doanh nghiệp,
- hỗ trợ ra quyết định đầu tư hoặc tín dụng,
- xử lý dữ liệu CSV tự động,
- trực quan hóa kết quả phân tích.

---

# 🚀 Chức Năng Chính

## 📂 Upload Dataset CSV

Người dùng có thể tải file CSV trực tiếp lên website để hệ thống tự động:
- đọc dữ liệu,
- kiểm tra dữ liệu,
- xử lý dữ liệu thiếu,
- tiến hành phân tích AI.

---

## 🧠 Phân Tích AI

Hệ thống sử dụng Machine Learning để:
- dự đoán mức độ rủi ro tài chính,
- phân loại doanh nghiệp,
- đánh giá tình trạng tài chính,
- đưa ra điểm tin cậy.

---

## 📈 Dashboard Thống Kê

Website hiển thị:
- tổng số dữ liệu,
- số doanh nghiệp rủi ro cao,
- số doanh nghiệp ổn định,
- bảng kết quả phân tích trực quan.

---

## ⚠️ Đánh Giá Rủi Ro

AI sẽ phân loại doanh nghiệp thành:
- Rủi Ro Cao
- Ổn Định

đồng thời đưa ra:
- Điểm Tin Cậy
- Tình Trạng Tài Chính

---

# 🧠 Công Nghệ Sử Dụng

| Công Nghệ | Chức Năng |
|---|---|
| Python | Ngôn ngữ lập trình chính |
| Flask | Xây dựng web backend |
| Pandas | Đọc và xử lý dữ liệu |
| NumPy | Tính toán dữ liệu |
| Scikit-learn | Machine Learning |
| HTML/CSS | Giao diện website |
| Joblib | Lưu AI model |
| Random Forest | Thuật toán AI |

---

# 🏗️ Kiến Trúc Hệ Thống

Hệ thống gồm 3 phần chính:

## 1️⃣ Data Processing
- đọc dữ liệu CSV,
- xử lý dữ liệu thiếu,
- chuẩn hóa dữ liệu,
- phân tích dữ liệu tài chính.

---

## 2️⃣ Machine Learning
- train mô hình Random Forest,
- dự đoán rủi ro tài chính,
- đánh giá mức độ tin cậy.

---

## 3️⃣ Web Application
- upload file,
- hiển thị dashboard,
- hiển thị kết quả phân tích,
- giao diện người dùng.

---

# 📂 Cấu Trúc Project

```bash
phân tích/
│
├── app.py
├── train_model.py
├── dataset.csv
├── risk_model.pkl
├── scaler.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── uploads/
```

---

# ⚙️ Cài Đặt Dự Án

## 1️⃣ Clone Repository

```bash
git clone https://github.com/haphuongg2107-blip/phan-tich-rui-ro-tai-chinh.git
```

---

## 2️⃣ Tạo Môi Trường Anaconda

```bash
conda create -n phantich_ai python=3.11
```

---

## 3️⃣ Activate Environment

```bash
conda activate phantich_ai
```

---

## 4️⃣ Cài Thư Viện

```bash
pip install flask pandas numpy scikit-learn matplotlib seaborn joblib
```

---

# ▶️ Chạy Dự Án

## 🧠 Train AI Model

```bash
python train_model.py
```

Sau khi train thành công sẽ tạo:
- `risk_model.pkl`
- `scaler.pkl`

---

## 🌐 Chạy Website Flask

```bash
python app.py
```

---

# 🌍 Truy Cập Website

Mở trình duyệt:

```bash
http://127.0.0.1:5000
```

---

# 📊 Quy Trình Hoạt Động

1. Người dùng upload file CSV  
2. Flask nhận dữ liệu  
3. Pandas đọc dữ liệu  
4. Hệ thống xử lý missing values  
5. AI model phân tích dữ liệu  
6. Random Forest dự đoán rủi ro  
7. Website hiển thị dashboard kết quả  

---

# 📈 Machine Learning Model

Dự án sử dụng:

## 🌲 Random Forest Classifier

Ưu điểm:
- xử lý dữ liệu tốt,
- độ chính xác cao,
- giảm overfitting,
- phù hợp dữ liệu tài chính.

---

# 🧪 Xử Lý Dữ Liệu

Hệ thống có:
- kiểm tra dữ liệu thiếu,
- chuẩn hóa dữ liệu,
- scaling dữ liệu,
- phân chia train/test,
- đánh giá model.

---

# 💻 Giao Diện Website

Website được thiết kế theo phong cách:
- Dark Dashboard UI,
- Fintech Dashboard,
- Modern Analytics Interface.

Gồm:
- upload file,
- thống kê dữ liệu,
- bảng phân tích AI,
- dashboard trực quan.

---

# 🔮 Hướng Phát Triển

Trong tương lai có thể nâng cấp:
- biểu đồ trực quan,
- AI Deep Learning,
- kết nối database,
- đăng nhập người dùng,
- deploy cloud,
- realtime analytics,
- PDF report export.

---

# 👨‍💻 Tác Giả

## Phương

Dự án học tập và nghiên cứu về:
- Machine Learning,
- Financial Analytics,
- Data Science,
- AI Web Application.

---

# ⭐ Repository

Nếu thấy dự án hữu ích hãy:
- ⭐ Star repository
- 🍴 Fork project
- 📢 Share project
- 💡 Đóng góp phát triển

---

# 📜 License

Dự án phục vụ mục đích:
- học tập,
- nghiên cứu,
- thực hành Machine Learning và Flask.
- 
