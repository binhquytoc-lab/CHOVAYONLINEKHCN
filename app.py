import streamlit as st

# Cấu hình trang
st.set_page_config(
    page_title="APP CHO VAY ONLINE KHÁCH HÀNG CÁ NHÂN_TS. VŨ ĐỨC BÌNH",
    page_icon="🏦",
    layout="centered"
)

# Tiêu đề
st.title("🏦 APP CHO VAY ONLINE KHÁCH HÀNG CÁ NHÂN_TS. VŨ ĐỨC BÌNH")

st.write("Nhập các thông tin của khách hàng để đánh giá khoản vay.")

# Nhập dữ liệu
STV = st.number_input(
    "Số tiền muốn vay (triệu đồng)",
    min_value=0.0,
    step=1.0
)

TGV = st.number_input(
    "Thời gian vay (năm)",
    min_value=1.0,
    step=1.0
)

LSV = st.number_input(
    "Lãi suất cho vay (dạng thập phân, ví dụ 0.12 = 12%)",
    min_value=0.0,
    step=0.01,
    format="%.4f"
)

TN = st.number_input(
    "Thu nhập hàng tháng (triệu đồng/tháng)",
    min_value=0.0,
    step=1.0
)

SNTGD = st.number_input(
    "Số người trong gia đình",
    min_value=1,
    step=1
)

PTMC = st.number_input(
    "Số tiền phải trả cho khoản vay cũ (triệu đồng/tháng)",
    min_value=0.0,
    step=1.0
)

GTTSDB = st.number_input(
    "Giá trị tài sản đảm bảo (triệu đồng)",
    min_value=0.0,
    step=1.0
)

STKH = st.number_input(
    "Tuổi của khách hàng",
    min_value=18,
    max_value=100,
    step=1
)

# Chi phí sinh hoạt mặc định
CPSH = 5

# Nút tính toán
if st.button("Đánh giá khoản vay"):

    if TN - SNTGD * CPSH <= 0:
        st.error("Thu nhập sau khi trừ chi phí sinh hoạt không hợp lệ.")
    elif GTTSDB == 0:
        st.error("Giá trị tài sản đảm bảo phải lớn hơn 0.")
    else:
        # Tính toán
        PTMM = (STV / (TGV * 12)) + (STV * (LSV / 12))

        DTI = (PTMC + PTMM) / (TN - SNTGD * CPSH)

        LTV = STV / GTTSDB

        # Hiển thị kết quả
        st.subheader("📊 Kết quả đánh giá")

        st.metric(
            label="DTI",
            value=f"{DTI*100:.2f}%"
        )

        st.metric(
            label="LTV",
            value=f"{LTV*100:.2f}%"
        )

        # Đưa ra quyết định
        if DTI <= 0.7 and LTV <= 0.7 and 18 <= STKH <= 70:
            st.success("✅ ĐƯỢC CHO VAY")
        else:
            st.error("❌ KHÔNG ĐƯỢC CHO VAY")

        # Giải thích chi tiết
        st.write("### Điều kiện xét duyệt")
        st.write(f"- DTI ≤ 70%: {'✅' if DTI <= 0.7 else '❌'}")
        st.write(f"- LTV ≤ 70%: {'✅' if LTV <= 0.7 else '❌'}")
        st.write(f"- Tuổi từ 18 đến 70: {'✅' if 18 <= STKH <= 70 else '❌'}")
