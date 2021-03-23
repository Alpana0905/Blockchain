Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\Latitude\Desktop\night sessions\s1-unveiling blockchain\blockchain.py
>>> local_blockchain=Blockchain()
>>> block_one_transactions={"sender":"Alpana","receiver":"Navya","amount":"1000"}
>>> block_two_transactions={"sender":"Navya","receiver":"Khushi","amount":"2500"}
>>> block_three_transactions={"sender":"Khushi","receiver":"Rehaan","amount":"3500"}
>>> fake_transactions={"sender":"Navya","receiver":"Khushi,Alpana","amount":"1500"}
>>> local_blockchain.add_block(block_one_transactions)
('00ce18d16569ae5904e2d6f2e29d786d525490ad7a770b9779ba91ff2d6b0425', <block.Block object at 0x000002720D8B88E0>)
>>> local_blockchain.print_blocks()
Block 0 <block.Block object at 0x000002720D8B89A0>
timestamp: 2021-02-23 17:19:17.021149
transactions: {}
current hash: 2cf31ab1aeb9ba03996a08c41918c46e045281132c8ed21abca91ac109e0f052
previous hash: 0
Block 1 <block.Block object at 0x000002720D8B88E0>
timestamp: 2021-02-23 18:28:30.848883
transactions: {'sender': 'Alpana', 'receiver': 'Navya', 'amount': '1000'}
current hash: 10218e84ce5ef18cdbb7714509a5c99691028d94ba91c88f4793fbbffc96d542
previous hash: 2cf31ab1aeb9ba03996a08c41918c46e045281132c8ed21abca91ac109e0f052
>>> local_blockchain.add_block(block_two_transactions)
('002fc0325265f05be118f4e488920089a15dc2de7dd942344f0280ac14bd7542', <block.Block object at 0x000002720D8B8BE0>)
>>> local_blockchain.add_block(block_three_transactions)
('00554e4256d1677c9fc8a3aef71eba64da0f5abeef2cd6d757e781079e99d3cf', <block.Block object at 0x000002720D8B8C70>)
>>> local_blockchain.print_blocks()
Block 0 <block.Block object at 0x000002720D8B89A0>
timestamp: 2021-02-23 17:19:17.021149
transactions: {}
current hash: 2cf31ab1aeb9ba03996a08c41918c46e045281132c8ed21abca91ac109e0f052
previous hash: 0
Block 1 <block.Block object at 0x000002720D8B88E0>
timestamp: 2021-02-23 18:28:30.848883
transactions: {'sender': 'Alpana', 'receiver': 'Navya', 'amount': '1000'}
current hash: 10218e84ce5ef18cdbb7714509a5c99691028d94ba91c88f4793fbbffc96d542
previous hash: 2cf31ab1aeb9ba03996a08c41918c46e045281132c8ed21abca91ac109e0f052
Block 2 <block.Block object at 0x000002720D8B8BE0>
timestamp: 2021-02-23 18:30:02.495419
transactions: {'sender': 'Navya', 'receiver': 'Khushi', 'amount': '2500'}
current hash: 7f9ad7d768e0c27263a5cea21deee6655a67584f4e8c7a25f8451bc6c1cced3a
previous hash: 10218e84ce5ef18cdbb7714509a5c99691028d94ba91c88f4793fbbffc96d542
Block 3 <block.Block object at 0x000002720D8B8C70>
timestamp: 2021-02-23 18:30:25.903118
transactions: {'sender': 'Khushi', 'receiver': 'Rehaan', 'amount': '3500'}
current hash: f35bbe435a37a55176709059eee1838be718bcc00ae64f9f4a3b8039b060d887
previous hash: 7f9ad7d768e0c27263a5cea21deee6655a67584f4e8c7a25f8451bc6c1cced3a
>>> local_blockchain.chain[2].transactions=fake_transactions
>>> local_blockchain.validate_chain()
The current hash of the block does not equal the generated hash of the block.
False
>>> 