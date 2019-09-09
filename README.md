# Multi Serial Protocol communication library
This python3.7 library enables control of MSP based cleanflight/betaflight flight controller boards via UART serial communication. It covers all commands and features listed in the [MultiWii wiki page](http://www.multiwii.com/wiki/index.php?title=Multiwii_Serial_Protocol). 
Initially tested using a Raspberry pi zero and an SP Racing F3 board communicating via the GPIO rx/tx pins.

## Installation and Initial setup
### Dependencies
- **Python3.7**
- pySerial
- Struct

`pip install .` should automatically install all requirements. 

### Requirements on the flight controller's side
- RX_MSP        (`#define USE_RX_MSP`)
- DYNBALANCE    (`#define DYNBALANCE`)

Throttle control via MSP may be disabled on certain boards with insufficient flash memory (anything under 128k flash size). Details on how to enable them can be found on [Cleanflight's GitHub repo](https://github.com/cleanflight/cleanflight/blob/master/docs/Customized%20Version.md).

