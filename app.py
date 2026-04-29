import streamlit as st
import time

# --- 網頁配置 ---
st.set_page_config(page_title="泰語 AI 發音教練", layout="centered")

# --- 自定義 CSS (美化介面) ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .main-title { color: #1E3A8A; text-align: center; font-weight: bold; }
    .feedback-box { padding: 15px; border-radius: 10px; background-color: #ffffff; border-left: 5px solid #3B82F6; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🇹🇭 泰語發音 AI 輔助訓練系統</h1>", unsafe_allow_html=True)
st.write("本研究旨在探討 AI 即時反饋對泰語相似音學習之影響。")

# --- 側邊欄：導覽 ---
page = st.sidebar.radio("導覽選單", ["練習中心", "心理感受調查 (問卷)"])

# --- 頁面 1：練習中心 ---
if page == "練習中心":
    st.header("🎯 本週主題：送氣音與不送氣音")
    st.info("請分辨 ป (p) 與 พ (ph) 的差異。")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("不送氣音 ป")
        st.code("ปลา (Pla) - 魚", language="")
        st.write("💡 要領：嘴唇緊閉憋氣後彈開。")
        # st.audio("path_to_standard_p.mp3") # 可自行放置音檔網址

    with col2:
        st.subheader("送氣音 พ")
        st.code("พลา (Phla) - 人名/地名", language="")
        st.write("💡 要領：發音時有明顯氣流噴出。")
        # st.audio("path_to_standard_ph.mp3")

    st.divider()
    
    st.subheader("🎙️ 開始練習")
    target_word = st.selectbox("請選擇要練習的單字", ["ปลา (Pla)", "พลา (Phla)"])
    
    # 錄音元件
    audio_data = st.audio_input(f"請按下麥克風並唸出：{target_word}")

    if audio_data:
        st.success("錄音已接收，正在進行 AI 聲學比對...")
        with st.spinner("AI 分析中..."):
            time.sleep(2.5) # 模擬運算時間
        
        # 這裡未來可整合 API，目前以 Rule-based 邏輯模擬反饋
        st.markdown("<div class='feedback-box'>", unsafe_allow_html=True)
        st.subheader("🤖 AI 反饋報告")
        
        if "ปลา" in target_word:
            st.warning("⚠️ **偏誤警告**：偵測到氣流過強。")
            st.write("您的發音目前聽起來接近 **พลา (Phla)**。請試著在發音時，於嘴唇前放一張衛生紙，確保衛生紙不會劇烈晃動。")
        else:
            st.write("✨ **表現優異**：您的送氣特徵非常清晰。")
        st.markdown("</div>", unsafe_allow_html=True)

# --- 頁面 2：心理感受調查 ---
elif page == "心理感受調查 (問卷)":
    st.header("📋 練習體驗回饋")
    st.write("請根據剛才的練習過程，勾選最符合您的感受。")

    with st.form("survey_form"):
        st.subheader("1. 認知負荷 (Cognitive Load)")
        load_1 = st.select_slider("剛才的發音練習對我來說在心智上是非常費力的：", options=[1, 2, 3, 4, 5, 6, 7], value=4)
        load_2 = st.select_slider("AI 給予的反饋訊息非常容易理解：", options=[1, 2, 3, 4, 5, 6, 7], value=4)

        st.subheader("2. 學習焦慮 (Learning Anxiety)")
        anx_1 = st.select_slider("面對這個 AI 工具練習，我不會擔心發音錯誤被嘲笑：", options=[1, 2, 3, 4, 5, 6, 7], value=4)
        anx_2 = st.select_slider("與真人老師相比，我更敢大聲練習：", options=[1, 2, 3, 4, 5, 6, 7], value=4)

        st.subheader("3. 系統可用性 (Usability)")
        use_1 = st.radio("我願意在未來的泰語課中使用這個系統練習：", ["強烈不同意", "不同意", "普通", "同意", "強烈同意"])
        
        submitted = st.form_submit_button("提交數據")
        if submitted:
            st.balloons()
            st.success("感謝您的參與！您的數據已模擬記錄成功。")
            # 實務上這裡可串接 Google Sheets 或 Database 儲存數據
