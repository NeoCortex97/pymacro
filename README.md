# pymacro
A simple macro system in pyton using pynput
## Dependencies
The project uses the following python Modules :
* pynput
* psutil
* subprocess (launchers only

### Usage details
The combo attribute of a macro should be a list of key codes fropm pynput.
If an action Method returns False the script will be exited normally.  
The Command attribute of The Launcher class schould be a list of the command and its parameters.  
If you want to use Hotkeys including the schift key it is advised to add a second instance with uppercase keys! 