-- initial seeds to start filling the database


-- books table
INSERT INTO books (title, author, pages, pub_date, blurb, genre)
	VALUES
	('Onkel Toms Huette, Berlin',
	'Pierre Frei',
	542,
	2005,
	'Im Berlin der frühen Nachkriegszeit treibt ein Serienmörder sein Unwesen. Ihm fallen vier Frauen aus unterschiedlichen Milieus zum Opfer: eine UfA-Schauspielerin, eine Psychiatrie- Krankenschwester, eine Prostituierte und eine Adelige im Auswärtigen Amt. Sie sind alle jung, blond und werden brutal zugerichtet und erwürgt.',
	'Thriller');


-- reading_challenges
INSERT INTO reading_challenges (name)
	VALUES 
	('The 52 Book Clubs Mystery Genre Challenge');
	
	
-- prompts
	
WITH challenge AS(
	SELECT id FROM reading_challenges
	WHERE name = 'The 52 Book Clubs Mystery Genre Challenge'
	)
	 
INSERT INTO prompts (challenge_id, text)
	VALUES
	((SELECT id FROM challenge), 'Murder disguised as an accident'),
	((SELECT id FROM challenge), 'A crime-solving duo'),
	((SELECT id FROM challenge), 'A victim with lots of enemies'),
	((SELECT id FROM challenge), 'A missing murder weapon');

	
-- challenge-books
-- this needs to be done fully manually

INSERT INTO challenge_books (prompt_id, book_id)
	VALUES
  --(prompt_id, book_id);



