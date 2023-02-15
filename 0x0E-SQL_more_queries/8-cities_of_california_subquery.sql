-- Lists all the cities of california in the hbtn_0d_usa database
-- Order results by ascending order cities.id
SELECT `id`, `name`
	FROM `cities`
      WHERE `state_id` IN
		(SELECT `id`
	 FROM `states`
	WHERE `name` = "California")
	ORDER BY `id`;
