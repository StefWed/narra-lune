import streamlit as st

st.header("Welcome to ReadingQuest!")

st.write("""
**Welcome to ReadingQuest – your playful guide through the world of books!**
ReadingQuest is like a digital treasure hunt for your next favorite book. It’s part game, part
book-matching companion, like a personal librarian. Whether you read one book a year or devour a stack a week, 
it helps you discover books in fun, creative ways. 

---

### What can you do?

- 🎲 **Generate a Random Reading Bingo Card**  
  Print it, share it, or use it as your yearly reading map.

- 💬 **Chat with our Book Matcher Bot**  
  Tell it what kind of challenge you're taking on - and it’ll try to find a match using real book blurbs.

---

Ready to begin?
""")

st.page_link("app_pages/page_2_reading_bingo.py", label="➡️ Start with a Bingo Card", icon="🎲")
st.page_link("app_pages/page_3_challenge_matching.py", label="➡️ Find a Book for a Prompt", icon="🔍")