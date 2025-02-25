// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ProductVerification {
    struct Product {
        string name;
        string serial;
        address owner;
    }

    mapping(string => Product) public products;

    function addProduct(string memory _name, string memory _serial) public {
        require(bytes(products[_serial].serial).length == 0, "Product already exists.");
        products[_serial] = Product(_name, _serial, msg.sender);
    }

    function verifyProduct(string memory _serial) public view returns (bool) {
        return bytes(products[_serial].serial).length > 0;
    }
}
