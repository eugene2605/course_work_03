from src.utils import get_operations, get_filtered_operations, get_sorted_operations, get_formatted_operations


def test_get_operations():
    assert isinstance(get_operations(), list)


def test_get_filtered_operations():
    assert len(get_filtered_operations([{"state": "EXECUTED"}, {"state": "CANCELED"}, {"state": "EXECUTED"}])) == 2


def test_get_sorted_operations():
    assert get_sorted_operations([{"date": "2018-10-14T08:21:33.419441"}, {"date": "2020-10-14T08:21:33.419441"}, {"date": "2019-10-14T08:21:33.419441"}]) == [{"date": "2020-10-14T08:21:33.419441"}, {"date": "2019-10-14T08:21:33.419441"}, {"date": "2018-10-14T08:21:33.419441"}]


def test_get_formatted_operations():
    a = [{
        "id": 596171168,
        "state": "EXECUTED",
        "date": "2018-07-11T02:26:18.671407",
        "operationAmount": {
            "amount": "79931.03",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 72082042523231456215"
    }]
    assert get_formatted_operations(a) == ["11.07.2018 Открытие вклада\nСчет ****************6215\n79931.03 руб.\n"]

    b = [{
        "id": 596171168,
        "state": "EXECUTED",
        "date": "2018-07-11T02:26:18.671407",
        "operationAmount": {
            "amount": "79931.03",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "from": "Visa Gold 5999414228426353",
        "to": "Счет 72082042523231456215"
    }]
    assert get_formatted_operations(b) == ["11.07.2018 Открытие вклада\nVisa Gold 5999 41** **** 6353 -> Счет ****************6215\n79931.03 руб.\n"]

    c = [{
        "id": 596171168,
        "state": "EXECUTED",
        "date": "2018-07-11T02:26:18.671407",
        "operationAmount": {
            "amount": "79931.03",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "from": "Счет 27248529432547658655",
        "to": "Счет 72082042523231456215"
    }]
    assert get_formatted_operations(c) == ["11.07.2018 Открытие вклада\nСчет ****************8655 -> Счет ****************6215\n79931.03 руб.\n"]


