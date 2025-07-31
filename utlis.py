from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.utilities import WikipediaAPIWrapper
key = "sk-a5ed6e0e8bfb445d802b46161fd51ebc"
base = "https://api.deepseek.com/v1"

def generate_script(subject, video_length, creativity, api_key ):
    title_template = ChatPromptTemplate.from_messages(
        [
            ("human",f"请为'{subject}'这个主题的视频像一个吸引人的标题,一个就行了，不要有多余的内容")
        ]
    )
    script_template = ChatPromptTemplate.from_messages(
        [
            ("human",
             """你是一个短视频博主，根据以下标题和相关信息写一份视频脚本
             视频标题：{title},视频时长：{duration}分钟，生成脚本的长度尽量遵循视频时长要求。
             要求开头抓住眼球，中间提供干货内容，结尾有惊喜，脚本格式也请按照【开头，中间，结尾】分隔。
             整体内容的表达形式尽量轻松有趣，吸引年轻人。
             脚本内容可以结合以下维基百科搜索出的信息，但仅作为参考，只结合相关的即可，对不相关的进行忽略：
             ```{wikipedia_search}```""")
        ]
    )

    model = ChatOpenAI(
        api_key=api_key,
        base_url=base,
        model = "deepseek-chat",
        temperature=creativity
    )

    title_chain = title_template | model
    script_chain = script_template | model

    title = title_chain.invoke({"subject": subject}).content

    search = WikipediaAPIWrapper(lang="zh")
    search_result = search.run(subject)


    script = script_chain.invoke({"title":title, "duration":video_length,
                         "wikipedia_search":search_result,
                         }).content

    return search_result, title, script

#print(generate_script("sora模型",1, 0.7, key))





