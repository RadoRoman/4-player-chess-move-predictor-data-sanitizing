create table game
(
	id INTEGER
		primary key,
	game_id INTEGER(10) not null,
	username VARCHAR(255) not null,
	round_nr VARCHAR(5) not null,
	moves_time TEXT not null,
	color VARCHAR(10) not null
);

