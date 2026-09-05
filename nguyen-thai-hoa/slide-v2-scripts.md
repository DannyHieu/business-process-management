# Script thuyết trình Slide v2 (7 phút)

## Slide 1: Tổng quan quy trình phát triển phần mềm

"Chúng ta sẽ nhìn vào quy trình phát triển phần mềm theo mô hình outsource. Quy trình này diễn ra từ khi khách hàng gửi yêu cầu cho đến khi phần mềm được nghiệm thu, bàn giao và thanh toán. Cấu trúc quy trình gồm 5 giai đoạn chính: khởi tạo và báo giá, chốt yêu cầu chi tiết, phát triển và kiểm thử nội bộ, nghiệm thu người dùng, và bàn giao đóng dự án. Mục tiêu của quy trình là đảm bảo phạm vi công việc rõ ràng, tiến độ được kiểm soát, chất lượng phần mềm đạt yêu cầu, và sự đồng thuận giữa khách hàng và công ty."

"Về mặt nghiệp vụ, quy trình có các điểm quyết định rất quan trọng. Đầu tiên là khách hàng có đồng ý báo giá hay không. Tiếp đó là tài liệu đặc tả có được duyệt hay cần chỉnh sửa. Sau đó, phần mềm có lỗi trong kiểm thử hay không. Nếu UAT đạt yêu cầu, dự án sẽ đi đến ký nghiệm thu và thanh toán; nếu không, sẽ phát sinh Change Request hoặc đòi hỏi sửa lỗi."

---

## Slide 2: Tác nhân, vai trò, kết quả đầu ra và giá trị mang lại

"Quy trình này có sự tham gia của nhiều tác nhân với vai trò khác nhau. Khách hàng là người đặt hàng và là chủ sở hữu của yêu cầu. Sales tiếp nhận yêu cầu và báo giá sơ bộ. BA làm rõ nghiệp vụ và viết tài liệu đặc tả. PM quản lý tiến độ, phạm vi và thay đổi yêu cầu. Development Team chịu trách nhiệm viết mã và xử lý lỗi. QA Team kiểm thử và xác nhận chất lượng."

"Về kết quả đầu ra, mô hình BPMN của quy trình cho thấy có tổng cộng 3 End Event. Thứ nhất, dự án kết thúc sớm khi khách hàng không ký hợp đồng sau khi nhận báo giá sơ bộ. Thứ hai, dự án hoàn thành thành công khi phần mềm được nghiệm thu, bàn giao và thanh toán. Thứ ba, quy trình kết thúc sau khi thanh toán thành công. Đây là các trạng thái kết thúc thực tế của quy trình, cho thấy quy trình không chỉ là một chuỗi phát triển kỹ thuật, mà còn là chuỗi thực thi thương mại và pháp lý rõ ràng."

"Về giá trị mang lại, quy trình giúp làm rõ yêu cầu từ đầu, kiểm soát tiến độ và chất lượng, tạo tính minh bạch giữa hai bên, và giảm lãng phí do làm lại công việc. Nói cách khác, quy trình này không chỉ tạo ra phần mềm, mà còn tạo ra sự tin cậy và kiểm soát cho cả khách hàng lẫn công ty."

---

## Slide 3: Chi tiết quy trình

"Để hiểu rõ hơn, hãy đi vào từng giai đoạn. Giai đoạn đầu tiên là khởi tạo và báo giá. Khách hàng gửi yêu cầu, Sales tiếp nhận và gửi cho BA và Dev. BA làm rõ yêu cầu, Dev đánh giá tính khả thi và ước lượng khối lượng. Sau đó, Sales tổng hợp báo giá sơ bộ. Nếu khách hàng đồng ý, quy trình đi tiếp đến ký hợp đồng."

"Giai đoạn thứ hai là chốt yêu cầu chi tiết. Khách hàng cung cấp tài liệu đặc tả phần mềm. BA phân tích nghiệp vụ và viết SRS. Nếu khách hàng không đồng ý, tài liệu sẽ được điều chỉnh lại cho đến khi được duyệt. PM sẽ chốt phạm vi và lập kế hoạch triển khai."

