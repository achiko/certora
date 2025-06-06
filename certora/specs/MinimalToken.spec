methods {
    function balanceOf(address) external returns (uint256) envfree;
    function totalSupply() external returns (uint256) envfree;
    function transfer(address, uint256) external returns (bool) envfree;
    function transferFrom(address, address, uint256) external returns (bool);
    function approve(address, uint256) external returns (bool);
}

/// @title Address Zero Invariant
invariant nonBalanceAddressZero() 
    balanceOf(0) == 0;

/// @title Token Solvency Invariant
invariant tokenSolvency()

    // 'nativeBalances' is a mapping that represents the balances of native tokens,
    // such as ETH on the Ethereum network. The balance for a specific address 'a'
    // can be accessed using 'nativeBalances[a]'.
    // https://docs.certora.com/en/latest/docs/cvl/expr.html 
    
    nativeBalances[currentContract] >= totalSupply();
