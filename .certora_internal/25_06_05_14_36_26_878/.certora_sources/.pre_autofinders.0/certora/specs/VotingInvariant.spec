methods {
    function votesInFavor() external returns (uint256) envfree;
    function votesAgainst() external returns (uint256) envfree;
    function totalVotes() external returns (uint256) envfree;
}


rule voteInvariantTest() {
    
    uint256 totalVotes = totalVotes();
    uint256 votesInFavor = votesInFavor();
    uint256 votesAgainst = votesAgainst();

    env e;

    assert(totalVotes(e) == 0);
    assert(votesInFavor(e) == 0);
    assert(votesAgainst(e) == 0);

    vote(e, true);

    assert(votesInFavor(e) == 1, "Votes in favor should be 1");
    assert(votesAgainst(e) == 0, "Votes against should be 0");
    assert(totalVotes(e) == 1, "Total votes should be 1");

    

    vote(e, false);

    assert(votesInFavor(e) == 1, "Votes in favor should be 1");
    assert(votesAgainst(e) == 1, "Votes against should be 1");
    assert(totalVotes(e) == 2, "Total votes should be 2");

    assert(votesInFavor() + votesAgainst() == to_mathint( totalVotes() ), "Total Votes shuld be equal sum of all votes");
}

invariant totalVotesInvariant() 
    votesInFavor() + votesAgainst() == to_mathint( totalVotes());
