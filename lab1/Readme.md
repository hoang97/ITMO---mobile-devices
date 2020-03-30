Варианты работы: (1)

Протарифицировать абонента с номером 915783624 с коэффициентом k: 
  - 2руб/минута исходящие звонки, 
  - 0руб/минута входящие, 
  - смс - первые 10шт бесплатно, далее 1руб/шт
  
how to run:
- open terminal
- write: py 
- write: import invoice,billing
- to see all details of client 915783624 with fiels:
  write: invoice.insertData('915783624')
- to see call_invoices,sms_invoices:
  write: billing.invoices('915783624')
