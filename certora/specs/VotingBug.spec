methods {
    // Declares the getter for the public state variables as `envfree`
    function totalVotes() external returns (uint256) envfree;
}

rule voteIntegrity(bool inFavor) {
    uint256 votedBefore = totalVotes();

    env e;

    vote(e, inFavor);

    assert(totalVotes(e) > votedBefore, "Total votes should increase");
    
}
