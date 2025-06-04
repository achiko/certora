methods {
    function totalVotes() returns (uint256) envfree;
}


rule voteIntegrity(bool inFavor) {
    uint256 votedBefore = totalVotes();

    env e;

    vote(e, inFavor);

    assert(totalVotes(e) > votedBefore, "Total votes should increase");
    
    // uint256 totalVotes = Voting.totalVotes();
    // uint256 votesInFavor = Voting.votesInFavor();
    // uint256 votesAgainst = Voting.votesAgainst();

    // assert(totalVotes == votesInFavor + votesAgainst);
    // assert(votesInFavor + votesAgainst == totalVotes);
    // assert(votesInFavor >= 0);
    // assert(votesAgainst >= 0);
}