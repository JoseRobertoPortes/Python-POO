import locale


def Real(num):
    try:
        locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
    except locale.Error:
        try:
            locale.setlocale(locale.LC_ALL, "pt_BR")  
        except locale.Error:
            locale.setlocale(locale.LC_ALL, "")

    try:
        if isinstance(num, str):
            num = num.strip().replace(",", ".")
        num_float = float(num)
    except (ValueError, TypeError):
        
        return "R$ 0,00"
    return locale.currency(num_float, grouping=True)  
