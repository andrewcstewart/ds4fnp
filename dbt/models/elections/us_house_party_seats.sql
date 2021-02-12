WITH sub1 AS (
	SELECT
		*,
		rank() OVER (PARTITION BY year,
			state,
			district ORDER BY candidate_votes DESC) AS rank
	FROM
		{{ ref('stg_us_house_election_results') }}
),
sub2 AS (
SELECT
	*,
	rank = 1 AS winner
FROM
	sub1
)

select 
	year,
	party,
	count(*) as seats
from sub2
where winner = True
group by year, party
