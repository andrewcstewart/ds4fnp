WITH sub1 AS (
	SELECT
		*,
		rank() OVER (PARTITION BY year,
			state
			ORDER BY candidate_votes DESC) AS rank
	FROM
		{{ ref('stg_us_president_election_results') }}
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
	count(*) as popular_votes
from sub2
where winner = True
group by year, party
