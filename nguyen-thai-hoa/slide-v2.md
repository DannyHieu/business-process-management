# Nội dung slide v2 - Quy trình phát triển phần mềm

## Slide 1: Tổng quan quy trình phát triển phần mềm

### Tiêu đề
Tổng quan quy trình phát triển phần mềm

### Nội dung chính
Quy trình phát triển phần mềm theo mô hình outsource gồm 5 giai đoạn chính: Khởi tạo & báo giá, Chốt yêu cầu chi tiết, Phát triển & kiểm thử nội bộ, Nghiệm thu người dùng (UAT), Bàn giao & đóng dự án.
Mục tiêu của quy trình là đảm bảo:
phạm vi công việc rõ ràng,
tiến độ được kiểm soát,
chất lượng phần mềm đạt yêu cầu,
sự đồng thuận giữa khách hàng và công ty.
Quy trình thực hiện theo logic liên tục và có điểm quyết định rõ ràng:
đồng ý báo giá hay không,
tài liệu được duyệt hay cần chỉnh sửa,
phần mềm có lỗi hay không,
UAT đạt yêu cầu hay cần xử lý Change Request,
khách hàng thanh toán và đóng dự án hay không.

### Hình minh họa
Sơ đồ tổng quan dạng flowchart với luồng chính: Khách hàng → Sales → BA/PM → Dev/QA → UAT → Bàn giao → Thanh toán.

---

## Slide 2: Tác nhân, vai trò, kết quả đầu ra và giá trị mang lại

### Tiêu đề
Tác nhân, vai trò, kết quả đầu ra và giá trị mang lại

### Nội dung chính
#### 1. Tác nhân và vai trò
Khách hàng: gửi yêu cầu phát triển phần mềm, duyệt báo giá, cung cấp tài liệu đặc tả, thực hiện UAT, ký nghiệm thu và thanh toán.
Sales: tiếp nhận yêu cầu đầu vào, báo giá sơ bộ, chốt hợp đồng với khách hàng.
Business Analyst (BA): làm rõ yêu cầu, phân tích nghiệp vụ, viết tài liệu đặc tả phần mềm (SRS).
Project Manager (PM): lập kế hoạch và chốt phạm vi, giám sát tiến độ, quản lý Change Request, hướng dẫn tiến trình UAT và bàn giao.
Development Team: đánh giá tính khả thi kỹ thuật, viết mã nguồn, chạy unit test, sửa lỗi và triển khai môi trường thử nghiệm.
QA Team: viết kịch bản kiểm thử, thực hiện kiểm thử nội bộ, báo lỗi, xác nhận QA Sign-off.

#### 2. Kết quả đầu ra của quy trình (dựa trên BPMN)
BPMN của quy trình có tổng cộng 3 End Event, tương ứng với 3 kết quả đầu ra chính:
1. Khách hàng không ký hợp đồng
Xảy ra sau bước kiểm tra báo giá sơ bộ.
Kết quả: dự án dừng ngay ở giai đoạn khởi tạo.
2. Dự án hoàn thành thành công
Xảy ra sau khi khách hàng thực hiện UAT sign-off và thanh toán.
Kết quả: phần mềm được triển khai lên môi trường production, bàn giao tài sản và đóng dự án.
3. Kết thúc luồng nghiệp vụ sau thanh toán
Xuất hiện sau bước "Thanh toán".
Kết quả: chốt thanh toán thành công và đóng quy trình chính thức.

#### 3. Đối tượng khách hàng
Doanh nghiệp hoặc cá nhân cần phát triển phần mềm nhưng không có đội ngũ kỹ thuật nội bộ.
Khách hàng đặc biệt quan tâm đến:
tính minh bạch,
kiểm soát phạm vi,
chất lượng phần mềm,
ràng buộc về nghiệm thu và thanh toán.

#### 4. Giá trị mang lại của quy trình
Làm rõ yêu cầu từ đầu để giảm rủi ro scope creep.
Tạo cơ chế kiểm soát tiến độ và chất lượng phần mềm.
Đảm bảo phần mềm được xác nhận bởi khách hàng trước khi bàn giao.
Cung cấp minh bạch trong báo giá, nghiệm thu và thanh toán.
Giảm lãng phí do làm lại công việc và sửa lỗi muộn.

