def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    new_dict_phones = {'UA':[], 'JP':[], 'TW':[], 'SG':[]}
    for phone in list_phones:
        phone = sanitize_phone_number(phone)
        if phone.isdigit():
            if phone[:3] == "380":
                new_dict_phones["UA"].append(phone)
            elif phone[:2] == "81":
                new_dict_phones["JP"].append(phone)
            elif phone[:2] == "65":
                new_dict_phones["SG"].append(phone)
            elif phone[:3] == "886":
                new_dict_phones["TW"].append(phone)
            else:
                new_dict_phones["UA"].append(phone)
        
    return new_dict_phones