<<<<<<< HEAD
from django.utils.http import urlquote,urlunquote
import hashlib

def EscapeContent(text):
	if (text==None):
		return None
	text = text.replace(" ","&nbsp;")
	text = text.replace("\n","<br />")
	text = text.replace('"',"&quot;")
	text = text.replace("&","&amp;")
	text = text.replace("<","&lt;")
	text = text.replace(">","&gt;")
	return text

def QuoteEscapeContent(text):
	if (text==None):
		return None
	text = text.replace(" ","&nbsp;")
	text = text.replace("\n","<br />")
	text = text.replace('"',"&quot;")
	text = text.replace("&","&amp;")
	text = text.replace("<","&lt;")
	text = text.replace(">","&gt;")
	return urlquote(text)

def md5(src):
	myMd5 = hashlib.md5()
	myMd5.update(src.encode("utf-8"))
=======
from django.utils.http import urlquote,urlunquote
import hashlib

def EscapeContent(text):
	if (text==None):
		return None
	text = text.replace(" ","&nbsp;")
	text = text.replace("\n","<br />")
	text = text.replace('"',"&quot;")
	text = text.replace("&","&amp;")
	text = text.replace("<","&lt;")
	text = text.replace(">","&gt;")
	return text

def QuoteEscapeContent(text):
	if (text==None):
		return None
	text = text.replace(" ","&nbsp;")
	text = text.replace("\n","<br />")
	text = text.replace('"',"&quot;")
	text = text.replace("&","&amp;")
	text = text.replace("<","&lt;")
	text = text.replace(">","&gt;")
	return urlquote(text)

def md5(src):
	myMd5 = hashlib.md5()
	myMd5.update(src.encode("utf-8"))
>>>>>>> 62eaae239e1b1b1771d0813d39f397efa0fdca60
	return myMd5.hexdigest()