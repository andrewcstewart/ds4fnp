select 
    to_date(year::VARCHAR, 'YYYY') as year,
    INITCAP(candidate) as candidate,
    split_part(candidate, ', ', 1) as candidate_lastname,
    split_part(candidate, ', ', 2) as candidate_firstname,
    INITCAP(party) as party,
    INITCAP(state) as state,
    state_po,
    candidatevotes::INTEGER as candidate_votes,
    totalvotes as total_votes,
	ROUND(candidatevotes::numeric / totalvotes::numeric * 100, 2) as vote_pct
from {{ source('mit','mit__president_elections') }}
where writein::BOOLEAN is False