-- select california for database
SELECT * FROM states WHERE name = 'California' ORDER BY (SELECT MIN(cities.id) FROM cities WHERE cities.state_id = states.id) ASC;