"Giai đoạn thứ ba là phát triển và kiểm thử nội bộ. Dev viết code và unit test, QA viết test case và thực hiện kiểm thử trên môi trường test. Nếu phát hiện lỗi, hệ thống sẽ thực hiện báo bug, Dev sửa lỗi và kiểm thử lại cho đến khi đạt tiêu chuẩn nội bộ."

"Giai đoạn thứ tư là UAT. PM triển khai phần mềm lên môi trường UAT, khách hàng dùng thử. Nếu phát hiện lỗi, sẽ phân định đây là bug hay là tính năng mới. Nếu là bug, Dev phải sửa; nếu là tính năng mới, dự án cần xử lý Change Request. Khi khách hàng chấp nhận, UAT sign-off sẽ được thực hiện."

"Giai đoạn cuối là bàn giao và đóng dự án. Phần mềm được triển khai lên production, bàn giao source code, tài liệu kỹ thuật và tài sản liên quan. Khi khách hàng ký nghiệm thu và thanh toán, dự án chính thức đóng lại. Đây là giai đoạn khép kín của quy trình, đồng thời là nơi xác nhận giá trị thực sự của dự án." 

---

## Slide 4: Khai phá quy trình

"Quy trình này được xây dựng dựa trên phương pháp khai phá quy trình theo hướng evidence-based. Nói đơn giản là chúng ta dựa trên bằng chứng thực tế: hợp đồng, tài liệu yêu cầu, biên bản nghiệm thu, workshop và các cuộc phỏng vấn với người trực tiếp làm việc. Mục tiêu của phương pháp này là hiểu đúng tình trạng thực tế, không chỉ suy đoán."

"Chúng ta sử dụng cả câu hỏi định tính và định lượng. Câu hỏi định tính giúp khám phá nguyên nhân, cảm nhận và kinh nghiệm thực tế của từng vai trò như PM, BA, QA, Dev, Sales và khách hàng. Ví dụ, chúng ta hỏi về tính minh bạch của Change Request, sự khó khăn trong việc chốt SRS, yếu tố dẫn đến lỗi bị phát hiện muộn ở UAT, hoặc mức độ đáp ứng của môi trường test và UAT."

"Song song đó là các câu hỏi định lượng, dùng để đo lường mức độ, tỷ lệ và tần suất. Ví dụ như mức độ rõ ràng của tài liệu BA, số lượng Change Request trung bình mỗi dự án, thời gian chốt báo giá, tỷ lệ lỗi lặp lại ở UAT, hoặc thời gian mất vì rework. Những câu hỏi này giúp chúng ta chuyển từ cảm nhận chủ quan sang phân tích khách quan."

---

## Slide 5: Phân tích quy trình - Phân tích giá trị gia tăng

"Trong phần phân tích giá trị gia tăng, chúng ta phân loại các hoạt động trong quy trình thành ba nhóm: VA, VBA và NVA. VA là các hoạt động trực tiếp tạo ra giá trị mà khách hàng sẵn sàng chi trả. Ví dụ như cung cấp yêu cầu, phân tích đặc tả phần mềm, viết tài liệu SRS, viết code và unit test, thực hiện UAT, triển khai production, bàn giao sản phẩm và thanh toán."

"VBA là những hoạt động cần thiết cho doanh nghiệp nhưng không trực tiếp tạo giá trị cho khách hàng như báo giá sơ bộ, đánh giá tính khả thi, chốt phạm vi, QA Sign-off, làm báo giá Change Request, hay quy trình xử lý thay đổi yêu cầu. Đây là những hoạt động bắt buộc để doanh nghiệp vận hành nhưng không phải là giá trị trực tiếp mà khách hàng nhìn thấy."

"NVA là các hoạt động lãng phí cần giảm thiểu như sửa lại tài liệu do khách hàng không chấp thuận, báo bug do sai từ đầu, và sửa bug vì rework. Đây chính là nơi mà quy trình cần tối ưu hóa, vì nếu không kiểm soát tốt, dự án sẽ tốn chi phí mà không tạo ra giá trị thực sự."

---

## Slide 6: Phân tích quy trình - Phân tích sự lãng phí

"Phần tiếp theo là phân tích lãng phí theo nguyên tắc Lean. Chúng ta nhận thấy có ba dạng lãng phí chính: Move, Hold và Overdo. Move là lãng phí do chuyển giao thông tin không rõ ràng, như yêu cầu chỉnh sửa gửi qua file rời hoặc báo bug từ QA sang Dev thiếu thông tin. Điều này dẫn đến việc phải trao đổi lại nhiều lần, gây tiêu tốn thời gian."

