Вариант работы: (4)

Протарифицировать абонента с номером 915642913 с коэффициентом k:

- 1руб/минута исходящие звонки,
- 1руб/минута входящие,
- смс - первые 5шт бесплатно, вторые 5шт 1руб/шт, после 10 - 2руб/шт

Протарифицировать абонента с IP-адресом 192.168.250.59 с коэффициентом k:

- 0,5руб/Кб до достижения 500Кб
- далее 1руб/Кб

How to run:

- open terminal
- write: py
- write: import create_bill
- to create pdf bill file: create_bill.pdf('915642913','192.168.250.59')

Note:

- programme need 2 addition modules: comtypes and python-docx
- to install comtypes module: py -m pip install -U comtypes
- to install python-docx module: py -m pip install -U python-docx
