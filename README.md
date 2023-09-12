# pingScript
a python script that pings a host and outputs the time if a failed response is returned

the time is output to myfile.txt

to run the command:
nohup python pingScript1.py > /dev/null 2>&1&

ps aux | grep python
to kill the python process

