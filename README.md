# NarraLune

#### -- Project Status: Active

## Project Intro

As a bookworm and serial note-taker, I’ve spent years collecting notes from literary podcasts and magazine previews. At some point, I also discovered reading challenges (with prompts/tasks like “a book with over 500 pages” or “a book which features magic creatures that are not dragons”) and I found myself needing a better way to organize books and match them to the reading challenge prompts.

NarraLune is the result – a Python-based application that connects a curated book database with a matching framework. All prompts are routed through a decision layer which allocates them through the matching steps. The system uses structured SQL filtering (for prompts with structured data, e.g., “a book with over 500 pages”),  a genre inference component (for prompts which directly or indirectly ask for a genre, e.g., “a book which will make you scared”), and a more general inference component to recommend books for more generally formulated challenge prompts (e.g., a book where an adult character changes careers).

Besides integrating the curated database, keeping LLM Usage purposeful and cost-effective was a major principle in building this.

### Methods Used

* Database Generation and Management
* Applied NLP
* Data Visualization

### Technologies

* Python
* SQLite
* Streamlit

## Project Description

For the overall user interface/ web application it was decided on three pages:

1. A landing page which introduces the project and includes links to the other pages. It also integrates a "Spotlight Book" - a random book recommendation, pulled from the existing database.

2. A gamification page. This page includes a personal bingo card with 24 reading prompts (played by the developer) and the possibility for the user to generate an own bingo card with the same prompts to play along.

3. The actual interface for matching reading challenge prompt with book. For now it has the functionality to accept a randomly picked reading challenge prompt from the database. This will then set in place the matching framework, with components as further discribed below. The user will see messages, what the router checked and what the result was.

Following are the main components of the matching framework: 

### Check-Point
Has a reading challenge already been matched to a book/ several books. If yes, the pipeline stops and the respective finding will be printed.

### Prompt Router
Directs reading task to suitable matching strategy.

### Rule Matcher
Reading prompts with structured data are used for database queries.

### Genre Detector
LLM interprets possible genre implications in challenge prompts. Found genre is then used for database query.

### Blurb Matcher
LLM component compares book blurbs to abstract prompts to find matches.

## Getting Started

### Database

* You will find a schema to create your own database if needed.
* Seeds will be added as an example on how to fill the database.
