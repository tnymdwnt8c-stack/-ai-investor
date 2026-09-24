import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="AI Investor V1", page_icon="📈", layout="wide")

st.title("📈 AI Investor V1 — Paper Trading")
st.caption("Paper Trading فقط | رأس مال تجريبي: $1,000 | أسهم وETF أمريكية")

if "cash" not in st.session_state:
    st.session_state.cash = 1000.0
if "trades" not in st.session_state:
    st.session_state.trades = []

st.sidebar.header("إعدادات الاختبار")
capital = st.sidebar.number_input("رأس المال الافتراضي ($)", min_value=100.0, value=1000.0, step=100.0)
symbol = st.sidebar.text_input("الرمز", value="SPY").upper().strip()
action = st.sidebar.selectbox("القرار التجريبي", ["WAIT", "BUY", "SELL"])
qty = st.sidebar.number_input("الكمية", min_value=0.0, value=1.0, step=1.0)
price = st.sidebar.number_input("السعر الافتراضي ($)", min_value=0.01, value=100.0, step=1.0)

if st.sidebar.button("تسجيل القرار"):
    value = qty * price
    st.session_state.trades.append({
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "symbol": symbol,
        "action": action,
        "qty": qty,
        "price": price,
        "value": round(value, 2),
    })

c1, c2, c3 = st.columns(3)
c1.metric("رأس المال الابتدائي", f"${capital:,.2f}")
c2.metric("قرارات مسجلة", len(st.session_state.trades))
c3.metric("وضع التشغيل", "PAPER ONLY")

st.subheader("سجل القرارات والصفقات")
if st.session_state.trades:
    st.dataframe(pd.DataFrame(st.session_state.trades), use_container_width=True)
else:
    st.info("لا توجد قرارات مسجلة بعد.")

st.subheader("منظومة AI Investor V1")
st.write("النسخة الحالية هي واجهة تشغيل آمنة للاختبار الورقي: بيانات → تحليل → فرصة → تقييم → قرار → إدارة مخاطر → تسجيل → قياس أداء.")
st.warning("لا يوجد تنفيذ تداول حقيقي في هذه النسخة.")
