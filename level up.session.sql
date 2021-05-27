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