methods {
    function votesInFavor() external returns (uint256) envfree;
    function votesAgainst() external returns (uint256) envfree;
    function totalVotes() external returns (uint256) envfree;
}


invariant totalVotesInvariant() 
    votesInFavor() + votesAgainst() == to_mathint( totalVotes());
