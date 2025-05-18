import streamlit as st
from modules.prompt_random_picker import get_random_prompt
from modules.book_matcher import find_existing_book_match
from modules.prompt_router import route_challenge_input
from modules.rule_based_matcher import query_books_by_filters


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
        # Step 4: Calling find_existing_book_match to see if a match has already been made
        matched_book = find_existing_book_match(st.session_state.prompt_id)

        # Step 5: If a match has been made print book info
        if matched_book:
            title, author, blurb, genre, pages = matched_book
            st.success(f"🎉 Found a match!\n\n**{title}** by *{author}*")
            st.markdown(f"**Genre:** {genre}  \n**Pages:** {pages}")
            st.markdown(f"**Blurb:** {blurb}")
        else:
            st.warning("😕 No book has been matched to this prompt yet.")

            # Step 6: Route based on prompt structure
            route, info = route_challenge_input(st.session_state.selected_prompt)

            if route == "sql":
                rule_match = query_books_by_filters(info)
                if rule_match:
                    title, author, blurb, genre, pages = rule_match
                    st.info("🔍 Rule-based match found:")
                    st.markdown(f"**{title}** by *{author}*")
                    st.markdown(f"**Genre:** {genre}  \n**Pages:** {pages}")
                    st.markdown(f"**Blurb:** {blurb}")
                else:
                    st.info("Tried structured rule, but found no matching book.")

            elif route == "semantic":
                st.info("Prompt is abstract — trying semantic match next...")
                # Placeholder: Call your LLM matcher here
                # result = query_books_by_llm(info)

            else:
                st.warning("Couldn't determine how to process this prompt yet.")
