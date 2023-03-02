/// 2023 Console Cowboys Python Smart Contract Hacking Course
/// @author Olie Brown @ficti0n
/// http://cclabs.io 

pragma solidity ^0.8.0; 

contract HelloWorld_Bank{
address public owner;
string private message;

  	mapping (address => uint) private balances;
  
  	constructor ()  payable {
    		owner = msg.sender; 
		message = "Hello";
 	 }

//Create Deposit Event
    event DepositLog(address indexed sender, uint value, string message);

//Setting Up authorization
    	function isOwner () public view returns(bool) {
        		return msg.sender == owner;
  	}

    	modifier onlyOwner() {
        		require(isOwner());
         		_;
  	}
  
	function changeMessage(string memory myMessage) public {
		message = myMessage;
	}

  	function deposit () public payable {
        		require((balances[msg.sender] + msg.value) >= balances[msg.sender]);
        		balances[msg.sender] += msg.value;
                emit DepositLog(msg.sender, msg.value ,"Deposited Eth");
    	}

    	function withdraw (uint withdrawAmount) public {
        		require (withdrawAmount <= balances[msg.sender]);
        
        		balances[msg.sender] -= withdrawAmount;
        		payable(msg.sender).transfer(withdrawAmount);
    	}
  
  
    	function withdrawAll() public onlyOwner {
        		payable(msg.sender).transfer(address(this).balance);
 	 }

	    function getBalance () public view returns (uint){
        		return balances[msg.sender];
    	}
}
