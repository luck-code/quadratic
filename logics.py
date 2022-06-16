def decide(a, b, c):
    result = {}
    if b * b - 4 * a * c < 0:
        result = {}

    elif b * b - 4 * a * c == 0:
        x = -b / (2 * a)
        result['x1'] = round(x, 4)
    elif b * b - 4 * a * c > 0:
        x1 = (-b - ((b * b - 4 * a * c) ** (0.5))) / (2 * a)
        x2 = (-b + ((b * b - 4 * a * c) ** (0.5))) / (2 * a)
        result['x1'] = round(x1, 4)
        result['x2'] = round(x2, 4)

    print(result)
    return result


def description(a, b, c, x1, x2):
    if x1 and x2:
        description_result = f'При введенных коэффициентах А={a}, B={b}, C={c} ' \
                             f'уравнение имеет два корня: х1 = ' \
                             f'{x1}, x2 = ' \
                             f'{x2}'
    elif x1:
        description_result = f'При введенных коэффициентах А={a}, B={b}, C={c} уравнение имеет один корень: x = {x1}'
    else:
        description_result = f'При введенных коэффициентах А={a}, B={b}, C={c} уравнение не имеет решений'
    return description_result
