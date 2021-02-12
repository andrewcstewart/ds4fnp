WITH foo AS (
	SELECT
		*,
		rank() OVER (PARTITION BY year,
			state
			ORDER BY candidate_votes DESC) AS rank
	FROM
		{{ ref('stg_us_senate_election_results') }}
),
foo2 AS (
SELECT
	*,
	rank = 1 AS winner
FROM
	foo
)

select 
	year,
	party,
	count(*) as seats
from foo2
where winner = True
group by year, party
