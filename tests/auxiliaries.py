import random


def proto_test_case(data, fct):
    for input, expected_output in data:
        # print(input, expected_output, fct(input))
        actual_output = fct(input)
        if actual_output != expected_output:
            print(f"input: {input} expected: {expected_output} got: {actual_output}")
        assert actual_output == expected_output


def random_point():
    return random.uniform(-180, 180), random.uniform(-90, 90)


def list_of_random_points(length):
    return [random_point() for _ in range(length)]


def list_equal(l1, l2):
    return False if len(l1) != len(l2) else all(i1 == i2 for i1, i2 in zip(l1, l2))


def nested_list_equal(l1, l2):
    if len(l1) != len(l2):
        return False
    first_entry = l1[0]
    if isinstance(first_entry, list):
        return all(nested_list_equal(i1, i2) for i1, i2 in zip(l1, l2))
    else:
        return list_equal(l1, l2)
