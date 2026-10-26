from ordenacao import bubble_sort


def test_lista_desordenada():
    assert bubble_sort([5, 3, 8, 1, 2]) == [1, 2, 3, 5, 8]


def test_lista_ja_ordenada():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_lista_invertida():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_lista_vazia():
    assert bubble_sort([]) == []


def test_um_elemento():
    assert bubble_sort([7]) == [7]


def test_numeros_repetidos():
    assert bubble_sort([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]


def test_numeros_negativos():
    assert bubble_sort([-2, 5, 0, -7, 3]) == [-7, -2, 0, 3, 5]


def test_strings():
    assert bubble_sort(["banana", "abacaxi", "uva"]) == ["abacaxi", "banana", "uva"]


def test_igual_sorted():
    lista = [9, 4, 6, 1, 8, 2, 7, 3, 5]
    assert bubble_sort(lista.copy()) == sorted(lista)


if __name__ == "__main__":
    for nome, teste in list(globals().items()):
        if nome.startswith("test_"):
            teste()
    print("ok")
