from rplidar import RPLidar


lidar = RPLidar('/dev/ttyUSB0')

#health of the Lidar because why not
health = lidar.get_health()
info = lidar.get_info()

