-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file, also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;


CREATE TABLE player
(
    player_id SERIAL PRIMARY KEY,
    name varchar(64)
);

CREATE TABLE match
(
    match_id SERIAL PRIMARY KEY,
    winner int REFERENCES player(player_id) ON DELETE CASCADE,
    loser int REFERENCES player(player_id) ON DELETE CASCADE
);

CREATE VIEW standing AS
(
    select
        p.player_id,
        p.name,
        count(m.winner) as win,
        (select count(*)
            from match m2
            where p.player_id=m2.winner or p.player_id=m2.loser
            ) as total
    from
        player p
        left join match m
        on p.player_id=m.winner
    group by
        p.player_id,
        p.name
    order by win desc, p.player_id asc
);
