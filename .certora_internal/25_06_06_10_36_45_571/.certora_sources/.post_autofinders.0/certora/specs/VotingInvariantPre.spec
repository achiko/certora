methods {
    function votesInFavor() external returns (uint256) envfree;
    function votesAgainst() external returns (uint256) envfree;
    function totalVotes() external returns (uint256) envfree;
}



rule totalVotesIsSumOfVotes(bool inFavor) {
    
    uint256 totalVotesPre = totalVotes();
    uint256 votesInFavorPre = votesInFavor();
    uint256 votesAgainstPre = votesAgainst();

    require(votesInFavorPre+votesAgainstPre == to_mathint(totalVotesPre), "");

    env e;
    
    vote(e, inFavor);

    uint256 totalVotesPost = totalVotes();
    uint256 votesInFavorPost = votesInFavor();
    uint256 votesAgainstPost = votesAgainst();

    require(votesInFavorPost+votesAgainstPost == to_mathint(totalVotesPost), "Total Votes should be equal sum of all votes");

}

invariant totalVotesIsSumOfVotesInvariant() 
    votesInFavor() + votesAgainst() == to_mathint( totalVotes());
