import time

def ToDateTime(UnixTimeStamp):
	format = '%Y-%m-%d %H:%M:%S'
	value = time.localtime(UnixTimeStamp)
	return time.strftime(format,value)
