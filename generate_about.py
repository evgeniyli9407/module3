# coding: utf-8

from horoscope import generate_prophecies
from datetime import datetime as dt

def generate_page(head, body):
	page = f"<html>{head}{body}</html>"
	return page

def generate_head(title):
	head = f"""<head>
	<meta charset='utf-8'>
	<title>{title}</title>
	</head>
	"""
	return head

def generate_body(header):
	body = f"<h1>{header}</h1>"

	return f"<body>{body}<ol><li>Времена дня:<ul><li>Утром</li><li>Вечером</li></ul></li><li>Глаголы:<ul><li>Oстерегайтесь</li><li>ожидайте</li></ul></li></ol><img src = ""horo.jpg""><a href = index.html> На главную</a></body>"

def save_page(title, header, output="about.html"):
	fp = open(output, "w", encoding="utf-8")
	today = dt.now().date()
	page = generate_page(
		head=generate_head(title),
		body=generate_body(header=header)
	)
	print(page, file=fp)
	fp.close()


#####################

today = dt.now().date()

save_page(
	title="Суть гороскопа",
	header="О чём всё это"
)