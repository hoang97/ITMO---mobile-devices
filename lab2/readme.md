Варианты работы: (4)

Протарифицировать абонента с IP-адресом 192.168.250.59 с коэффициентом k: 

- 0,5руб/Кб до достижения 500Кб
- далее 1руб/Кб

How to run:

- open terminal
- write: nfdump -r nfcapd.202002251200 -o "fmt:%sa,%da,%byt,%ts,%te" >> data1.txt
- write: py
- write: import plotGraphic,billing
- to see graphic of user's traffic: plotGraphic.show('192.168.250.59')
- to see internet_invoices: billing.invoices('192.168.250.59')

Note:

If you haven't installed pyplot for python, follow these instruction for installing:

- open terminal
- write: py -m pip install -U pip
- write: py -m pip install -U matplotlib
