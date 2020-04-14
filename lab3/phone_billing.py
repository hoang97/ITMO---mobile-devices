import phone_invoice
def invoices(phoneNum):
    fiels,data = phone_invoice.insertData(phoneNum)
    origin = fiels.index('msisdn_origin')
    dest = fiels.index('msisdn_dest')
    call = fiels.index('call_duration')
    sms = fiels.index('sms_number')
    call_out_coef = 1
    call_in_coef = 1
    call_free = 0
    sms_free = 5
    call_out_duration = 0
    call_in_duration = 0
    sms_number = 0
    for row in data:
        if row[origin] == phoneNum:
            call_out_duration += float(row[call])
            sms_number += float(row[sms])
        if row[dest] == phoneNum:
            call_in_duration += float(row[call])
    call_invoices = max(0,(call_out_duration-call_free)*call_out_coef+call_in_duration*call_in_coef)
    sms_invoices = max(0,(sms_number-sms_free)*1) + max(0,(sms_number-10)*1)
    return call_invoices,sms_invoices
