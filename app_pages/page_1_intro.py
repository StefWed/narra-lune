import streamlit as st
from modules.book_picker import get_random_book

st.header("Welcome to NarraLune!")

st.write("""
**Welcome to NarraLune – your playful guide through the world of books!**
NarraLune is like a digital treasure hunt for your next favorite read. Part game, part
book-matching companion, it's your personal librarian. Whether you read one book a year or devour a stack a week, 
NarraLune helps you discover books in fun, creative ways. 

It all starts with reading challenge prompts — tasks that ask you to find books based on not only genres, but also
settings, themes, characters, or even a single word in the title. Some are easy, others might send you digging through 
library stacks or calling a bookish friend for help.

The idea is to step outside your usual reading patterns: read more, read differently, and get creative. To inspire 
you even more and to help you in your search, the app includes a curated selection of book recommendations. After 
deciding on a prompt, it let's you start a matching process to find a book.

And to make it a shared adventure, I’ve added a Reading Bingo game — you’ll discover that on the second page.

So...
Pack your bookmarks.
Sharpen your TBR (to be read) list.
And step into the story.


---


### What can you do?

""")

st.page_link("app_pages/page_2_reading_bingo.py", label="Start with a Bingo Card", icon="🎲")
st.write("Print it, share it, or use it as your yearly reading map.")

st.page_link("app_pages/page_3_challenge_matching.py", label="Find a Book for a Reading Prompt", icon="🔍")
st.write("Get a random prompt, then find the perfect book match.")

st.write("---")

with st.container():
    st.subheader("📚 Spotlight Book")

    book = get_random_book()

    if book:
        title, author, blurb, genre, pages = book

        st.markdown(
            f"""
            <div style="
                border: 1px solid rgba(200, 200, 200, 0.5);
                border-radius: 10px;
                padding: 1rem;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.04);
                margin-bottom: 1.5rem;
            ">
                <strong>{title}</strong><br>
                <em>by {author}</em><br><br>
                <strong>Genre:</strong> {genre} &nbsp; | &nbsp; <strong>Pages:</strong> {pages}<br><br>
                <strong>Blurb:</strong> {blurb}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        st.warning("No books available yet for Daily Pick!")