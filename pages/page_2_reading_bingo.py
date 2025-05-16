import streamlit as st
from modules.bingo_generator import generate_word_bingo_html

# Sample word list
words = [
    "A Book With Your Favorite Color",
    "Magical Realism",
    "A Book on Display at the Library",
    "Murder Mystery",
    "Sherlock Holmes Inspired",
    "Book With Ambiguous Ending",
    "Current #1 at OrellFuessli",
    "City or Country Name in the Title",
    "Historical Fiction",
    "The Main Character Has a Pet",
    "A Book Set in the Future",
    "Inspired by Folk Tales",
    "Book You Saw Someone Reading",
    "Black And White Cover",
    "A Book That Won An Award",
    "Dystopian Fiction",
    "A Book That Your Friend Suggests",
    "A Book Set Before 17th Century",
    "A Book That Was Banned in Your Country",
    "A Book by an African Author",
    "Author With X, Y or Z in Their Name",
    "The Word 'Game' in the Title",
    "Includes an Exotic Animal",
    "A Family Saga"
]

len(words)


# === Intro Section ===
st.title("📚 Reading Bingo")

st.markdown("""
Welcome to the **Reading Bingo Challenge**! 📖✨  
This is my personal bingo card — a mix of fun, quirky, and challenging prompts to spice up the year’s reading.

Want to play along? 🎲 You can generate your own random bingo card using the same prompt list below!
""")

# === Show Fixed Personal Bingo ===
st.subheader("My Bingo Card 🎯")
personal_card_html = generate_word_bingo_html(words, fixed_seed=200)  # Add optional seed for a fixed card
st.markdown(personal_card_html, unsafe_allow_html=True)

# === Spacer ===
st.markdown("---")

# === Interactive Generator Section ===
st.subheader("Generate Your Own Bingo Card")

# Initialize default user bingo
if "bingo_html" not in st.session_state:
    st.session_state["bingo_html"] = generate_word_bingo_html(words)

if st.button("🎲 Generate New Card"):
    st.session_state["bingo_html"] = generate_word_bingo_html(words)

st.markdown(st.session_state["bingo_html"], unsafe_allow_html=True)

# === Optional: Download ===
#image_path = save_bingo_as_image(st.session_state["bingo_html"])
#with open(image_path, "rb") as f:
#    st.download_button("📥 Download Your Bingo Card", f, file_name="reading_bingo_card.png")
