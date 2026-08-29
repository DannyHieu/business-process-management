Quy trình phát triển phần mềm
1. Các tác nhân tham gia
Quy trình có sự tham gia của hai nhóm tác nhân chính, đại diện cho đơn vị đặt hàng và đơn vị gia công:
Khách hàng: Là cá nhân hoặc đại diện doanh nghiệp có nhu cầu xây dựng phần mềm. Khách hàng đóng vai trò cung cấp yêu cầu bài toán, xét duyệt tài liệu, trực tiếp tham gia kiểm thử nghiệm thu và tiến hành thanh toán chi phí.
Công ty phần mềm: Là đơn vị chịu trách nhiệm gia công, bao gồm 5 bộ phận chuyên môn:
Sales (Kinh doanh): Bộ phận tiền tuyến, chịu trách nhiệm tiếp nhận yêu cầu ban đầu, gửi báo giá và tiến hành ký kết hợp đồng.
Business Analysis (Phân tích nghiệp vụ): Là cầu nối để phân tích đặc tả phần mềm từ khách hàng và viết tài liệu yêu cầu chi tiết.
Project Manager (Quản lý dự án): Người điều phối chung, chịu trách nhiệm lên kế hoạch, chốt phạm vi công việc, xử lý các báo giá thay đổi yêu cầu và quản lý quá trình bàn giao.
Development Team (Đội Lập trình): Chịu trách nhiệm đánh giá tính khả thi kỹ thuật, viết mã nguồn, kiểm tra lỗi cục bộ (unit test), sửa lỗi và đưa phần mềm lên các môi trường sử dụng.
QA Team (Đội Đảm bảo chất lượng): Đảm nhiệm việc viết kịch bản kiểm thử, trực tiếp kiểm tra phần mềm và báo lỗi cho đội lập trình.
2. Diễn giải quy trình nghiệp vụ
Quy trình được thực hiện qua các giai đoạn nối tiếp nhau một cách chặt chẽ:

Giai đoạn Khởi tạo và Báo giá: Khách hàng bắt đầu bằng việc gửi yêu cầu phát triển phần mềm. Bộ phận Sales tiếp nhận và gửi thông tin đi phân tích sơ bộ. Tại bước này, hai công việc được tiến hành đồng thời: bộ phận Phân tích nghiệp vụ tiến hành làm rõ yêu cầu, trong khi Đội Lập trình đánh giá tính khả thi và ước lượng khối lượng công việc. Sau khi có kết quả từ hai bộ phận trên, Sales sẽ tổng hợp làm báo giá sơ bộ gửi cho khách hàng. Khách hàng kiểm tra báo giá; nếu không đồng ý, quy trình sẽ kết thúc. Nếu đồng ý, hai bên tiến hành ký hợp đồng và phía công ty phần mềm sẽ chuyển sang bước phân tích chi tiết.
Giai đoạn Chốt yêu cầu chi tiết: Khách hàng cung cấp các tài liệu đặc tả phần mềm. Dựa vào đó, bộ phận Phân tích nghiệp vụ tiến hành phân tích và viết tài liệu yêu cầu hệ thống. Tài liệu này được gửi lại cho khách hàng để chờ duyệt. Trong trường hợp khách hàng chưa ưng ý và yêu cầu chỉnh sửa, bộ phận Phân tích nghiệp vụ sẽ cập nhật lại tài liệu cho đến khi được duyệt. Khi nhận được thông báo tài liệu đã duyệt, Quản lý dự án sẽ chốt phạm vi công việc và lập kế hoạch chi tiết cùng các mốc thời gian bàn giao.
Giai đoạn Phát triển và Kiểm thử nội bộ: Dựa trên kế hoạch đã chốt, Đội Lập trình bắt đầu viết mã nguồn và kiểm tra nội bộ. Đồng thời, đội QA cũng tiến hành viết các kịch bản kiểm thử. Sau khi việc lập trình hoàn tất, phần mềm được đưa lên môi trường kiểm thử. Đội QA tiến hành kiểm tra; nếu phát hiện lỗi, họ sẽ báo lại để Đội Lập trình sửa chữa và cập nhật lại phần mềm. Quá trình này lặp lại cho đến khi phần mềm không còn lỗi, lúc này đội QA sẽ xác nhận hoàn tất khâu kiểm thử nội bộ.
Giai đoạn Nghiệm thu người dùng (UAT): Quản lý dự án tiếp nhận xác nhận từ đội QA và đưa phần mềm lên môi trường nghiệm thu thực tế. Khách hàng nhận được thông báo và bắt đầu dùng thử phần mềm. Nếu quá trình dùng thử phát sinh vấn đề, khách hàng sẽ thông báo lỗi lại cho phía công ty. Đội Lập trình sẽ phân tích phản hồi này: nếu là lỗi kỹ thuật, họ sẽ tiến hành sửa lỗi; nếu khách hàng muốn thêm tính năng mới so với hợp đồng ban đầu, Quản lý dự án sẽ tiến hành làm báo giá thay đổi yêu cầu và thực hiện quy trình bổ sung. Khi phần mềm đã đáp ứng đúng kỳ vọng, khách hàng sẽ xác nhận nghiệm thu thành công.
Giai đoạn Bàn giao và Đóng dự án: Nhận được xác nhận nghiệm thu, Đội Lập trình đưa hệ thống lên môi trường hoạt động chính thức. Quản lý dự án tiến hành bàn giao mã nguồn, tài liệu kỹ thuật và gửi thông báo nghiệm thu cho khách hàng. Khách hàng chính thức ký nghiệm thu và thực hiện thanh toán. Về phía công ty phần mềm, họ sẽ chờ đến khi xác nhận được khoản thanh toán này rồi mới chính thức tuyên bố kết thúc dự án.

