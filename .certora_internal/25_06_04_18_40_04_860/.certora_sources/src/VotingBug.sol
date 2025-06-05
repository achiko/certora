// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

contract VotingBug {
    uint256 public number;

    mapping(address => bool) public voters;

    uint256 public votesInFavor;
    uint256 public votesAgainst;
    uint256 public totalVotes;

    function vote(bool inFavor) public {
        require(!voters[msg.sender], "Already voted");
        voters[msg.sender] = true;

        totalVotes = 1;
        if (inFavor) {
            votesInFavor += 1;
        } else {
            votesAgainst += 1;
        }
    }

}
