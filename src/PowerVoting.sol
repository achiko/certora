// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "./MinimalToken.sol";

contract PowerVoting {

    MinimalToken public token;
    uint256 public number;

    mapping(address => bool) public voters;
    mapping(address => uint256) public amountVoted;

    uint256 public votesInFavor;
    uint256 public votesAgainst;
    
    function totalVotes() public view returns (uint256) {
        return token.balanceOf(address(this));
    }

    function vote(bool inFavor) public {
        require(!voters[msg.sender], "Already voted");
        voters[msg.sender] = true;

        uint256 power = token.balanceOf(msg.sender);
        token.transferFrom(msg.sender, address(this), power);
        amountVoted[msg.sender] += power;

        if (inFavor) {
            votesInFavor += power;
        } else {
            votesAgainst += power;
        }
    }

}