### Hình minh họa
Sơ đồ Stakeholder Map / RACI matrix
Hoặc sơ đồ 3 kết quả đầu ra từ End Event trong BPMN: Hủy hợp đồng, Hoàn thành dự án, Thanh toán thành công.

---

## Slide 3: Chi tiết quy trình

### Tiêu đề
Chi tiết quy trình phát triển phần mềm

### Nội dung chính
Giai đoạn 1: Khởi tạo và báo giá
Khách hàng gửi yêu cầu phát triển phần mềm.
Sales tiếp nhận và gửi thông tin cho BA và Dev.
BA làm rõ yêu cầu, Dev đánh giá khả thi và ước lượng công việc.
Sales tổng hợp báo giá sơ bộ và gửi cho khách hàng.
Nếu khách hàng không đồng ý → kết thúc dự án.
Nếu đồng ý → ký hợp đồng.

Giai đoạn 2: Chốt yêu cầu chi tiết
Khách hàng cung cấp tài liệu đặc tả phần mềm.
BA phân tích nghiệp vụ và viết tài liệu yêu cầu chi tiết.
Khách hàng duyệt hoặc yêu cầu chỉnh sửa.
PM chốt phạm vi công việc và lên kế hoạch triển khai.

Giai đoạn 3: Phát triển và kiểm thử nội bộ
Dev bắt đầu viết code và unit test.
QA viết test case và tiến hành kiểm thử trên môi trường test.
Nếu có lỗi: báo bug → Dev sửa → kiểm thử lại.
Khi không còn lỗi → QA Sign-off.

Giai đoạn 4: Nghiệm thu người dùng (UAT)
PM triển khai phần mềm lên môi trường UAT.
Khách hàng dùng thử và báo lỗi nếu có.
Nếu là bug: Dev sửa lỗi và thử lại.
Nếu là tính năng mới: kích hoạt Change Request.
Nếu đạt yêu cầu: UAT Sign-off.

Giai đoạn 5: Bàn giao và đóng dự án
Dev triển khai phần mềm lên môi trường production.
Bàn giao source code, tài liệu kỹ thuật và tài sản liên quan.
Khách hàng nghiệm thu và thực hiện thanh toán.
Dự án chính thức đóng lại.

### Điều kiện và điểm quyết định quan trọng
Khách hàng có đồng ý báo giá sơ bộ không?
Tài liệu đặc tả có được duyệt không?
Phần mềm có lỗi trong kiểm thử nội bộ không?
Khách hàng có đồng ý UAT sign-off không?
Khách hàng đã thanh toán chưa?

### Hình minh họa
BPMN của quy trình với các lane: Công ty phần mềm và Khách hàng.

---

## Slide 4: Khai phá quy trình

### Tiêu đề
Khai phá quy trình

### Nội dung chính
Phương pháp tiếp cận: dựa trên bằng chứng (Evidence-based)
Nguồn dữ liệu thực tế:
hợp đồng,
tài liệu yêu cầu,
biên bản nghiệm thu,
workshop,
phỏng vấn trực tiếp với người thực thi và khách hàng.

#### Câu hỏi định tính
Câu hỏi có cấu trúc (có lựa chọn):
PM: Anh/chị đánh giá thế nào về tính minh bạch của quy trình xử lý Change Request hiện tại?
A. Rất minh bạch
B. Bình thường
C. Không minh bạch
D. Rất không minh bạch

BA: Khó khăn lớn nhất khi chốt tài liệu đặc tả (SRS) với khách hàng là gì?
A. Khách hàng không nắm rõ nghiệp vụ
B. Yêu cầu thay đổi liên tục
C. Tài liệu chưa rõ ràng
D. Khác

QA: Theo anh/chị, nguyên nhân cốt lõi nào dẫn đến việc phát hiện lỗi trễ ở khâu UAT thay vì ở khâu Test nội bộ?
A. Test case chưa đầy đủ
B. Môi trường UAT không tương đồng
C. Khách hàng chưa có kịch bản rõ ràng
D. Khác

Sales: Khách hàng thường phàn nàn về vấn đề gì nhất ở giai đoạn chốt báo giá sơ bộ?
A. Chi phí cao
B. Phạm vi chưa rõ
C. Thời gian chốt quá lâu
D. Khác

