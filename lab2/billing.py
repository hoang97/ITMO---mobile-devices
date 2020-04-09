import invoice
def invoices(IpNum):
    _,data = invoice.insertData(IpNum)
    origin = 0
    dest = 1
    byte = 2
    internet_free = 0
    internet_low = 500
    internet_coeff = 0.5
    total_amount = 0
    for row in data:
        a = row[origin].split()[0]
        if a == IpNum:
            b = row[dest].split()[0]
            c = row[byte].split()[0]
            total_amount += float(c)
    total_amount /= pow(2,10)
    internet_invoice = max(0,(total_amount-internet_free)*internet_coeff) + max(0,(total_amount-internet_low)*internet_coeff)
    return internet_invoice