def dict_int_tuple_str_str_equals(obj1: dict[int, (str, str)], obj2: dict[int, (str, str)]) -> bool:
    if len(obj1.keys()) == len(obj2.keys()):
        for obj1_key, obj1_val in obj1.items():
            if obj1_val != obj2.get(obj1_key):
                return False
        return True
    return False

def dict_int_tuple_str_str_hash(obj: dict[int, (str, str)]) -> int:
    return hash(
        tuple(
            [
                (order, name, value)
                for order, (name, value)
                in obj.items()
            ]
        )
    )

def dict_int_tuple_str_str_str(
        obj: dict[int, (str, str)],
        values_only: bool =False,
        preserve_insertion_order: bool=False) -> str:
    keys = [k for k in obj.keys()]

    if not preserve_insertion_order:
        keys.sort(reverse=True)

    lines = []
    for key in keys:
        lines.append(obj.get(key))

    return "\n".join(
        [
            f'{value}' for _, value in lines
        ]
        if values_only
        else
        [
            f'{name}: {value}' for name, value in lines
        ]
    )

def list_eq(l1: list, l2: list, ignore_order=False) -> bool:
    if l1 is None or l2 is None or len(l1) != len(l2):
        return False

    if ignore_order:
        l1.sort()
        l2.sort()

    for i, l1_item in enumerate(l1):
        if l1_item != l2[i]:
            return False

    return True