Dev: Môi trường Test và UAT hiện tại có đáp ứng đủ nhu cầu triển khai độc lập của team không?
A. Hoàn toàn đáp ứng
B. Đáp ứng một phần
C. Không đáp ứng
D. Chưa đánh giá

Câu hỏi không có cấu trúc:
Hãy kể về một dự án gần đây mà tình trạng "phình to phạm vi" (scope creep) xảy ra nghiêm trọng nhất. Anh/chị đã xử lý tình huống đó ra sao?
Điều gì làm anh/chị cảm thấy hoang mang hoặc chưa hài lòng nhất trong quá trình nghiệm thu phần mềm?
Giả sử được quyền thay đổi một bước duy nhất trong cách giao tiếp với khách hàng, anh/chị sẽ thay đổi điều gì để chốt scope nhanh hơn?
Kể lại một cuộc tranh luận đáng nhớ nhất giữa anh/chị và team Dev về việc xác định "đây là lỗi hay là tính năng mới".
Khi khách hàng ép tiến độ nhưng ngân sách thấp, anh/chị thường dùng cách gì để vừa ký được hợp đồng vừa bảo vệ team sản xuất?

#### Câu hỏi định lượng
Câu hỏi có cấu trúc (có lựa chọn):
Dev: Đánh giá mức độ rõ ràng và hoàn thiện của tài liệu do BA cung cấp trên thang điểm từ 1 đến 5.
1
2
3
4
5

PM: Trung bình mỗi dự án outsource hiện tại phát sinh bao nhiêu Change Request (CR)?
A. Dưới 3
B. Từ 3-5
C. Trên 5

Khách hàng: Mức độ hài lòng của anh/chị về thời gian phản hồi (SLA) của đội ngũ hỗ trợ trên thang điểm từ 1 đến 10.
A. 1-3
B. 4-6
C. 7-8
D. 9-10

Sales: Thời gian trung bình từ lúc nhận yêu cầu sơ bộ đến khi chốt được báo giá mất khoảng bao nhiêu ngày?
A. <3 ngày
B. 3-7 ngày
C. >7 ngày

QA: Đâu là tỷ lệ phần trăm các lỗi (bugs) bị đẩy ngược từ môi trường UAT về lại môi trường Test?
A. <10%
B. 10-20%
C. >20%

Câu hỏi không có cấu trúc:
Dựa trên kinh nghiệm quản lý, chi phí phát sinh do việc phải làm lại (rework) chiếm khoảng bao nhiêu phần trăm tổng ngân sách dự án?
Anh/chị ước lượng mình bị lãng phí khoảng bao nhiêu giờ mỗi tuần chỉ để tạo test case cho những yêu cầu không được định nghĩa rõ ràng?
Theo sổ tay ghi nhận của anh/chị, khoảng bao nhiêu phần trăm tài liệu yêu cầu (SRS) bị khách hàng yêu cầu viết lại sau lần gửi đầu tiên?
Trong một Sprint kéo dài 2 tuần, anh/chị thường phải trích ra mấy ngày công (man-days) chỉ để tập trung fix bug UAT từ phía khách hàng?
Anh/chị ước tính tỷ lệ chuyển đổi thành công (Conversion rate) từ bước gửi báo giá sơ bộ sang bước chính thức ký hợp đồng là bao nhiêu phần trăm?

---

## Slide 5: Phân tích quy trình - Phân tích giá trị gia tăng

### Tiêu đề
Phân tích giá trị gia tăng (VA, VBA, NVA)

### Nội dung chính
Các hoạt động trong quy trình được phân loại theo 3 nhóm:

VA (Value-Adding): hoạt động trực tiếp tạo ra giá trị mà khách hàng sẵn sàng chi trả
Gửi yêu cầu phát triển phần mềm,
Cung cấp yêu cầu,
Phân tích đặc tả phần mềm,
Viết tài liệu SRS,
Viết code và unit test,
Triển khai lên môi trường UAT,
Kiểm thử dựa trên trường hợp thực tế (UAT),
UAT Sign-off,
Triển khai lên môi trường production,
Bàn giao tài liệu kỹ thuật, source code và asset liên quan,
Nghiệm thu,
Thanh toán.

