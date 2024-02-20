import re
import subprocess

from influxdb import InfluxDBClient
from datetime import datetime

response = subprocess.Popen('/usr/bin/speedtest --accept-license --accept-gdpr',
    shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')

ping = re.search('Latency:\s+(.*?)\s', response, re.MULTILINE)

download = re.search('Download:\s+(.*?)\s', response, re.MULTILINE)
download_low = re.search('Download:.*?low:\s+(.*?)ms', response, re.DOTALL)
download_high = re.search('Download:.*?high:\s+(.*?)ms', response, re.DOTALL)

upload = re.search('Upload:\s+(.*?)\s', response, re.MULTILINE)
upload_low = re.search('Upload:.*?low:\s+(.*?)ms', response, re.DOTALL)
upload_high = re.search('Upload:.*?high:\s+(.*?)ms', response, re.DOTALL)


jitter = re.search('Latency:.*?jitter:\s+(.*?)ms', response, re.MULTILINE)
ping_low = re.search('Latency:.*?low:\s+(.*?)ms', response, re.MULTILINE)
ping_high = re.search('Latency:.*?high:\s+(.*?)ms', response, re.MULTILINE)


print(response)

ping = ping.group(1)
ping_low = ping_low.group(1)
ping_high = ping_high.group(1)

print(ping_high)

download = download.group(1)
download_low = download_low.group(1)
download_high = download_high.group(1)
print(download)
print(download_low)

upload = upload.group(1)
upload_low = upload_low.group(1)
upload_high = upload_high.group(1)
print(upload_low)

jitter = jitter.group(1)

speed_data_Mbps = [
   {

        "measurement" : "Mbps",

        "tags" : {

            "host": "RaspiGuntiSpeedy",
            "entity_id": "download"

        },

        "fields" : {
            "value": float(download)
        }
     },
   {

        "measurement" : "Mbps",

        "tags" : {

            "host": "RaspiGuntiSpeedy",
            "entity_id": "upload"

        },

        "fields" : {
            "value": float(upload)
        }
     }
]

speed_data_ms = [

   {
        "measurement" : "ms",
        "tags" : {
            "host": "RaspiGuntiSpeedy",
            "entity_id": "ping"
        },
        "fields" : {
            "value": float(ping)
        }
     },
   {
        "measurement" : "ms",
        "tags" : {
            "host": "RaspiGuntiSpeedy",
            "entity_id": "ping_low"
        },
        "fields" : {
            "value": float(ping_low)
        }
     },
   {
        "measurement" : "ms",
        "tags" : {
            "host": "RaspiGuntiSpeedy",
            "entity_id": "ping_high"
        },
        "fields" : {
            "value": float(ping_high),
        }
     },
   {
        "measurement" : "ms",
        "tags" : {
            "host": "RaspiGuntiSpeedy",
            "entity_id": "download_low"
        },
        "fields" : {
            "value": float(download_low),
        }
     },
   {
        "measurement" : "ms",
        "tags" : {
            "host": "RaspiGuntiSpeedy",
            "entity_id": "download_high"
        },
        "fields" : {
            "value": float(download_high),
        }
     },
   {
        "measurement" : "ms",
        "tags" : {
            "host": "RaspiGuntiSpeedy",
            "entity_id": "upload_low"
        },
        "fields" : {
            "value": float(upload_low),
        }
     },
   {
        "measurement" : "ms",
        "tags" : {
            "host": "RaspiGuntiSpeedy",
            "entity_id": "upload_high"
        },
        "fields" : {
            "value": float(upload_high),
        }
     },
   {
        "measurement" : "ms",
        "tags" : {
            "host": "RaspiGuntiSpeedy",
            "entity_id": "ping"
        },
        "fields" : {
            "value": float(ping),
        }
     },
   {
        "measurement" : "ms",
        "tags" : {
            "host": "RaspiGuntiSpeedy",
            "entity_id": "ping_low"
        },
        "fields" : {
            "value": float(ping_low),
        }
     },
  {
        "measurement" : "ms",
        "tags" : {
            "host": "RaspiGuntiSpeedy",
            "entity_id": "ping_high"
        },
        "fields" : {
            "value": float(ping_high),
        }
     },

  {
        "measurement" : "ms",
        "tags" : {
            "host": "RaspiGuntiSpeedy",
            "entity_id": "jitter"
        },
        "fields" : {
            "value": float(jitter),
        }
     }



]

client = InfluxDBClient('localhost', 8086, 'speedmonitor', 'pass', 'internetspeed')

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
client.write_points(speed_data_Mbps)
client.write_points(speed_data_ms)


