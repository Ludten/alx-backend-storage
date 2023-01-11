# MySQL advanced
> Each file in this repository holds code that illustrates MySQL
> specific to SQL.

## Description of what each file shows:
* 0-uniq_users.sql: SQL script that creates a table `users` following these requirements:

	- With these attributes:
		- `id`, integer, never null, auto increment and primary key
		- `email`, string (255 characters), never null and unique
		- `name`, string (255 characters)
	- If the table already exists, your script should not fail
	- Your script can be executed on any database

* 1-country_users.sql: SQL script that creates a table users following these requirements:

    - With these attributes:
		- `id`, integer, never null, auto increment and primary key
		- `email`, string (255 characters), never null and unique
		- `name`, string (255 characters)
		- `country`, enumeration of countries: `US`, `CO` and `TN`, never null (= default will be the first element of the enumeration, here `US`)
	- If the table already exists, your script should not fail
	- Your script can be executed on any database

* 2-fans.sql: SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans

	__Requirements:__
	- Import this table dump: [metal_bands.sql.zip](https://intranet.alxswe.com/rltoken/uPn947gnZLaa0FJrrAFTGQ)
	- Column names must be: `origin` and `nb_fans`
	- Your script can be executed on any database

* 3-glam_rock.sql: A SQL script that lists all bands with `Glam rock` as their main style, ranked by their longevity

	__Requirements:__
	- Import this table dump: [metal_bands.sql.zip](https://intranet.alxswe.com/rltoken/uPn947gnZLaa0FJrrAFTGQ)
	- Column names must be: `band_name` and `lifespan` (in years)
	- You should use attributes `formed` and `split` for computing the `lifespan`
	- Your script can be executed on any database

* 4-store.sql: A SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

	Quantity in the table `items` can be negative.

* 5-valid_email.sql: A SQL script that creates a trigger that resets the attribute `valid_email` only when the `email` has been changed.

* 6-bonus.sql: A SQL script that creates a stored procedure `AddBonus` that adds a new correction for a student.

	__Requirements:__
	- Procedure `AddBonus` is taking 3 inputs (in this order):
		- `user_id`, a `users.id` value (you can assume `user_id` is linked to an existing `users`)
		- `project_name`, a new or already exists `projects` - if no `projects.name` found in the table, you should create it
		- score, the score value for the correction

* 7-average_score.sql: A SQL script that creates a stored procedure `ComputeAverageScoreForUser` that computes and store the average score for a student. Note: An average score can be a decimal

	__Requirements:__
	- Procedure `ComputeAverageScoreForUser` is taking 1 input:
		- `user_id`, a `users.id` value (you can assume `user_id` is linked to an existing `users`)

* 8-index_my_names.sql: A SQL script that creates an index `idx_name_first` on the table `names` and the first letter of `name`.

	__Requirements:__

	- Import this table dump: [names.sql.zip](https://intranet.alxswe.com/rltoken/BluyCCIIfw0NqcjqUiUdEw)
	- Only the first letter of `name` must be indexed

* 9-index_name_score.sql: A SQL script that creates an index `idx_name_first_score` on the table `names` and the first letter of `name` and the score.

	__Requirements:__

	- Import this table dump: [names.sql.zip](https://intranet.alxswe.com/rltoken/BluyCCIIfw0NqcjqUiUdEw)
	- Only the first letter of `name` AND `score` must be indexed

* 10-div.sql: A SQL script that creates a function `SafeDiv` that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

	__Requirements:__

	- You must create a function
	- The function `SafeDiv` takes 2 arguments:
		- `a`, INT
		- `b`, INT
	- And returns `a / b` or 0 if `b == 0`

* 11-need_meeting.sql: A SQL script that creates a view `need_meeting` that lists all students that have a score under 80 (strict) and no `last_meeting` or more than 1 month.

	__Requirements:__

	- The view `need_meeting` should return all students name when:
		- They score are under (strict) to 80
		- __AND__ no `last_meeting` date __OR__ more than a month

* 100-average_weighted_score.sql: A SQL script that creates a stored procedure `ComputeAverageWeightedScoreForUser` that computes and store the average weighted score for a student.

	__Requirements:__

	- Procedure ComputeAverageScoreForUser is taking 1 input:
		- `user_id`, a `users.id` value (you can assume `user_id` is linked to an existing `users`)

* 101-average_weighted_score.sql: A SQL script that creates a stored procedure `ComputeAverageWeightedScoreForUsers` that computes and store the average weighted score for all students.

	__Requirements:__

	- Procedure `ComputeAverageWeightedScoreForUsers` is not taking any input.
