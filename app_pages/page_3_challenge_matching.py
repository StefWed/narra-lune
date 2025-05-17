import streamlit as st
from modules.prompt_random_picker import get_random_prompt
from modules.book_matcher import find_existing_book_match

st.header("🔍 Find a Book for a Challenge Prompt")

# Step 1: Button to pick a random prompt
if "selected_prompt" not in st.session_state:
    st.session_state.selected_prompt = None
    st.session_state.prompt_id = None

if st.button("🎲 Pick a Random Challenge for Me"):
    prompt_id, prompt_text = get_random_prompt()
    st.session_state.selected_prompt = prompt_text
    st.session_state.prompt_id = prompt_id

# Step 2: Display the picked prompt (if any)
if st.session_state.selected_prompt:
    st.markdown("### Your Challenge Prompt:")
    st.success(st.session_state.selected_prompt)

    # Step 3: Matching button only appears once a prompt is picked
    if st.button("📚 Try to Match a Book"):
        matched_book = find_existing_book_match(st.session_state.prompt_id)

        if matched_book:
            title, author, blurb, genre, pages = matched_book
            st.success(f"🎉 Found a match!\n\n**{title}** by *{author}*")
            st.markdown(f"**Genre:** {genre}  \n**Pages:** {pages}")
            st.markdown(f"**Blurb:** {blurb}")
        else:
            st.warning("😕 No book has been matched to this prompt yet.")