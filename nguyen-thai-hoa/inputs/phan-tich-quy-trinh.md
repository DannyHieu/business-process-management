


BÁO CÁO PHÂN TÍCH QUY TRÌNH PHÁT TRIỂN PHẦN MỀM (MÔ HÌNH OUTSOURCE)
1. Phân tích giá trị gia tăng (Value-Added Analysis)
Các hoạt động trong quy trình được phân loại thành 3 nhóm:
VA (Value-Adding): Hoạt động trực tiếp tạo ra giá trị mà khách hàng sẵn sàng chi trả.
VBA (Value-Business-Adding): Hoạt động không tạo giá trị trực tiếp cho khách hàng nhưng bắt buộc phải có để doanh nghiệp vận hành (pháp lý, quản trị rủi ro).
NVA (Non-Value-Adding): Hoạt động lãng phí, cần loại bỏ hoặc tối ưu hóa.

1.1. Bảng phân tích chi tiết các hoạt động
STT
Tên hoạt động trong quy trình
Phân loại
Mô tả nguyên do
Đề xuất khắc phục / Tối ưu
1
Gửi yêu cầu phát triển phần mềm 


VA
Khởi tạo nhu cầu cốt lõi của dự án từ phía Khách hàng.
Cung cấp sẵn biểu mẫu (Form) để khách hàng điền đầy đủ thông tin ngay từ đầu.
2
Gửi phân tích sơ bộ 


VBA
Bắt buộc để luân chuyển thông tin nội bộ cho đội ngũ đánh giá.
Tự động hóa luồng tickiting (ví dụ qua Jira/Trello).
3
Phân tích yêu cầu sơ bộ 


VBA
Giúp định hình bài toán kinh doanh, không tạo mã nguồn nhưng cần thiết để báo giá.
Sử dụng Checklist mẫu để rút ngắn thời gian phân tích.
4
Đánh giá tính khả thi và estimate 


VBA
Dự trù rủi ro kỹ thuật và nguồn lực, phục vụ cho việc tính chi phí.
Xây dựng bộ định mức thời gian (Effort estimation matrix) cho các tính năng cơ bản.
5
Báo giá sơ bộ 


VBA
Hoạt động thương mại bắt buộc để chốt giao dịch.
Dùng phần mềm tạo báo giá tự động dựa trên man-days.
6
Kiểm tra báo giá sơ bộ 


VA
Khách hàng rà soát để đảm bảo ngân sách phù hợp.
Trình bày báo giá rõ ràng, minh bạch các khoản mục.
7
Ký hợp đồng 


VBA
Chốt chặn pháp lý quan trọng nhất để khởi động dự án.
Sử dụng hợp đồng điện tử (e-contract) để rút ngắn thời gian chờ đợi.
8
Lây yêu cầu chi tiết 


VBA
Quá trình khơi gợi yêu cầu (Elicitation) để hiểu rõ nghiệp vụ khách hàng.
Thu âm hoặc ghi biên bản họp (MoM) rõ ràng ngay sau buổi họp.
9
Cung cấp yêu cầu 


VA
Khách hàng cung cấp nguyên liệu đầu vào (tài liệu, quy trình cũ).
Hướng dẫn khách hàng chuẩn bị sẵn tài liệu trước buổi Kick-off.
10
Phân tích đặc tả phần mềm 


VA
Chuyển đổi ý tưởng thành bản vẽ kỹ thuật chi tiết.
Sử dụng wireframe/mockup để minh họa trực quan.
11
Viết tài liệu 


VA
Tài liệu SRS là tài sản mà khách hàng sở hữu để kiểm chứng phần mềm.
Sử dụng các công cụ viết tài liệu chuẩn hóa (Confluence).
12
Yêu cầu chỉnh sửa 


NVA
Vòng lặp phát sinh do khách hàng chưa ưng ý tài liệu.
BA cần xác nhận từng phần nhỏ thay vì đợi viết xong toàn bộ mới gửi duyệt.
13
Gửi thông báo tài liệu được duyệt 


VA
Chốt chặn phạm vi (Scope baseline) để team bắt đầu sản xuất.
Dùng quy trình duyệt qua email hoặc hệ thống ký số.
14
Chốt phạm vi công việc 


VBA
Tránh rủi ro trôi trượt phạm vi (Scope Creep) về sau.
Đóng băng yêu cầu (Freeze requirement), mọi thay đổi sau bước này tính là CR.
15
Lập kế hoạch công việc và các mốc giao hàng 


