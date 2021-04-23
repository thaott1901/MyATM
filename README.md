# MyATM

This is a simple ATM program

### Clone: Using the following git repository:

https://github.com/thaott1901/MyATM.git

### Test environment:

-  PyCharm 2020.2.3 Community edition.
-  Python 3.8.

### Demo:
The running process will be as follow:
Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw

Demo steps:
- Run Main.py
- Input cardID: for default test case in code, use 12345 or 54321
- Input pin number, for default test: 123 for card 12345 or 543 for 54321
- The screen will show a list of available account. For testing:
    Card 12345 --> account: a1, a2
    Card 54321 --> account: b1, b2
    --> input 1 of the account: a1, a2, b1, b2
- The screen will show 3 items in the corresponding account:
    + Account balance: current account balance
    + Deposit history: show as list of pair value (date: value) (date can be implemented differently)
    + Withdraw history: show as list of pair value (date: value) (date can be implemented differently)

Note: 
- For more testing, testers can use these functions to set different testing scenario:
    + depositCash, withdrawCash
    + createAccount

