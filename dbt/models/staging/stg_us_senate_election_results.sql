select 
    to_date(year::VARCHAR, 'YYYY') as year,
    INITCAP(candidate) as candidate,
    INITCAP(party) as party,
    INITCAP(state) as state,
    state_po,
    candidatevotes::INTEGER as candidate_votes,
    totalvotes as total_votes,
	ROUND(candidatevotes::numeric / totalvotes::numeric * 100, 2) as vote_pct
from {{ source('mit','mit__senate_elections') }}
where writein::BOOLEAN is False