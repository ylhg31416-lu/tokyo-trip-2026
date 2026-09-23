import streamlit as st

# 設定網頁標題與寬度
st.set_page_config(page_title="2026 東京近郊散心充電旅", page_icon="🗼", layout="centered")

st.title("🗼 2026 東京近郊散心充電旅")
st.markdown("靈魂需要放空，而風景剛好溫柔 🌸")
st.divider()

# 側邊欄 - 航班與住宿
st.sidebar.header("✈️ 航班與住宿總覽")
st.sidebar.markdown("""
**去程 (12/05)**：CI104 12:35-16:35  
**回程 (12/13)**：CI109 19:30-22:45  
**住宿**：
* 12/05-07：新宿華盛頓新館
* 12/07-08：東橫Inn 河口湖
* 12/08-13：相鐵 FRESA INN 東新宿
""")

# 每日行程資料 (簡化範例)
itinerary = {
    "12/05 (週六) 抵達東京": ["12:35 搭機 ➔ 成田T2", "入住新宿華盛頓新館", "周邊逛街吃晚餐"],
    "12/06 (週日) 市區散心": ["明治神宮、表參道、涉谷、原宿", "傍晚六義園或新宿御苑賞夜楓"],
    "12/07 (週一) 富士回遊➔河口湖": ["搭車前往河口湖", "東橫Inn寄行李、忍野八海", "山中湖遊船、晚餐吃和花"],
    "12/08 (週二) 新倉山淺間神社": ["下吉田站參訪淺間神社", "下午回新宿，入住相鐵FRESA INN"],
    "12/09-12/12 彈性行程": ["箱根一日遊 / 鎌倉一日遊 / 市區血拼 / 迪士尼海洋"],
    "12/13 (週日) OUTLETS➔返台": ["酒酒井 PREMIUM OUTLETS 血拼", "成田T2搭 CI109 返台"]
}

# 選擇日期
selected_day = st.selectbox("📅 請選擇想查看的日期行程：", list(itinerary.keys()))
if selected_day:
    st.subheader(f"📌 {selected_day}")
    for item in itinerary[selected_day]:
        st.markdown(f"- {item}")

st.divider()

# 💬 行程討論區 (Discuss) 功能
st.subheader("💬 行程討論與記事留言板")
st.markdown("大家可以在這裡留言討論想吃什麼、哪裡要調整，或是記錄隨身備忘！")

# 初始化留言紀錄（儲存在 session 中）
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"name": "小幫手", "text": "歡迎大家來到東京自由行討論區！有什麼想修改的可以在下面留言喔～"}
    ]

# 顯示所有留言
for msg in st.session_state.messages:
    st.markdown(f"💬 **{msg['name']}**： {msg['text']}")

# 撰寫新留言的輸入表單
with st.form("comment_form", clear_on_submit=True):
    user_name = st.text_input("您的稱呼", placeholder="例如：同行友人 / 佳瑩")
    user_comment = st.text_input("留言內容", placeholder="例如：這天晚餐我想吃燒肉！")
    submit_button = st.form_submit_button(label="發布留言")
    
    if submit_button and user_comment:
        st.session_state.messages.append({"name": user_name if user_name else "訪客", "text": user_comment})
        st.rerun()
