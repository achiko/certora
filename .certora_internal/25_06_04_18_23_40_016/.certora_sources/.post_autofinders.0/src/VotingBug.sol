// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

contract VotingBug {
    uint256 public number;

    mapping(address => bool) public voters;

    uint256 public votesInFavor;
    uint256 public votesAgainst;
    uint256 public totalVotes;

    function vote(bool inFavor) public {assembly ("memory-safe") { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00000000, 1037618708480) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00000001, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00000005, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00006000, inFavor) }
        require(!voters[msg.sender], "Already voted");
        voters[msg.sender] = true;

        totalVotes += 1;
        if (inFavor) {
            votesInFavor += 1;
        } else {
            votesAgainst += 1;
        }
    }

}
