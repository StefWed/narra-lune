import streamlit as st

intro_page = st.Page("../pages/page_1_intro.py", title="Introduction to ReadingQuest")
reading_bingo = st.Page("../pages/page_2_reading_bingo.py", title="Reading Bingo")
challenge_matching = st.Page("../pages/page_3_challenge_matching.py", title="Challenge Matching")

pg = st.navigation([intro_page, reading_bingo, challenge_matching])
st.set_page_config(page_title="ReadingQuest")
pg.run()