"Hold là lãng phí do chờ đợi. Ví dụ như chờ phản hồi UAT từ khách hàng hoặc chờ xác nhận thanh toán. Khi dự án bị treo, các team không thể tiến hành bước tiếp theo, gây kẹt tiến độ và tăng chi phí. Overdo là lãng phí do làm quá mức cần thiết, như viết báo giá Change Request cho những thay đổi quá nhỏ hoặc viết test case quá chi tiết trước khi yêu cầu đã chốt."

"Giải pháp của chúng ta là chuẩn hóa giao tiếp, tạo template báo lỗi, dựng SLA cho UAT, và bỏ bớt các bước không cần thiết. Kết luận là quy trình cần giảm Move, Hold và Overdo để tăng hiệu quả và giảm rework." 

---

## Slide 7: Phân tích quy trình - Phân tích các bên liên quan

"Phần thứ ba là phân tích các bên liên quan. Vấn đề trung tâm của quy trình là khách hàng chậm trễ hoặc từ chối ký UAT Sign-off. Đây là điểm rủi ro nhất vì nó làm ách tắc cả chuỗi dự án: không triển khai production, không kết thúc dự án, và làm chậm thanh toán."

"Để hiểu rõ nguyên nhân, chúng ta dùng mô hình xương cá 6M. Man là do khách hàng thiếu kỹ năng UAT hoặc người test không tham gia từ đầu. Method là do thiếu kịch bản UAT, thiếu hướng dẫn cách dùng và cách báo lỗi. Machine là do môi trường UAT không ổn định hoặc công cụ báo lỗi quá phức tạp. Material là do đặc tả phần mềm mơ hồ. Measurement là do thiếu tiêu chí Definition of Done và SLA. Milieu là do môi trường kinh doanh khách hàng quá tải hoặc người phụ trách thay đổi."

"Như vậy, rủi ro không nằm ở một nguyên nhân đơn lẻ, mà là sự kết hợp của nhiều yếu tố từ con người, phương pháp, công cụ, dữ liệu và môi trường. Chính vì vậy, giải pháp cần đồng bộ ở cả phía doanh nghiệp và phía khách hàng để giảm rủi ro về UAT và scope creep."

---

## Slide 8: Phân tích quy trình - Phân tích định lượng

"Cuối cùng là phân tích định lượng. Theo báo cáo, quy trình được mô hình hóa thành 5 khối công việc chính: khởi tạo và ký hợp đồng, phân tích và chốt tài liệu, thực thi song song, kiểm thử nội bộ, và UAT & bàn giao. Mỗi khối có thời gian và xác suất làm lại khác nhau."

"Khối 2 có thời gian chu kỳ thực tế là 6,25 ngày do xác suất rework 20%. Khối 4 có thời gian chu kỳ thực tế là 2,86 ngày do tỷ lệ lỗi nội bộ 30%. Khối 5 có thời gian chu kỳ thực tế 5 ngày do xác suất bắt lỗi ở UAT là 20%. Tổng thời gian chu kỳ của toàn bộ dự án là 32,11 ngày trong khi thời gian xử lý lý tưởng chỉ là 29 ngày."

"Điều này cho thấy hiệu suất thời gian là khoảng 90,3%, chứng tỏ rằng các vòng lặp rework và lỗi đang làm kéo dài dự án. Nút thắt cổ chai nằm ở các khâu rework, đặc biệt ở việc sửa tài liệu, test nội bộ và UAT. Vì vậy, mục tiêu cải tiến là giảm rework, chọn đúng scope từ đầu, và tăng tính rõ ràng trong giao tiếp và chốt yêu cầu."

"Kết luận chung là quy trình phát triển phần mềm hiện tại đã có cấu trúc rõ ràng nhưng còn nhiều rủi ro ở chốt scope, UAT và rework. Nếu giảm được các yếu tố lãng phí và định nghĩa rõ hơn tiêu chí hoàn thành, dự án sẽ ít bị trễ, ít phát sinh chi phí, và hiệu quả hơn rất nhiều."