VBA
Phục vụ công tác quản lý tiến độ nội bộ.
Áp dụng Agile/Scrum để lập kế hoạch linh hoạt theo Sprint.
16
Viết test cases 


VBA
Đảm bảo tiêu chuẩn chất lượng công ty, không bán trực tiếp cho khách.
Dùng kỹ thuật kiểm thử (Test design techniques) để tối ưu số lượng test case.
17
Viết code và unit test 


VA
Hoạt động cốt lõi trực tiếp tạo ra sản phẩm phần mềm.
Tuân thủ Clean Code và chạy tự động Unit Test trên CI/CD.
18
Triên khai lên môi trường kiểm thử 


VA
Bắt buộc để phần mềm có nơi vận hành thử nghiệm.
Tự động hóa bằng các pipeline (Jenkins, GitLab CI).
19
Kiểm thử 


VBA
Lọc lỗi trước khi giao cho khách hàng.
Tự động hóa các kịch bản kiểm thử hồi quy (Regression test).
20
Báo bug 


NVA
Lãng phí do làm sai ngay từ đầu.
Áp dụng template báo lỗi chuẩn (Steps to reproduce, Expected, Actual).
21
Sửa bug 


NVA
Công việc làm lại (Rework) gây tốn chi phí (Cost of poor quality).
Đẩy mạnh khâu Code Review chéo giữa các Dev trước khi merge code.
22
QA Sign-off 


VBA
Cổng kiểm duyệt chất lượng cuối cùng của nội bộ.
Quy định rõ ràng bộ tiêu chí hoàn thành (Definition of Done).
23
Triển khai lên môi trường UAT 


VA
Đưa sản phẩm lên môi trường giống hệt thực tế để khách hàng kiểm chứng.
Thiết lập môi trường UAT cô lập, dữ liệu sạch.
24
Kiểm thử dựa trên trường hợp thực tế (UAT) 


VA
Khách hàng trải nghiệm và xác nhận giá trị phần mềm.
Cung cấp kịch bản UAT (UAT Script) hỗ trợ khách hàng test đúng trọng tâm.
25
Thông báo lỗi UAT 


NVA
Vòng lặp phát sinh do lỗi lọt ra ngoài phạm vi kiểm soát của nội bộ.
Nâng cao chất lượng test nội bộ, bổ sung kịch bản test thực tế.
26
Phân tích lỗi 


VBA
Cần thiết để phân định rạch ròi giữa Lỗi (Bug) và Tính năng mới (CR).
Cần có BA và PM cùng tham gia đánh giá với Dev để tránh tranh cãi.
27
Làm báo giá Change Request 


VBA
Bảo vệ doanh thu của công ty khi khách hàng thay đổi yêu cầu.
Có sẵn bảng giá (Rate card) theo giờ/ngày công để báo giá nhanh.
28
Quy trình Change Request 


VBA
Bắt buộc để thực thi sự thay đổi một cách có kiểm soát.
Gom nhóm các CR nhỏ để xử lý thành 1 đợt.
29
UAT Sign-off 


VA
Bằng chứng cho thấy phần mềm đã đạt giá trị kỳ vọng.
Ký số trên biên bản nghiệm thu UAT.
30
Triên khai lên môi trường production 


VA
Đưa phần mềm vào vận hành thực tế, sinh lời cho khách hàng.
Lên kế hoạch Go-live chi tiết, có phương án rollback nếu lỗi.
31
Bàn giao tài liệu kỹ thuật, source code và asset liên quan 


VA
Chuyển giao toàn quyền sở hữu tài sản số cho khách hàng.
Đóng gói tài liệu trên môi trường cloud bảo mật.
32
Nghiệm thu 


VA
Hoạt động công nhận sự thành công của toàn bộ dự án.
Hoàn thiện sớm hồ sơ nghiệm thu từ lúc UAT.
33
Thanh toán 


VA
Hoàn thành nghĩa vụ tài chính, mang lại dòng tiền.
Theo sát tiến độ làm thủ tục của kế toán khách hàng.

1.2. Phân tích trên quy trình

Link Github:
business-process-management/nguyen-thai-hoa/do_an_quy-trinh-phat-trien-phan-mem-1-phan-tich-gtgt.svg at main · DannyHieu/business-process-management 
business-process-management/nguyen-thai-hoa/do_an_quy-trinh-phat-trien-phan-mem-1-phan-tich-gtgt.bpmn at main · DannyHieu/business-process-management 