VBA (Value-Business-Adding): không tạo giá trị trực tiếp cho khách hàng nhưng cần thiết cho hoạt động doanh nghiệp
Gửi phân tích sơ bộ,
Phân tích yêu cầu sơ bộ,
Đánh giá tính khả thi và estimate,
Báo giá sơ bộ,
Chốt phạm vi công việc,
Lập kế hoạch công việc và mốc giao hàng,
Viết test cases,
QA Sign-off,
Phân tích lỗi,
Làm báo giá Change Request,
Quy trình Change Request.

NVA (Non-Value-Adding): hoạt động lãng phí nên giảm tối thiểu
Yêu cầu chỉnh sửa do tài liệu chưa được khách hàng chấp thuận,
Báo bug do sai từ đầu,
Sửa bug (rework),
Thông báo lỗi UAT.

Kết luận
Quy trình cần tối ưu hóa VBA và cắt giảm NVA, trong khi giữ nguyên hoặc nâng cao VA để tăng giá trị thực sự cho khách hàng.

### Hình minh họa
Bảng phân loại VA / VBA / NVA theo 3 cột, kèm ví dụ hoạt động cụ thể theo từng giai đoạn trong quy trình.

---

## Slide 6: Phân tích quy trình - Phân tích sự lãng phí

### Tiêu đề
Phân tích sự lãng phí trong quy trình

### Nội dung chính
Quy trình hiện tại xuất hiện 3 dạng lãng phí đặc thù của ngành phần mềm:

Move (Chuyển giao thông tin)
Luồng tin nhắn, yêu cầu chỉnh sửa và gửi lại tài liệu.
Báo bug từ QA sang Dev thiếu thông tin, dẫn đến phải trao đổi lại nhiều lần.
Nguyên nhân: giao tiếp qua file rời/emails khiến thông tin bị phân mảnh, dễ hiểu sai ý nhau.
Giải pháp: dùng công cụ cộng tác trực tuyến như Figma, Google Docs và chuẩn hóa ticket lỗi.

Hold (Chờ đợi)
Event chờ phản hồi UAT.
Event chờ xác nhận thanh toán.
Nguyên nhân: khách hàng bận công việc, quy trình kế toán và hồ sơ bàn giao rườm rà.
Giải pháp: thỏa thuận SLA UAT và chuẩn bị sẵn hồ sơ nghiệm thu từ trước.

Overdo (Làm quá mức cần thiết)
Làm báo giá Change Request cho các sửa đổi quá nhỏ như đổi màu nút bấm, sửa vài chữ.
Viết test case ở mức độ chi tiết thái quá khi yêu cầu chưa được chốt cứng.
Nguyên nhân: quy trình quá cứng nhắc, yêu cầu chưa đúng scope.
Giải pháp: dành buffer time 10% dự án và áp dụng checklist thay vì viết test case quá sâu ngay từ đầu.

Kết luận
Nguồn lãng phí chính nằm ở chuyển giao thông tin, chờ đợi và làm lại do quy trình không được chuẩn hóa đầu đủ.

### Hình minh họa
Mô hình 3 tầng lãng phí: Move, Hold, Overdo, với ví dụ thực tế trong quy trình phần mềm outsource.

---

## Slide 7: Phân tích quy trình - Phân tích các bên liên quan

### Tiêu đề
Phân tích các bên liên quan và nguyên nhân gốc rễ

### Nội dung chính
Vấn đề trung tâm của quy trình là: khách hàng chậm trễ hoặc từ chối ký UAT Sign-off.
Hậu quả:
dự án bị ách tắc,
đội phát triển không thể triển khai production,
dự án rơi vào trạng thái chờ xác nhận thanh toán,
công ty bị chôn vốn và tăng rủi ro doanh thu.

#### Phân tích theo mô hình 6M (Ishikawa)
Man (Con người)
Khách hàng thiếu chuyên môn IT để tự thực hiện UAT.
Người được giao test không tham gia từ đầu nên không nắm rõ đặc tả phần mềm.

Method (Phương pháp)
Thiếu kịch bản UAT và phương pháp hướng dẫn rõ ràng.
PM không tổ chức buổi hướng dẫn khách hàng cách test và cách báo lỗi.

