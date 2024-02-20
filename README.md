This python-script based on:
https://www.theengineeringprojects.com/2022/09/internet-speed-monitor-using-raspberry-pi-4.html
to check my internet speed with the tool speedtest and store all values to an influxdb.
I can make grafana dashboards to visualize the results of the speedtest-commands.
The start of my script works with a cron-job like:
<code>
*/5 * * * * /usr/bin/python /home/pi/speedtest.py >> /home/pi/speedtest.log
</code>
