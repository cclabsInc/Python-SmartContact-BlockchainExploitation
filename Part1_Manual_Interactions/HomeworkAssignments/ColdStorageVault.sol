// 2023 Console Cowboys Python Smart Contract Hacking Course
// @author Olie Brown @ficti0n
// http://cclabs.io 

pragma solidity ^0.8.0;

contract ColdStorageVault {
    bool public is_locked;
    string private my_password;

    constructor(string memory password) payable {
        is_locked = true;
        my_password = password;
    }

    function WithdrawAll() public   {
        require(is_locked == false, "Withdraw function locked");
        payable (msg.sender).transfer(address(this).balance);
    }

    function unlock(string memory password) external returns (string memory) {
        if (keccak256(abi.encodePacked(my_password)) == keccak256(abi.encodePacked(password))) {
            is_locked = false;
            return "Correct password";
        }
        else{
            return "Bad Password";
            }
        
    }
    function lock() external {
        is_locked = true;
    }

}
