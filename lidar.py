from rplidar import RPLidar


lidar = RPLidar('/dev/ttyUSB0')

#health of the Lidar because why not
health = lidar.get_health()
info = lidar.get_info()

print(info)

# for i, scan in enumerate(lidar.iter_scans()):
#   print('%d: Got %d measurments' % (i, len(scan)))
#   if i > 10:
#    break