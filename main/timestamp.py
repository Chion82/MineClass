<<<<<<< HEAD
import time

def ToDateTime(UnixTimeStamp):
	format = '%Y-%m-%d %H:%M:%S'
	value = time.localtime(UnixTimeStamp)
	return time.strftime(format,value)
=======
import time

def ToDateTime(UnixTimeStamp):
	format = '%Y-%m-%d %H:%M:%S'
	value = time.localtime(UnixTimeStamp)
	return time.strftime(format,value)
>>>>>>> 62eaae239e1b1b1771d0813d39f397efa0fdca60
