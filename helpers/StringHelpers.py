def str_eq_ignore_case_null_safe(str1: str, str2: str) -> bool:
    if str1 is None and str2 is None:
        return True
    if str1 is None or str2 is None:
        return False
    return str1.casefold() == str2.casefold()