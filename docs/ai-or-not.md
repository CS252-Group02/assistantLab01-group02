# AI Service: 10 Questions That Need AI vs. 10 That Do Not

Tài liệu này xác định ranh giới kỹ thuật giữa các yêu cầu có thể giải quyết bằng **quy tắc xác định / tra cứu dữ liệu (Rule-based / Deterministic Lookup)** và các yêu cầu đòi hỏi năng lực của **Mô hình Ngôn ngữ Lớn (LLM / Generative AI)** trong dự án *Smart Virtual Assistant*.

---

## 1. Tiêu chí phân loại (Classification Criteria)

| Tiêu chí | Hệ thống Quy tắc / Tra cứu (No AI) | Dịch vụ AI / LLM (Need AI) |
| :--- | :--- | :--- |
| **Bản chất dữ liệu** | Dữ liệu bảng có cấu trúc (`offices.csv`, CSDL, API). | Dữ liệu phi cấu trúc (văn bản quy chế, PDF sổ tay, câu hỏi mở). |
| **Độ đa dạng ngôn ngữ** | Từ khóa cố định, câu lệnh cú pháp chuẩn, ý định đóng. | Tiếng lóng, viết tắt, từ địa phương, diễn đạt gián tiếp/đa ý. |
| **Logic xử lý** | Khớp chuỗi (exact/partial match), tra cứu khóa chính, logic if-else. | Suy luận đa bước (multi-step reasoning), tóm tắt, tạo sinh văn bản. |
| **Chi phí & Độ trễ** | Thực thi tức thì (< 5ms), chi phí tính toán $\approx 0$. | Tốn token/API, độ trễ cao hơn (500ms - vài giây). |

---

## 2. 10 câu hỏi KHÔNG CẦN AI (Deterministic / Rule-based)

Các câu hỏi này có thể xử lý hoàn toàn bằng cơ chế tra cứu từ điển/CSV, Regex hoặc câu lệnh hệ thống tĩnh.

| STT | Câu hỏi (User Query) | Thành phần xử lý | Lý do 1 dòng (One-line Reason) |
| :---: | :--- | :--- | :--- |
| 1 | "Phòng Đào tạo ở đâu?" / "Where is the Training Office?" | Lookup `data/offices.csv` | Tra cứu vị trí phòng học trực tiếp từ cột `room` của bảng dữ liệu có sẵn. |
| 2 | "Thư viện mở cửa lúc mấy giờ?" | Lookup `data/offices.csv` | Lấy giờ làm việc cố định theo tên phòng từ trường `hours` trong CSV. |
| 3 | "Xin chào" / "Hello" | Static intent dictionary | Khớp trực tiếp với danh sách các từ khóa chào hỏi tĩnh đã định nghĩa trước. |
| 4 | "Help" / "Trợ giúp" | Help command handler | Trả về thông điệp tĩnh liệt kê cú pháp và các lệnh hệ thống được hỗ trợ. |
| 5 | "Số điện thoại của Trạm Y tế trường là gì?" | Contact database lookup | Truy vấn giá trị trường số điện thoại cố định của một đơn vị trong cơ sở dữ liệu. |
| 6 | "Hôm nay là thứ mấy, ngày mấy?" | System runtime (`datetime`) | Lấy thông tin thời gian hiện tại từ đồng hồ hệ điều hành một cách xác định. |
| 7 | "Học phí một tín chỉ ngành Công nghệ thông tin là bao nhiêu?" | Tuition fee table lookup | Lấy giá trị học phí cố định đã được cấu hình trong bảng đơn giá tín chỉ. |
| 8 | "Phòng I.101 là văn phòng của đơn vị nào?" | Reverse lookup in CSV | Truy vấn ngược từ mã phòng học (`room`) để tìm tên đơn vị (`name`) trong CSV. |
| 9 | "Xem thời khóa biểu hôm nay của sinh viên 25125089" | Student portal API call | Gọi API cổng thông tin đào tạo với mã số sinh viên để trả về dữ liệu lịch học cụ thể. |
| 10 | "quit" / "exit" | CLI flow controller | Nhận diện câu lệnh điều khiển hệ thống để thoát phiên làm việc dòng lệnh. |

---

## 3. 10 câu hỏi CẦN AI (LLM / Generative AI / NLU)

Các câu hỏi này yêu cầu hiểu ngữ cảnh phức tạp, tổng hợp tài liệu quy chế dài hoặc tạo sinh nội dung cá nhân hóa.

| STT | Câu hỏi (User Query) | Năng lực AI yêu cầu | Lý do 1 dòng (One-line Reason) |
| :---: | :--- | :--- | :--- |
| 1 | "Em bị rớt môn Đại số tuyến tính thì nên học lại kỳ hè hay học kỳ sau để không trễ tiến độ tốt nghiệp?" | Multi-step reasoning | Cần suy luận logic dựa trên cây môn học tiên quyết và lộ trình học tập cá nhân. |
| 2 | "Tóm tắt quy định xét học bổng khuyến khích học tập năm 2026 từ sổ tay sinh viên." | Document summarization / RAG | Đòi hỏi đọc hiểu văn bản pháp quy dài và tổng hợp các tiêu chí cốt lõi thành bản tóm tắt. |
| 3 | "Viết giúp em email gửi giảng viên xin nộp bài tập lớn trễ 2 ngày do bị ốm có giấy viện." | Text generation | Cần kỹ năng tạo sinh văn bản với văn phong trang trọng, chuẩn mực và đúng hoàn cảnh. |
| 4 | "Phòng đào tạo sáng ni có làm việc k mn ơi, e muốn nộp đơn hoãn thi gấp." | NLU & Ambiguity resolution | Cần xử lý ngôn ngữ tự nhiên chứa từ địa phương, viết tắt và tách đa ý định trong một câu. |
| 5 | "So sánh sự khác nhau về định hướng nghề nghiệp giữa ngành Kỹ thuật Phần mềm và Khoa học Máy tính." | Knowledge synthesis | Cần tổng hợp, đối chiếu và phân tích trừu tượng từ nhiều nguồn kiến thức đào tạo. |
| 6 | "Em đang cảm thấy quá tải và kiệt sức vì đồ án cuối kỳ, em nên bắt đầu gỡ rối từ đâu?" | Empathetic guidance | Cần phản hồi mang tính đồng cảm, định hướng tâm lý và gợi ý các kênh hỗ trợ phù hợp. |
| 7 | "Giải thích thuật toán Dijkstra bằng một ví dụ thực tế dễ hiểu cho người mới học." | Pedagogical explanation | Đòi hỏi khả năng diễn giải khái niệm kỹ thuật phức tạp thành hình ảnh ẩn dụ đời thường. |
| 8 | "Quy trình xin mở một Câu lạc bộ học thuật mới trong trường gồm những bước nào?" | Multi-document synthesis | Cần tổng hợp thủ tục từ nhiều văn bản hướng dẫn Đoàn - Hội thành các bước thực hiện tuần tự. |
| 9 | "Em nộp nhầm file nháp lên hệ thống nộp bài và bị chấm 0 điểm, em có thể làm đơn phúc khảo như thế nào?" | Contextual policy advising | Cần phân tích tình huống thực tế, đối chiếu quy chế thi cử và hướng dẫn các bước giải trình. |
| 10 | "Gợi ý lộ trình tự học lập trình Web Fullstack từ cơ bản đến nâng cao trong 6 tháng cho sinh viên năm nhất." | Personalized curriculum design | Yêu cầu phân bổ khối lượng kiến thức theo thời gian và khả năng tiếp thu của người học. |
