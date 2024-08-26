import streamlit as st
import base64

def main():
    st.set_page_config(page_title="네이버 스타일 포털", layout="wide")

    # Custom CSS
    st.markdown("""
    <style>
    .stApp {
        background-color: #f5f6f7;
        font-family: -apple-system, BlinkMacSystemFont, "Malgun Gothic", "맑은 고딕", helvetica, "Apple SD Gothic Neo", sans-serif;
    }
    .header {
        background-color: #19ce60;
        padding: 20px;
        margin-bottom: 20px;
    }
    .content-box {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    h2 {
        color: #03c75a;
        border-bottom: 2px solid #e6e6e6;
        padding-bottom: 10px;
        margin-bottom: 15px;
    }
    a {
        color: #333;
        text-decoration: none;
    }
    a:hover {
        color: #03c75a;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown('<div class="header">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,3,1])
    with col2:
        search_term = st.text_input("", placeholder="검색어를 입력해 주세요.")
        if st.button("검색"):
            st.write(f"'{search_term}' 검색 결과")
    st.markdown('</div>', unsafe_allow_html=True)

    # Content
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.markdown("<h2>뉴스</h2>", unsafe_allow_html=True)
        st.markdown("""
        - [코로나19 백신 접종 현황 업데이트](/news/article?id=1)
        - [국내 IT 기업, 인공지능 기술 개발 박차](/news/article?id=2)
        - [올해의 영화상 후보작 발표](/news/article?id=3)
        """)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.markdown("<h2>스포츠</h2>", unsafe_allow_html=True)
        st.markdown("""
        - [프로야구 개막, 팬들의 기대감 고조](/sports/article?id=1)
        - [올림픽 메달리스트 은퇴 선언](/sports/article?id=2)
        - [국가대표 축구팀 새 감독 선임](/sports/article?id=3)
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.markdown("<h2>실시간 검색어</h2>", unsafe_allow_html=True)
        st.markdown("""
        1. [날씨](/search?q=날씨)
        2. [주식](/search?q=주식)
        3. [부동산](/search?q=부동산)
        4. [월드컵](/search?q=월드컵)
        5. [건강식품](/search?q=건강식품)
        """)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.markdown("<h2>엔터테인먼트</h2>", unsafe_allow_html=True)
        st.markdown("""
        - [인기 아이돌 그룹 컴백 소식](/entertainment/article?id=1)
        - [국내 드라마, 해외 스트리밍 서비스 진출](/entertainment/article?id=2)
        - [유명 배우 부부, 둘째 임신 소식 전해](/entertainment/article?id=3)
        """)
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()