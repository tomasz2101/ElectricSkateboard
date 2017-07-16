from pathlib import Path
file = Path("/home/pi/ElectricSkateboard/python/test.txt")
file.open("a").write(u"test1\n")
