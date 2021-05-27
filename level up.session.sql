SELECT
    e.id,
    e.organizer_id as gamer_id,
    e.date,
    e.time,
    g.title AS game_name,
    u.id gamer_id,
    u.first_name || ' ' || u.last_name AS full_name
FROM
    levelupapi_event e
JOIN
    levelupapi_game g ON  g.id = e.game_id
JOIN
    levelupapi_gamer gr ON e.organizer_id = gr.id
JOIN
    auth_user u ON gr.user_id = u.id

-- create a view that multiple applications can call

CREATE VIEW GAMES_BY_USER AS
SELECT
    g.id,
    g.title,
    g.maker,
    g.genre_id,
    g.number_of_players,
    g.skill_level,
    u.id user_id,
    u.first_name || ' ' || u.last_name AS full_name
FROM
    levelupapi_game g
JOIN
    levelupapi_gamer gr ON g.gamer_id = gr.id
JOIN
    auth_user u ON gr.user_id = u.id
;

-- create a view to replace the user events report query
CREATE VIEW EVENTS_BY_USER AS
SELECT
    e.id,
    e.organizer_id,
    e.date,
    e.time,
    g.title AS game_name,
    u.id user_id,
    u.first_name || ' ' || u.last_name AS full_name
FROM
    levelupapi_event e
JOIN
    levelupapi_game g ON  g.id = e.game_id
JOIN
    levelupapi_gamer gr ON e.organizer_id = gr.id
JOIN
    auth_user u ON gr.user_id = u.id;