2. Phân tích sự lãng phí (Waste Analysis)
Dựa trên nguyên tắc tinh gọn (Lean), quy trình hiện tại xuất hiện 3 dạng lãng phí đặc thù của ngành công nghiệp phần mềm: Move (Chuyển giao thông tin), Hold (Chờ đợi), và Overdo (Làm quá mức cần thiết).



2.1. Bảng phân tích chi tiết
Nhóm Lãng phí
Hoạt động lãng phí trong quy trình
Nguyên nhân (Mô tả)
Cách khắc phục
Move 
Luồng tin nhắn/Message Flow Yêu cầu chỉnh sửa và Gửi lại tài liệu. 


Việc giao tiếp qua lại bằng file rời (Word/Excel) hoặc email khiến thông tin bị phân mảnh, dễ hiểu sai ý nhau.
Sử dụng các công cụ cộng tác trực tuyến (Figma, Google Docs) để chốt yêu cầu ngay trong thời gian thực.
Move 
Tác vụ Báo bug từ QA sang Dev. 


Ghi nhận lỗi thiếu thông tin (thiếu hình ảnh, không rõ môi trường), dẫn đến việc Dev phải tốn thời gian trao đổi lại với QA để tìm cách tái hiện lỗi.
Quy chuẩn hóa định dạng ticket lỗi. Quay video màn hình thao tác lỗi đính kèm vào ticket.
Hold 
Event Đợi phản hồi UAT. 


Dự án bị tạm dừng do khách hàng bận công việc kinh doanh, chậm trễ trong việc xếp lịch dùng thử phần mềm.
Thỏa thuận rõ SLA trong hợp đồng: Khách hàng có tối đa 5-7 ngày để UAT, quá hạn mặc định là Pass.
Hold 
Event Chờ xác nhận thanh toán. 


Quy trình hành chính, kế toán từ phía khách hàng rườm rà; hồ sơ bàn giao bị trả về do sai sót biểu mẫu.
Chuẩn bị trước bộ hồ sơ nghiệm thu theo đúng form của kế toán khách hàng ngay từ khi vừa Sign-off UAT.
Overdo
Tác vụ Làm báo giá Change Request cho các sửa đổi quá nhỏ. 


Áp dụng luồng quy trình quá cứng nhắc. PM dừng dự án để làm báo giá chỉ vì khách muốn đổi màu một nút bấm hoặc sửa vài dòng chữ.
Tạo "Quỹ thời gian dự phòng" (Buffer time) khoảng 10% tổng dự án để PM chủ động duyệt và xử lý luôn các CR nhỏ lẻ, giữ nhịp độ bàn giao.
Overdo
Tác vụ Viết test cases ở mức độ chi tiết thái quá. 


Viết test case tĩnh quá chi tiết trong khi giao diện/yêu cầu phần mềm chưa được chốt cứng, dẫn đến việc phải vứt bỏ hoặc viết lại toàn bộ kịch bản.
Áp dụng Checklist kiểm thử ở giai đoạn đầu, chỉ đi sâu viết chi tiết (Step-by-step) cho các luồng nghiệp vụ lõi (Thanh toán, Xác thực).

2.2. Phân tích trên quy trình

Link Github:
business-process-management/nguyen-thai-hoa/ptlp-do_an_quy-trinh-phat-trien-phan-mem-1.svg at main · DannyHieu/business-process-management 
business-process-management/nguyen-thai-hoa/ptlp-do_an_quy-trinh-phat-trien-phan-mem-1.bpmn at main · DannyHieu/business-process-management 