Machine (Công cụ / hạ tầng)
Môi trường UAT không ổn định, giật lag, dữ liệu rác.
Công cụ báo lỗi (Jira/Trello) quá phức tạp đối với người dùng phi kỹ thuật.

Material (Đầu vào / dữ liệu)
Đặc tả phần mềm viết quá mơ hồ.
Khách hàng không đọc kỹ tài liệu nhưng vẫn chấp thuận, dẫn đến phản ứng tiêu cực khi thấy phần mềm thực tế.

Measurement (Đo lường / tiêu chuẩn)
Không thống nhất Definition of Done với khách hàng từ đầu.
Không có SLA cụ thể cho thời hạn phản hồi UAT.

Milieu (Môi trường / bối cảnh)
Môi trường doanh nghiệp khách hàng đang quá tải.
Người phụ trách dự án thay đổi hoặc nghỉ việc, khiến quyết định ký nghiệm thu bị trì hoãn.

Stakeholder và mối quan tâm
Khách hàng: phần mềm đúng kỳ vọng, ít phát sinh chi phí, dễ kiểm tra.
BA: tài liệu rõ ràng, ít tranh cãi về yêu cầu.
PM: kiểm soát scope, timeline và rủi ro dự án.
Dev: lỗi được mô tả rõ ràng và đúng với thực tế.
QA: test case phù hợp với business flow.
Sales: hạn chế rủi ro thương lượng và scope creep.

### Hình minh họa
Mô hình xương cá 6M với các nhánh nguyên nhân và các bên liên quan tương ứng.

---

## Slide 8: Phân tích quy trình - Phân tích định lượng

### Tiêu đề
Phân tích định lượng và hiệu suất quy trình

### Nội dung chính
Quy trình được mô hình hóa thành 5 khối công việc chính với các biến số thời gian và xác suất làm lại như sau:

Khối 1: Khởi tạo & Ký hợp đồng
T1 = 3 ngày.

Khối 2: Phân tích & Chốt tài liệu
T2 = 5 ngày; xác suất khách hàng yêu cầu sửa lại r1 = 20%.
Thời gian chu kỳ thực tế: CT2 = 5 / (1 - 0.2) = 6.25 ngày.

Khối 3: Thực thi song song
Dev viết code: T3A = 15 ngày.
QA viết test case: T3B = 3 ngày.
Thời gian chu kỳ: CT3 = max(15, 3) = 15 ngày.

Khối 4: Kiểm thử nội bộ
T4 = 2 ngày; xác suất lỗi r2 = 30%.
Thời gian chu kỳ thực tế: CT4 = 2 / (1 - 0.3) ≈ 2.86 ngày.

Khối 5: UAT & Bàn giao
T5 = 4 ngày; xác suất khách hàng bắt lỗi UAT r3 = 20%.
Thời gian chu kỳ thực tế: CT5 = 4 / (1 - 0.2) = 5 ngày.

Tổng thời gian chu kỳ của dự án:
CT = 3 + 6.25 + 15 + 2.86 + 5 = 32.11 ngày.

Hiệu suất thời gian:
Thời gian xử lý lý tưởng nếu không có rework: PT = 29 ngày.
Hiệu suất = 29 / 32.11 ≈ 90.3%.

Kết luận
Nút thắt cổ chai nằm ở các vòng lặp rework (sửa tài liệu, kiểm thử nội bộ, UAT).
Việc chạy song song giữa Dev và QA giúp tối ưu thời gian, nhưng rework vẫn là yếu tố chính làm tăng chu kỳ dự án.

### Hình minh họa
Biểu đồ mô phỏng chu kỳ dự án: T1, CT2, CT3, CT4, CT5 và tổng CT = 32.11 ngày; kèm nhấn mạnh bottleneck ở rework loop.

---

## Gợi ý trình bày
Mỗi slide nên có:
tiêu đề rõ ràng,
3–5 điểm chính,
1 hình minh họa đơn giản,
giọng văn chuyên nghiệp và logic.

Màu sắc phù hợp:
xanh dương: quy trình và hệ thống,
cam: rủi ro / lãng phí,
đỏ: vấn đề cần cải tiến,
xám: dữ liệu phụ trợ.
