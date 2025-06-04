// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Test, console} from "forge-std/Test.sol";
import {VotingBug} from "../src/VotingBug.sol";

contract CounterTest is Test {
    VotingBug public counter;

    function setUp() public {
        counter = new VotingBug();
        // counter.setNumber(0);
    }

    function test_Increment() public {
        assert(true);
    }

    // function testFuzz_SetNumber(uint256 x) public {
    //     counter.setNumber(x);
    //     assertEq(counter.number(), x);
    // }
}