3. Phân tích các bên liên quan
Trong quy trình phát triển phần mềm mô hình Outsource, khâu rủi ro nhất thường nằm ở sự tương tác giữa Công ty phần mềm và Khách hàng tại điểm chạm nghiệm thu. Do đó, mô hình Xương cá dưới đây được thiết lập để "mổ xẻ" một vấn đề nhức nhối điển hình làm ảnh hưởng đến tiến độ và doanh thu của dự án.
3.1. Xác định Vấn đề Trung tâm (Đầu cá - Issue)
Vấn đề (Issue): Khách hàng chậm trễ hoặc từ chối ký "UAT Sign-off" (Nghiệm thu người dùng).
Hậu quả: Gây ách tắc luồng công việc, đội lập trình không thể "Triển khai lên môi trường production", dự án rơi vào trạng thái "Chờ xác nhận thanh toán" kéo dài khiến công ty bị chôn vốn.
3.2. Phân tích 6 yếu tố nguyên nhân (6M) tác động lên Stakeholder
Ta phân rã nguyên nhân khiến khách hàng có hành vi chậm trễ/từ chối nghiệm thu thông qua 6 nhánh xương cá (6M), đồng thời xác định rõ bên liên quan nào (Stakeholder) đang chịu trách nhiệm cho nguyên nhân đó.
3.2.1. Man (Con người)
Bên liên quan trực tiếp: Khách hàng, Business Analyst (BA).
Nguyên nhân chính (Primary): Khách hàng thiếu chuyên môn IT để tự thực hiện "Kiểm thử dựa trên trường hợp thực tế (UAT)". Họ có tâm lý sợ hãi, sợ nghiệm thu xong phần mềm sập thì mình phải chịu trách nhiệm.
Nguyên nhân phụ (Secondary): Ban giám đốc của khách hàng giao việc test UAT cho các nhân viên cấp dưới – những người không tham gia từ đầu và không nắm rõ "Phân tích đặc tả phần mềm".
3.2.2. Method (Phương pháp)
Bên liên quan trực tiếp: Project Manager (PM), Khách hàng.
Nguyên nhân chính (Primary): Thiếu kịch bản và phương pháp hướng dẫn UAT rõ ràng. Khách hàng bị ném cho một đường link phần mềm và bị yêu cầu tự test mà không biết phải bắt đầu từ đâu.
Nguyên nhân phụ (Secondary): PM không tổ chức buổi họp (Training/Workshop) để hướng dẫn khách hàng cách sử dụng và cách ghi nhận "Thông báo lỗi UAT".
3.2.3. Machine (Công cụ / Hạ tầng)
Bên liên quan trực tiếp: Development Team (Dev).
Nguyên nhân chính (Primary): Tác vụ "Triển khai lên môi trường UAT" được thực hiện trên một hạ tầng server kém ổn định, giật lag hoặc chứa đầy dữ liệu rác (dummy data), khiến khách hàng có trải nghiệm tồi tệ ngay lần đầu dùng thử.
Nguyên nhân phụ (Secondary): Công cụ dùng để khách hàng báo lỗi (Jira, Trello) quá phức tạp đối với người dùng phi kỹ thuật.
3.2.4. Material (Đầu vào / Dữ liệu)
Bên liên quan trực tiếp: Business Analyst (BA), Khách hàng.
Nguyên nhân chính (Primary): Đầu vào của dự án – tức "Đặc tả phần mềm" – bị viết quá mơ hồ, không lột tả hết nghiệp vụ thực tế của khách hàng.
Nguyên nhân phụ (Secondary): Khách hàng không đọc kỹ tài liệu nhưng vẫn "Gửi thông báo tài liệu được duyệt". Đến khi thấy phần mềm thực tế, họ phát hiện ra nó không giống như những gì họ tưởng tượng, dẫn đến việc họ viện cớ báo lỗi để đòi "Quy trình Change Request" miễn phí.
3.2.5. Measurement (Đo lường / Tiêu chuẩn)
Bên liên quan trực tiếp: Sales, Project Manager (PM).
Nguyên nhân chính (Primary): Không thống nhất bộ tiêu chí "Hoàn thành" (Definition of Done) với khách hàng ngay tại bước "Ký hợp đồng". Khách hàng không biết thế nào là một tính năng đã đạt chuẩn để ký nghiệm thu.
Nguyên nhân phụ (Secondary): Trong hợp đồng không thiết lập SLA (Cam kết chất lượng dịch vụ) quy định thời hạn tối đa để "Đợi phản hồi UAT". Khách hàng ngâm bản test bao lâu cũng không bị vi phạm hợp đồng.
3.2.6. Milieu (Môi trường / Bối cảnh)
Bên liên quan trực tiếp: Khách hàng.
Nguyên nhân chính (Primary): Môi trường kinh doanh nội bộ của khách hàng đang rơi vào mùa cao điểm, không có bất kỳ nhân sự nào rảnh rỗi để ưu tiên cho việc test phần mềm.
Nguyên nhân phụ (Secondary): Người phụ trách dự án (Sponsor) phía khách hàng bất ngờ nghỉ việc hoặc bị luân chuyển, người mới lên thay không nắm được lịch sử dự án nên không dám ký "UAT Sign-off".
3.3. Nhật ký vấn đề và Đề xuất hành động (Issue Register & Mitigation)
Từ việc mổ xẻ nguyên nhân qua Mô hình Xương cá, Quản lý dự án (PM) sẽ lập sổ đăng ký phát hành (Issue Register) để đưa ra các biện pháp phản ứng với Stakeholder:
Phản ứng với nhóm Man & Method: PM và QA phải tạo ra một bảng "UAT Checklist" (đánh dấu tick) đơn giản bằng Excel và tổ chức một buổi Google Meet 30 phút để hướng dẫn khách hàng test từng luồng một thay vì để họ tự bơi.
Phản ứng với nhóm Material & Measurement: Cập nhật ngay vào mẫu hợp đồng của khối Sales điều khoản: "Nếu sau 07 ngày kể từ lúc nhận tài khoản UAT mà khách hàng không có phản hồi, hệ thống mặc định được nghiệm thu (Auto Sign-off)".
Phản ứng với nhóm Machine: Yêu cầu Dev phải chuẩn bị sẵn Data mồi (Master data) giống hệt thực tế để trải nghiệm test của khách hàng được mượt mà nhất.

