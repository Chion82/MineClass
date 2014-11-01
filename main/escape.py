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

def QuoteContent(text):
	if (text==None):
		return None
	text = text.replace("<script","&lt;script")
	text = text.replace("javascript:","java script:")
	return urlquote(text)

def md5(src):
	myMd5 = hashlib.md5()
	myMd5.update(src.encode("utf-8"))
	return myMd5.hexdigest()