3. Đối tượng khách hàng
Quy trình này hướng tới nhóm khách hàng doanh nghiệp hoặc cá nhân cần gia công phần mềm nhưng không có sẵn đội ngũ kỹ thuật nội bộ.
Phù hợp với các khách hàng yêu cầu tính minh bạch cao về tài chính và phạm vi công việc, muốn được trực tiếp kiểm duyệt tài liệu và tham gia vào khâu kiểm thử thực tế trước khi thanh toán.
 
4. Các kết quả có thể xảy ra của quy trình
4.1 Hoàn thành quy trình thành công
Sản phẩm phần mềm hoàn chỉnh: Phần mềm đạt yêu cầu, được khách hàng xác nhận nghiệm thu (UAT Sign-off) và được triển khai thành công lên môi trường hoạt động chính thức (Production).
Gói tài sản bàn giao: Toàn bộ mã nguồn (source code), tài liệu kỹ thuật và các tài sản liên quan được bàn giao trọn vẹn cho khách hàng.
Hồ sơ nghiệm thu và Thanh toán: Khách hàng tiếp nhận yêu cầu nghiệm thu, chính thức ký nghiệm thu và hoàn tất việc thanh toán chi phí. Sự kiện nhận thanh toán đánh dấu kết quả dự án được đóng lại thành công.
4.2 Khách hàng từ chối báo giá ban đầu (Hủy dự án sớm)
Tình huống: Sau khi Sales gửi báo giá sơ bộ, khách hàng kiểm tra và cảm thấy chi phí hoặc phương án không phù hợp.
Kết quả: Khách hàng quyết định không ký hợp đồng. Quy trình lập tức kết thúc ngay tại giai đoạn khởi tạo mà không tiêu tốn thêm nguồn lực sản xuất của công ty phần mềm.
4.5 Khách hàng phát hiện vấn đề khi nghiệm thu thực tế - UAT (Từ chối nghiệm thu)
Đây là kịch bản ngoại lệ phức tạp nhất. Khách hàng dùng thử phần mềm và thấy không đúng kỳ vọng nên gửi thông báo lỗi UAT và từ chối ký nghiệm thu. Đội lập trình phải phân tích lỗi này và dẫn đến 2 kết quả xử lý khác nhau:
Kết quả 4a (Nếu xác định là lỗi kỹ thuật - Bug): Khách hàng đã báo đúng lỗi. Đội Lập trình phải chịu trách nhiệm sửa lỗi này và cập nhật lại lên môi trường UAT để khách hàng thử lại. Quá trình bàn giao bị chậm trễ.
Kết quả 4b (Nếu xác định là yêu cầu tính năng mới - Change Request): Khách hàng muốn thêm những thứ không có trong tài liệu đã chốt từ đầu. Quản lý dự án sẽ can thiệp để làm một báo giá mới (Báo giá Change Request) và kích hoạt một quy trình rẽ nhánh bổ sung. Kết quả là khách hàng phải chờ lâu hơn và phát sinh thêm chi phí so với ngân sách ban đầu.
4.6 Khách hàng chậm thanh toán (Dự án bị treo)
Tình huống: Dù khách hàng đã ký nghiệm thu thành công và công ty phần mềm đã bàn giao toàn bộ tài liệu, mã nguồn, nhưng tiền vẫn chưa được chuyển.
Kết quả: Quy trình của công ty phần mềm rơi vào trạng thái "Chờ xác nhận thanh toán". Quản lý dự án không thể chính thức đóng dự án và ghi nhận doanh thu cho đến khi nghĩa vụ tài chính từ phía khách hàng được hoàn tất.
