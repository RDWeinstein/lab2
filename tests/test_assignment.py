from assignment import create_list, concatenate_lists, scalar_multiply

def test_create_list():
    assert create_list("apple, banana, cherry") == ["apple", "banana", "cherry"]
    assert create_list("a, b, c") == ["a", "b", "c"]

def test_concatenate_lists():
    assert concatenate_lists([1, 2], [3, 4]) == [1, 2, 3, 4]
    assert concatenate_lists([], [5, 6]) == [5, 6]

def test_scalar_multiply():
    assert scalar_multiply([1, 2, 3], 2) == [2, 4, 6]
    assert scalar_multiply([0, -1, 4], 3) == [0, -3, 12]
