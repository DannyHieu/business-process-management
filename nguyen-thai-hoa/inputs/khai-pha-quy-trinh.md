
I. Phương pháp thực hiện: Dựa trên bằng chứng (Evidence-based)
1. Mô tả quy trình hiện có (As-Is Process)
Thực trạng: Hiện tại, công ty chưa có quy trình chuẩn hóa. Bộ phận Sales thường chốt hợp đồng dựa trên các yêu cầu miệng hoặc tài liệu rất sơ sài từ khách hàng. Business Analyst (BA) bị cuốn vào việc giải quyết phát sinh thay vì phân tích từ đầu.
Vấn đề: Khách hàng thường xuyên thêm yêu cầu mới ở giai đoạn UAT (Nghiệm thu) nhưng không bị tính thêm phí (Scope creep). Đội QA và Dev làm việc chồng chéo, không có cổng phê duyệt (Sign-off) rõ ràng, dẫn đến trễ deadline và đội chi phí.
2. Sơ đồ tổ chức (Organizational Chart)
Ban Giám đốc (BOD): Phê duyệt ngân sách và các hợp đồng lớn.
Khối Kinh doanh (Sales/Account): Tiếp cận khách hàng, lập báo giá.
Khối Sản xuất (Delivery):
Project Management Office (PMO): Quản lý dự án (PM).
Bộ phận Phân tích nghiệp vụ: Business Analyst (BA).
Đội Kỹ thuật: Lập trình viên (Dev), Kỹ sư QA/Tester.
3. Kế hoạch làm việc (Kế hoạch khai phá quy trình)
Tuần 1: Thu thập toàn bộ biểu mẫu, tài liệu dự án cũ (Hợp đồng, SRS, Biên bản nghiệm thu).
Tuần 2: Tổ chức Workshop với các Trưởng bộ phận (Sales, PM, Dev Lead, QA Lead) để xác định các điểm nghẽn (bottlenecks).
Tuần 3: Phỏng vấn sâu 1-1 với nhân sự trực tiếp thực thi và đại diện Khách hàng.
Tuần 4: Vẽ sơ đồ quy trình As-Is và đề xuất quy trình To-Be (BPMN).
4. Thuật ngữ và sổ tay (Glossary)
RFP (Request for Proposal): Hồ sơ yêu cầu báo giá từ khách hàng.
SRS (Software Requirements Specification): Tài liệu đặc tả yêu cầu phần mềm.
UAT (User Acceptance Testing): Giai đoạn khách hàng kiểm thử nghiệm thu.
CR (Change Request): Yêu cầu thay đổi/thêm tính năng ngoài phạm vi hợp đồng.
Sign-off: Hành động ký duyệt, đồng ý chuyển sang giai đoạn tiếp theo.
5. Biểu mẫu và Workshop
Kịch bản Workshop khai phá: Khởi động (Nêu lý do thất bại của dự án cũ) -> Brainstorming (Ghi nhận khó khăn trên giấy note) -> Phân nhóm vấn đề -> Đề xuất hướng giải quyết.
Biểu mẫu cuộc họp (Meeting Minutes Form): Bao gồm: Thời gian, Thành phần tham dự, Nền tảng (Google Meet/Offline), Quyết định đã chốt (Scope, Timeline), Các rủi ro (Risk Log), và Chữ ký số của Khách hàng.
II. Phương pháp thực hiện: Phỏng vấn (Interview)
Dưới đây là danh sách 20 câu hỏi phỏng vấn dành cho các đối tượng liên quan (PM, BA, Dev, QA, Sales, Khách hàng).
A. 10 Câu hỏi Định tính (Qualitative)
Khám phá nguyên nhân, cảm nhận và cách giải quyết vấn đề.
5 Câu hỏi có cấu trúc (Structured - Kịch bản cứng, hỏi chung cho các đối tượng):
(Cho PM) Anh/chị đánh giá thế nào về tính minh bạch của quy trình xử lý Change Request hiện tại?
(Cho BA) Khó khăn lớn nhất của anh/chị khi chốt tài liệu đặc tả (SRS) với khách hàng là gì?
(Cho QA) Theo anh/chị, nguyên nhân cốt lõi nào dẫn đến việc phát hiện lỗi trễ ở khâu UAT thay vì khâu Test nội bộ?
(Cho Sales) Khách hàng thường phàn nàn về vấn đề gì nhất ở giai đoạn chốt báo giá sơ bộ?
(Cho Dev) Môi trường Test và UAT hiện tại có đáp ứng đủ nhu cầu triển khai độc lập của team không?
5 Câu hỏi không có cấu trúc (Unstructured - Hỏi mở, đào sâu theo ngữ cảnh):
(Cho PM) Hãy kể về một dự án gần đây mà tình trạng "phình to phạm vi" (scope creep) xảy ra nghiêm trọng nhất. Anh/chị đã xử lý tình huống đó ra sao?
(Cho Khách hàng) Điều gì làm anh/chị cảm thấy hoang mang hoặc chưa hài lòng nhất trong quá trình nghiệm thu phần mềm đợt vừa rồi?
(Cho BA) Giả sử được quyền thay đổi một bước duy nhất trong cách giao tiếp với khách hàng, anh/chị sẽ thay đổi điều gì để chốt scope nhanh hơn?
(Cho QA) Kể lại một cuộc tranh luận đáng nhớ nhất giữa anh/chị và team Dev về việc xác định "đây là lỗi hay là tính năng mới".
(Cho Sales) Khi khách hàng ép tiến độ nhưng ngân sách thấp, anh/chị thường dùng mẹo gì để vừa ký được hợp đồng vừa bảo vệ được team sản xuất?
B. 10 Câu hỏi Định lượng (Quantitative)
Thu thập số liệu đo lường, tần suất, tỷ lệ và thang điểm.
5 Câu hỏi có cấu trúc (Structured - Trắc nghiệm, Thang đo Likert 1-5):
(Cho Dev) Đánh giá mức độ rõ ràng và hoàn thiện của tài liệu do BA cung cấp trên thang điểm từ 1 đến 5?
(Cho PM) Trung bình mỗi dự án outsource hiện tại phát sinh bao nhiêu Change Request (CR)? (A: Dưới 3 | B: Từ 3-5 | C: Trên 5).
(Cho Khách hàng) Mức độ hài lòng của anh/chị về thời gian phản hồi (SLA) của đội ngũ hỗ trợ trên thang điểm từ 1 đến 10?
(Cho Sales) Thời gian trung bình từ lúc nhận yêu cầu sơ bộ đến khi chốt được báo giá mất khoảng bao nhiêu ngày? (A: <3 ngày | B: 3-7 ngày | C: >7 ngày).
(Cho QA) Đâu là tỷ lệ phần trăm các lỗi (bugs) bị đẩy ngược từ môi trường UAT về lại môi trường Test? (A: <10% | B: 10-20% | C: >20%).
5 Câu hỏi không có cấu trúc (Unstructured - Đòi hỏi người được phỏng vấn tự ước lượng số liệu thực tế):
(Cho PM) Dựa trên kinh nghiệm quản lý, chi phí phát sinh do việc phải làm lại (rework) chiếm khoảng bao nhiêu phần trăm tổng ngân sách dự án?
(Cho QA) Anh/chị ước lượng mình bị lãng phí khoảng bao nhiêu giờ mỗi tuần chỉ để tạo test case cho những yêu cầu không được định nghĩa rõ ràng?
(Cho BA) Theo sổ tay ghi nhận của anh/chị, khoảng bao nhiêu phần trăm tài liệu yêu cầu (SRS) bị khách hàng yêu cầu viết lại sau lần gửi đầu tiên?
(Cho Dev) Trong một Sprint kéo dài 2 tuần, anh/chị thường phải trích ra mấy ngày công (man-days) chỉ để tập trung fix bug UAT từ phía khách hàng?
(Cho Sales) Anh/chị ước tính tỷ lệ chuyển đổi thành công (Conversion rate) từ bước gửi báo giá sơ bộ sang bước chính thức ký hợp đồng là bao nhiêu phần trăm?

