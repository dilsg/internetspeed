This python-script based on:
https://www.theengineeringprojects.com/2022/09/internet-speed-monitor-using-raspberry-pi-4.html
to check my internet speed with the tool speedtest and store all values on an influxdb.
First on installation I need:
<code>
sudo apt install apt-transport-https gnupg1 dirmngr
</code>

<code>
curl -L https://packagecloud.io/ookla/speedtest-cli/gpgkey | gpg --dearmor | sudo tee /usr/share/keyrings/speedtestcli-archive-keyring.gpg >/dev/null
</code>

<code>
echo "deb [signed-by=/usr/share/keyrings/speedtestcli-archive-keyring.gpg] https://packagecloud.io/ookla/speedtest-cli/debian/ $(lsb_release -cs) main" | sudo tee  /etc/apt/sources.list.d/speedtest.list
</code>

<code>
sudo apt update
</code>

<code>
sudo apt install speedtest
</code>

Check it with:
<code>
speedtest
</code>


*** INFLUXDB

<code>
CREATE DATABASE internetspeed
</code>

<code>
CREATE USER "speedmonitor" WITH PASSWORD 'pass' 
</code>
<code>
GRANT ALL ON "internetspeed" to "speedmonitor"
</code>

Quit 


<code>
sudo apt install python3-influxdb
</code>
<code>
CREATE DATABASE internetspeed
</code>


I can make grafana dashboards to visualize the results of the speedtest-commands.
The start of my script works with a cron-job like:
<code>
*/5 * * * * /usr/bin/python /home/pi/speedtest.py >> /home/pi/speedtest.log
</code>
