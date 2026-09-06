Phần 1: Giới thiệu và Tổng quan

### (0:00 - 0:45) Slide 1: Tổng quan quy trình phát triển phần mềm
"Dạ, em xin kính chào thầy cô và các bạn. Hôm nay, em xin đại diện trình bày về phân tích quy trình phát triển phần mềm theo mô hình outsource. Luồng quy trình này trải dài từ lúc khách hàng gửi yêu cầu cho đến khi dự án được nghiệm thu và thanh toán. Về cơ bản, quy trình gồm 5 giai đoạn chính: Khởi tạo báo giá, Chốt yêu cầu, Phát triển & Kiểm thử, Nghiệm thu UAT, và Đóng dự án.
Mục tiêu cốt lõi của quy trình không chỉ là hoàn thiện mã nguồn, mà còn là đảm bảo phạm vi rõ ràng, tiến độ được kiểm soát và sự đồng thuận giữa hai bên qua các điểm chốt chặn quan trọng như: chốt báo giá, duyệt đặc tả, và UAT sign-off."

### (0:45 - 1:30) Slide 2: Tác nhân, vai trò và giá trị mang lại
"Ở Slide 2, thầy cô và các bạn có thể thấy sự tham gia của nhiều tác nhân. Khách hàng là chủ sở hữu yêu cầu; Sales và BA là tuyến đầu làm rõ bài toán; PM giữ nhịp dự án; còn cụm Dev - QA là lực lượng thực thi chính.
Nhìn vào sơ đồ BPMN, quy trình có 3 điểm kết thúc (End Event) thực tế: Dự án dừng sớm vì không ký được hợp đồng; Dự án hoàn thành tốt đẹp; và kết thúc sau khi thanh toán xong."

### Slide 2.1
"Điều này khẳng định đây là một chuỗi thực thi mang tính thương mại và pháp lý rất rõ ràng. Giá trị cuối cùng quy trình mang lại không chỉ là phần mềm, mà là sự tin cậy và tính minh bạch."

### (1:30 - 2:30) Slide 3: Chi tiết quy trình
"Chuyển sang Slide 3 về luồng di chuyển chi tiết. Ban đầu, khách hàng đưa yêu cầu, nhóm nội bộ đánh giá khả thi và ra báo giá. Sau khi chốt, BA sẽ tiến hành phân tích thành tài liệu đặc tả (SRS). Khi phạm vi (scope) đã được khóa, team Dev bắt tay viết code, QA song song viết test case và tiến hành kiểm thử nội bộ.
Sau đó, sản phẩm được đưa lên môi trường UAT để khách hàng kiểm tra. Đây là một giai đoạn khá nhạy cảm: nếu có lỗi thì Dev phải sửa, còn nếu là tính năng mới thì sẽ kích hoạt luồng Change Request. Cuối cùng, khi mọi thứ đạt yêu cầu, phần mềm được deploy lên Production, bàn giao source code, chờ ký nghiệm thu và thanh toán. Đến đây là tròn một vòng đời dự án."

Phần 2: Phương pháp phân tích và Đánh giá lãng phí

### (2:30 - 3:15) Slide 4: Khai phá quy trình (Process Discovery)
"Để phân tích sâu hơn, ở Slide 4, nhóm đã áp dụng phương pháp khai phá quy trình dựa trên thực chứng (evidence-based). Dữ liệu được thu thập từ hợp đồng, biên bản, và phỏng vấn trực tiếp các team.
Quá trình này kết hợp cả định tính lẫn định lượng. Định tính để trả lời câu hỏi 'Tại sao' – ví dụ tại sao chốt SRS khó, tại sao lỗi lại lọt ra tới UAT. Còn định lượng dùng để đo lường 'Bao nhiêu' – ví dụ trung bình một dự án mất bao nhiêu thời gian cho việc làm lại (rework). Nhờ đó, quá trình đánh giá được chuyển từ cảm quan chủ quan sang các số liệu khách quan."

### (3:15 - 4:00) Slide 5: Phân tích Giá trị gia tăng
"Dựa trên bộ số liệu đó, ở Slide 5, các hoạt động được chia thành 3 nhóm. Nhóm VA (Value Added) là những công việc trực tiếp tạo ra giá trị cho khách hàng như: phân tích, viết code, UAT. Nhóm VBA là các việc bắt buộc công ty phải làm để vận hành như báo giá, quản lý dự án.
Đáng chú ý nhất là nhóm NVA (Non-Value Added) - bao gồm những lãng phí rành rành như: viết sai tài liệu phải sửa lại, hay dev code lỗi khiến QA phải test lại nhiều vòng. Đây chính là lỗ hổng làm tiêu hao chi phí dự án mà không mang lại giá trị."

