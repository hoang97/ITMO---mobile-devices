Варианты работы: (4)

Протарифицировать абонента с номером 915642913 с коэффициентом k: 
  - 1руб/минута исходящие звонки, 
  - 1руб/минута входящие, 
  - смс - первые 5шт бесплатно, вторые 5шт 1руб/шт, после 10 - 2руб/шт
  
how to run:
- open terminal
- write: py 
- write: import invoice,billing
- to see all details of client 915642913 with fiels:
  write: invoice.insertData('915642913')
- to see call_invoices,sms_invoices:
  write: billing.invoices('915642913')
