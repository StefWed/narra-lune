from dotenv import load_dotenv
import os
import openai

# Load variables from .env
load_dotenv()

# Set up OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)


def extract_genre_with_llm(prompt_text):
    """
    Uses LLM to determine if a reading challenge prompt implies a specific book genre.
    Returns a genre string if one is confidently identified, else None.
    """
    system_prompt = (
        "You are a book genre expert. Your task is to analyze the reading challenge prompt "
        "and extract the specific genre of book that would satisfy this challenge. "
        "Look for explicit genre mentions as well as implicit genre suggestions. "
        "Consider common genres like: Fantasy, Science Fiction, Mystery, Murder Mystery, Thriller, Horror, "
        "Romance, Historical Fiction, Literary Fiction, Non-Fiction, Biography, Memoir, "
        "Self-Help, Young Adult, Children's, Poetry, Drama, Dystopia, Adventure, etc. "
        "If multiple genres could apply, select the most specific or dominant one."
    )

    user_prompt = (
        f'Reading Challenge Prompt: "{prompt_text}"\n\n'
        'Respond with ONLY the genre name if one is implied (either explicitly or implicitly). '
        'Return just the name of the most appropriate genre, without explanation. '
        'If no specific genre is implied, respond with exactly "None".'
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3
        )

        genre = response.choices[0].message.content.strip()
        return None if genre.lower() == "none" else genre
    except Exception as e:
        print(f"Error in genre extraction: {e}")
        return None