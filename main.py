#!/usr/bin/python2

combo_start = '29.2.2019'


import requests
import datetime
from time import sleep

sleep(300)

while 1:
    budget_id_fd = open('budget-id', 'r')
    budget_id = budget_id_fd.read().strip('\n')
    budget_id_fd.close()

    token_fd = open('token', 'r')
    token = token_fd.read().strip('\n')
    token_fd.close()

    endpoint = 'https://api.youneedabudget.com/v1/budgets/' + budget_id + '/accounts'
    headers = {'Authorization': 'Bearer ' + token}

    data_table = requests.get(endpoint, headers=headers).text.split('"balance":')

    balance = 0.0

    for cell in data_table:
        try:
            balance = balance + float(cell.split(',')[0]) / 1000
        except:
            pass

    html_file = open('/usr/share/nginx/html/index.html', 'w')
    html_file.write('<head><meta http-equiv="refresh" content="3600"/><style>body {  background-color: black;  font-size: 100px;  font-family: "Courier New", Courier, monospace;} #wrap { padding: 10px; text-align:center; width:100%; height:1000px; } #left { color:lime; display:inline-block; padding:30px; } #right { color:Aqua; display:inline-block; padding:30px; }</style></head><body>')
    html_file.write('<br><br><div id="wrap"><div id="left">')
    html_file.write(str(int(float((datetime.datetime.now()-datetime.datetime.strptime(combo_start, '%d.%m.%Y')).days))))
    html_file.write('d</div><div id="right">')
    html_file.write(str(int(round(balance/100)*100)))
    html_file.write('&euro;</div></body></html>')
    html_file.close()

    sleep(3600)

