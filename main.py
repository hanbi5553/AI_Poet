import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv


#load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("AI Poet — 인공지능 시 생성기")
st.write("주제를 입력하면 OpenAI로 시를 만들어 드립니다.")

topic = st.text_input("시의 주제를 입력하세요!", "")

if st.button("시 생성"):
    if topic.strip() == "":
        st.warning("주제를 입력해주세요!")
    else:
        with st.spinner("시를 생성하는 중입니다..."):
            response = client.responses.create(
                model="gpt-4.1-mini",
                input=[
                    {"role": "system", "content": "너는 한국어 시를 잘 쓰는 시인이다."},
                    {"role": "user", "content": f"'{topic}'에 대한 시 한 편을 써줘."}
                ],
                max_output_tokens=300
            )

            poem = response.output_text
            st.success("시가 완성되었습니다!")
            st.write(poem)