4. Phân tích định lượng (Quantitative Analysis)
4.1. Mô hình quy trình (Định nghĩa biến số và thông số)
Để phục vụ việc tính toán, quy trình Phát triển phần mềm Outsource được mô hình hóa thành 5 khối công việc chính. Các thông số thời gian (T - đo bằng ngày) và xác suất rẽ nhánh/làm lại (p, r) được ước lượng dựa trên dữ liệu lịch sử của công ty:
Khối 1: Khởi tạo & Ký hợp đồng (Tuần tự): T1 = 3 ngày.
Khối 2: Phân tích & Chốt tài liệu (Vòng lặp Rework): Thời gian BA làm tài liệu T2 = 3 ngày. Xác suất khách hàng yêu cầu sửa lại (Rework) là r1 = 20% (0.2).
Khối 3: Thực thi (Đường song song - Parallel Paths): Dev viết code (T3A = 15 ngày) và QA viết test case (T3B = 3 ngày) thực hiện cùng lúc.
Khối 4: Kiểm thử nội bộ (Vòng lặp Rework): Thời gian test T4 = 2 ngày. Xác suất có bug phải trả về cho Dev sửa là r2 = 30% (0.3).
Khối 5: UAT & Bàn giao (Vòng lặp Rework): Thời gian UAT và Deploy T5 = 4 ngày. Xác suất khách hàng bắt lỗi UAT phải làm lại là r3 = 20% (0.2).
4.2. Xác định kịch bản (Scenario Definition)
Kịch bản hiện tại (As-Is Scenario):
Mục tiêu là tính toán Thời gian chu kỳ (Cycle Time - CT) kỳ vọng để hoàn thành một dự án phần mềm cơ bản dựa trên các thông số hiện tại. Việc tính toán sẽ áp dụng bộ công thức Flow Analysis cho từng dạng mô hình (Tuần tự, Song song, Vòng lặp).
4.3. Chạy mô phỏng (Tính toán Flow Analysis)
Áp dụng công thức tính cho từng dạng mô hình phân nhánh, ta có kết quả mô phỏng từng khối như sau:
Thời gian chu kỳ Khối 1 (Đường tuần tự):
Áp dụng CT = T1 + T2 + ... + Tn:
CT1 = T1 = 3 (ngày)
Thời gian chu kỳ Khối 2 (Vòng lặp Rework - Khách sửa tài liệu):
Áp dụng CT = T / (1 - r):
CT2 = 5 / (1 - 0.2) = 6.25 (ngày)
Thời gian chu kỳ Khối 3 (Đường song song - Parallel Paths):
Áp dụng CT = max(T1, T2, … Tn):
CT3 = max(15, 3) = 15 (ngày)
Thời gian chu kỳ Khối 4 (Vòng lặp Rework - Bug nội bộ):
Áp dụng CT = T / (1 - r):
CT4 = 2 / (1 - 0.3) ~ 2.86 (ngày)
Thời gian chu kỳ Khối 5 (Vòng lặp Rework - Lỗi UAT):
Áp dụng CT = T / (1 - r):
CT5 = 4 / (1 - 0.2) = 5 (ngày)
Tổng Thời gian chu kỳ (Total Cycle Time) của toàn bộ dự án:
CT = CT1 + CT2 + CT3 + CT4 + CT5 = 3 + 6.25 + 15 + 2.86 + 5 = 32.11 (ngày)
Hiệu suất thời gian (Cycle Time Efficiency):
Thời gian xử lý lý tưởng (Processing Time) nếu không có bất kỳ vòng lặp làm lại nào là: PT = 3 + 5 + max(15, 3) + 2 + 4 = 29 ngày.
Hiệu suất thời gian = Thời gian xử lý / Thời gian chu kỳ
Hiệu suất = 29 / 32.11 ~ 90.3%
4.4. Phân tích kết quả đầu ra (Output Analysis)
Dựa trên kết quả mô phỏng, ta rút ra các nhận định sau:
Nút thắt cổ chai (Bottlenecks) nằm ở các Rework Loop: Mặc dù thời gian xử lý gốc của Khối 2 (Làm tài liệu) chỉ là 5 ngày, nhưng do xác suất khách hàng bắt sửa lại lên tới 20%, thời gian thực tế bị đội lên thành 6.25 ngày. Tương tự, khâu Test nội bộ bị kéo dài thêm gần 1 ngày do tỷ lệ lỗi 30%.
Hiệu quả của việc chạy song song (Parallel Paths): Khối 3 được tối ưu rất tốt bằng việc cho QA và Dev chạy song song. Thời gian chu kỳ chỉ phụ thuộc vào nhánh dài nhất là Dev (15 ngày), giúp tiết kiệm hoàn toàn 3 ngày của QA.
Đánh giá hiệu suất: Hiệu suất thời gian đạt mức khá cao (~90.3%) do thời gian làm lại (Rework) chiếm khoảng 10% tổng thời lượng. Việc tính toán hiệu suất này rất quan trọng để đối chiếu với các mục tiêu kinh doanh..
4.5. Lặp lại các trường hợp thay thế (What-If Analysis)
Để đề xuất giải pháp cải tiến (To-Be Process), ta lặp lại kịch bản chạy mô phỏng với các thông số đầu vào được thay đổi (Alternative scenarios):
Kịch bản 1: Cải tiến khâu Phân tích nghiệp vụ (Giảm tỷ lệ Rework tài liệu)
Giả định: Công ty áp dụng phần mềm vẽ Mockup trực quan, giúp khách hàng dễ hình dung và chốt yêu cầu nhanh hơn. Tỷ lệ sửa tài liệu r1 giảm từ 20% xuống còn 5%.
Chạy lại mô phỏng Khối 2: CT2 = 5 (1 - 0.05) = 5.26 ngày.
Kết quả: Tiết kiệm được xấp xỉ 1 ngày công của BA so với kịch bản As-Is (6.25 ngày).
Kịch bản 2: Áp dụng TDD (Test-Driven Development) giảm lỗi nội bộ
Giả định: Dev viết Unit Test chặt chẽ hơn, thời gian code tăng nhẹ (nhánh Dev T3A lên 16 ngày) nhưng bù lại tỷ lệ Bug nội bộ (r2) giảm từ 30% xuống 10%.
Chạy lại mô phỏng:
Khối 3: CT3 = max(16, 3) = 16 ngày.
Khối 4 (Test nội bộ): CT4 = 2 / (1-0.1) = 2.22 ngày.
Kết quả: Tổng thời gian Khối 3 + Khối 4 là 16 + 2.22 = 18.22 ngày. So với kịch bản cũ (15 + 2.86 = 17.86 ngày), kịch bản này làm dự án chậm thêm một chút. Phân tích này cho thấy nếu tăng thời gian code quá nhiều chỉ để giảm một lượng nhỏ bug ở khâu test ngắn hạn thì chưa chắc đã mang lại lợi ích về tổng thời gian (Cycle Time).
Kịch bản 3: Rủi ro thảm họa ở khâu UAT (Unhappy Case)
Giả định: Khách hàng test UAT cực kỳ khắt khe, xác suất bắt lỗi bắt làm lại r3 tăng đột biến lên 50%.
Chạy lại mô phỏng Khối 5: CT5 = 4 / (1 - 0.5) = 8 ngày.
Kết quả: Thời gian khâu UAT bị nhân đôi (từ 4 ngày lên 8 ngày). Rủi ro này kéo theo nguy cơ vỡ hợp đồng và phạt chậm tiến độ cực kỳ cao. Dự án cần thiết lập ngay cổng Sign-off nghiêm ngặt ở các bước trước để tránh kịch bản này xảy ra.

