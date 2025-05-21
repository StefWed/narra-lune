import streamlit as st
from modules.prompt_random_picker import get_random_prompt
from modules.book_matcher import find_existing_book_match
from modules.prompt_router import route_challenge_input
from modules.rule_based_matcher import query_books_by_filters
from modules.query_books_by_genre import query_books_by_genre
from modules.semantic_blurb_matcher import query_books_by_llm

st.header("🔍 Find a Book for a Reading Challenge Prompt")

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

            # Step 6: Route based on prompt structure - now includes genre detection
            route, info = route_challenge_input(st.session_state.selected_prompt)
            match_found = False

            if route == "sql":
                rule_match = query_books_by_filters(info)
                if rule_match:
                    title, author, blurb, genre, pages = rule_match
                    st.info("🔍 Rule-based match found:")
                    st.markdown(f"**{title}** by *{author}*")
                    st.markdown(f"**Genre:** {genre}  \n**Pages:** {pages}")
                    st.markdown(f"**Blurb:** {blurb}")
                    match_found = True
                else:
                    st.info("Tried structured rule, but found no matching book.")

            elif route == "genre":
                with st.spinner(f"Looking for books in genre: {info}..."):
                    st.info(f"📚 Detected genre: **{info}**")

                    # Query books by the extracted genre
                    genre_match = query_books_by_genre(info)

                    if genre_match:
                        title, author, blurb, genre, pages = genre_match
                        st.success(f"Found a book by genre match:")
                        st.markdown(f"**{title}** by *{author}*")
                        st.markdown(f"**Genre:** {genre}  \n**Pages:** {pages}")
                        st.markdown(f"**Blurb:** {blurb}")
                        match_found = True
                    else:
                        st.warning(f"No books found for genre: {info}")

            elif route == "semantic":
                st.info("Prompt is abstract — trying semantic matching...")

            # If no match found yet, try semantic matching as a last resort
            if not match_found:
                with st.spinner("Using AI to find a matching book by analyzing blurbs..."):
                    semantic_match = query_books_by_llm(st.session_state.selected_prompt)

                    if semantic_match:
                        title, author, blurb, genre, pages = semantic_match
                        st.success(f"🤖 AI found a match through blurb analysis:")
                        st.markdown(f"**{title}** by *{author}*")
                        st.markdown(f"**Genre:** {genre}  \n**Pages:** {pages}")
                        st.markdown(f"**Blurb:** {blurb}")
                    else:
                        st.warning("Could not find a suitable book match for this prompt.")