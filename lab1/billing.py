import invoice
def invoices(phoneNum):
    fiels,data = invoice.insertData(phoneNum)
    origin = fiels.index('msisdn_origin')
    dest = fiels.index('msisdn_dest')
    call = fiels.index('call_duration')
    sms = fiels.index('sms_number')
    call_free = 0
    sms_free = 10
    call_duration = 0
    sms_number = 0
    for row in data:
        if row[origin] == phoneNum:
            call_duration += float(row[call])
            sms_number += float(row[sms])
    call_invoices = max(0,(call_duration-call_free)*2)
    sms_invoices = max(0,(sms_number-sms_free)*1)
    return call_invoices,sms_invoices
