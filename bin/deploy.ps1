

# create destination folder
# copy code into folder
# copy cron config to apprpriate destination
$ip_address = '192.168.9.191'
get-content .\requirements.txt | ForEach-Object{
    $library = $_
    $cmd = "/usr/bin/pip install $library"
    ssh pi@$ip_address $cmd
}

# login and create folder
ssh pi@$ip_address mkdir -p 'flightwatch'

# copy src files
scp src/* pi@${ip_address}:/home/pi/flightwatch

ssh pi@$ip_address "echo '0 12 * * * /usr/bin/python3 /home/pi/flightwatch/scheduler.py' | /usr/bin/crontab -"