### (4:00 - 4:20) Slide 6: Phân tích sự lãng phí (Nguyên lý Lean)
"Chiếu theo nguyên lý Lean ở Slide 6, lãng phí lớn nhất của quy trình hiện tại nằm ở hai yếu tố: 'Hold' tức là chờ đợi, và 'Move' tức là khâu chuyển giao. Việc các team phải đợi phản hồi từ đối tác, hoặc luân chuyển những luồng thông tin không rõ ràng đang bào mòn quỹ thời gian dự án. Hệ quả điển hình nhất của các lãng phí này chính là tình trạng ách tắc ở khâu UAT Sign-off."

### (4:20 - 4:45) Slide 7: Phân tích rủi ro UAT (Mô hình xương cá 6M)
"Bước sang Slide 7, để bóc tách nguyên nhân gây kẹt ở khâu UAT, nhóm áp dụng phương pháp phân tích xương cá theo mô hình 6M. Thầy cô và các bạn có thể thấy nguyên nhân đến từ nhiều phía đồng thời: có thể do khách hàng thiếu kỹ năng kiểm thử, môi trường hệ thống không ổn định, hoặc nghiêm trọng nhất là do quy trình nội bộ đã chuyển giao một sản phẩm chứa quá nhiều lỗi từ giai đoạn trước đó."

Phần 3: Phân tích định lượng và Đề xuất giải pháp

### (4:45 - 5:15) Slide 8: Nền tảng đo lường Định lượng
"Để chứng minh cho những lãng phí đó bằng các con số cụ thể, kính mời thầy cô và các bạn đi vào phần báo cáo định lượng. Nhằm thống nhất góc nhìn, chúng ta sẽ bám sát 4 chỉ số cốt lõi: PT - Thời gian xử lý thực tế, WT - Thời gian chờ, CT - Tổng thời gian chu kỳ, và CTE - Hiệu suất quy trình."

### (5:15 - 5:45) Slide 9: Đối chiếu AS-IS vs TO-BE
"Nhìn vào bảng đối chiếu ở slide này, điểm đáng lưu tâm nhất nằm ở khâu Viết code đang tiêu tốn đến 48 giờ, và Kiểm thử mất 32 giờ. Trong khi đó, thời gian chờ khách duyệt (WT) dẫu chiếm tới 72 giờ nhưng đa phần là thời gian thụ động. Do đó, mục tiêu tối ưu hóa bắt buộc phải tập trung trực tiếp vào việc cắt giảm 47% thời gian xử lý cốt lõi ở hai khâu code và test."

### (5:45 - 6:10) Slide 10: Sơ đồ dòng chảy (Điểm nghẽn)
"Chuyển sang Slide 10, nhìn trực tiếp lên sơ đồ đã được gắn nhãn, khu vực báo đỏ tập trung toàn bộ ở cụm Dev và QA. Tiến độ dự án đang bị 'thắt cổ chai' ngay tại đây với tỷ lệ phát sinh lỗi nội bộ cao đến 60%. Toàn bộ dòng chảy công việc gần như bị nghẽn lại, tạo ra vòng lặp sửa lỗi liên tục trước khi ra được sản phẩm cuối cùng."

### (6:10 - 6:35) Slide 11: Phân tích Nguyên nhân gốc rễ (3-WHY)
"Tại sao lỗi lại lọt tới 60%? Đi sâu vào phân tích 3-WHY ở Slide 11, nguyên nhân gốc rễ là do áp lực rà soát chất lượng bị dồn hết về giai đoạn cuối cho đội QA, và thực hiện hoàn toàn thủ công. Lập trình viên code xong xuôi mới chuyển qua test. Quy trình chưa tích hợp được automation, và Dev cũng chưa có công cụ hỗ trợ để rà soát code ngay từ lúc gõ phím."

### (6:35 - 7:00) Slide 12: Đề xuất khắc phục
"Để giải quyết triệt để tình trạng này, Slide cuối đưa ra các nhóm giải pháp hành động: Đưa ngay framework kiểm thử tự động vào luồng CI/CD, chuẩn hóa kiểm thử ngay từ giai đoạn đầu - theo hướng Shift-left testing. Đồng thời, ứng dụng công cụ AI để hỗ trợ Dev tăng tốc độ viết code. Riêng khâu UAT, cần thiết lập lại SLA để giới hạn thời gian chờ. Mục tiêu cuối cùng là cắt giảm 32% tổng thời gian chu kỳ và tối ưu triệt để chi phí rework.

Phần trình bày của nhóm đến đây là kết thúc, em xin cảm ơn thầy cô và các bạn đã chú ý lắng nghe. Kính mong nhận được thêm ý kiến đóng góp từ thầy cô ạ."