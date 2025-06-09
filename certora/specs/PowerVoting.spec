 using MinimalToken as token;

methods {
    function totalVotes() external returns (uint256) envfree;
    function votesInFavor() external returns (uint256) envfree;
    function votesAgainst() external returns (uint256) envfree;

    function MinimalToken.balanceOf(address) external returns (uint256) envfree;
}

// @title Vote Integrity
rule voteIntegrity(bool inFavor) {
    uint256 votedBefore = totalVotes();
    
    env e;
    
    uint256 balance = token.balanceOf(e.msg.sender);

    vote(e, inFavor);
    assert(balance > 0 => totalVotes(e) > votedBefore, "Total votes should increase");
    assert(balance == 0 => totalVotes(e) == votedBefore, "Total votes should NOT increase");
}

// Invariant: Total votes should be equal to the sum of votes in favor and votes against
invariant voteIntegrityInvariant() 
    votesInFavor() + votesAgainst() == to_mathint(totalVotes());