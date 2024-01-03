# calculator
Basic string-input calculator for a college assignment

To run you need to download python here: https://www.python.org/downloads

Only the calculator.py needs to be downloaded. Once downloaded, open a command prompt and change to the directory to wherever the calculator.py file is located. Then enter "python calculator.py" to run.

Examples of using the program:
![calculator default usage](https://github.com/sharktrexer/calculator/assets/32965854/880b1cca-a1f3-4000-907a-f4b06db94295)
![calculator debug](https://github.com/sharktrexer/calculator/assets/32965854/45f01927-3f05-4834-acb9-3c29183886ac)
![calculator help](https://github.com/sharktrexer/calculator/assets/32965854/43291470-7183-405e-90db-75a07beca384)


Known Bugs:
- an equation that negates a function being applied to an expression will be incorrectly evaluated i.e., "-sin(8+4)" will be evaluated as "-(sin(8)+4)"
- an equation such as "2-94+" will be accepted as valid and ignore the hanging operator
