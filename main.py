import streamlit as st
from utlis import generate_script


st.title("🎬视频脚本生成器")

with st.sidebar:
    key = st.text_input("请输入你的key",type="password")
    st.markdown("[了解获取key的详情](https://platform.deepseek.com/api_keys)")
subject = st.text_input("请输入视频的主题")
video_length = st.number_input("请输入视频的大致时长（单位：分钟）",value = 1.0,min_value=0.1,step = 0.1)
creativity = st.slider("请输入视频脚本的创造力（数字小说明更严谨，数字大说明更多样）",value = 0.2,min_value=0.0,max_value=1.0,step = 0.1)
submit = st.button("生成脚本")

if submit and not key:
    st.info("请输入你的key")
    st.stop()
if submit and not subject:
    st.info("请输入视频主题")
    st.stop()
if submit:
    with st.spinner(("AI正在思考中，请稍等...")):
        search_result, title, script = generate_script(subject, video_length, creativity, key)
    st.success("视频脚本已生成！")
    st.subheader("🔥标题：")
    st.write(title)
    st.subheader("📜视频脚本：")
    st.write(script)
    with st.expander("网络搜索结果：👀"):
        st.info(search_result)