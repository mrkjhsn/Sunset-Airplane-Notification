param(
    $pip=$true
    ,$apt=$true   
)

# create destination folder
# copy code into folder
# copy cron config to apprpriate destination
$ip_address = '192.168.9.191'

# login and create folder
ssh pi@$ip_address mkdir -p 'flightwatch'

# copy src files
scp src/* pi@${ip_address}:/home/pi/flightwatch

# install utilities
if ($apt) {
    ssh pi@$ip_address "sudo apt install at libatlas-base-dev"
}

# install python libraries
if ($pip) {
    $cmd = "/usr/bin/pip3 install -r ./flightwatch/requirements.txt"
    ssh pi@$ip_address $cmd
}

ssh pi@$ip_address "echo '0 12 * * * /usr/bin/python3 /home/pi/flightwatch/scheduler.py' | /usr/bin/crontab -"