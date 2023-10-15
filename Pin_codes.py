def is_valid_pin_codes(pin_codes) :
    list_audit = set(pin_codes)
    if len(list_audit) == len(pin_codes) :
        
        for pin in pin_codes :
            if type(pin) == str:
                for p in pin :
                    if len(p) == 4 and type(p) == int :
                        return True
                    else :
                        return False
                    #change
        
        
        
        
    
print(is_valid_pin_codes(['1101', '9034', '1101']))
