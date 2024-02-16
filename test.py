import subprocess
import pytest
from hello import hello
from python_if_else import python_if_else
from arithmetic_operators import arithmetic_operators
from division import division
from loops import loops
from print_function import print_function
from second_score import second_score
from nested_list import nested_list
from max_word import max_word



# INTERPRETER = 'python3'

# def run_script(filename, input_data=None):
#     proc = subprocess.run(
#         [INTERPRETER, filename],
#         input='\n'.join(input_data if input_data else []),
#         capture_output=True,
#         text=True,
#         check=False
#     )
#     return proc.stdout.strip()
 
# test_dt = ["Hello, World!", "Hello, World!", "Hello, World!", "Hello, World!", "Hello, World!", "Hello, World!", "Hello, World!", "Hello, World!"]
# # база тестов hello == Hello, World!

# def helloqwe(itm: str):
#     assert hello() == itm
# ## инциализация функции теста    
# def test_qweqwe():
#     for i in range(len(test_dt)):
#         helloqwe(test_dt[i])
# ## перебор тестов. Закидываем в функции 1 тест 













# data_if= [3, 4, 18, 22]
# exitdata_if = ["Weird", "Not Weird", "Weird", "Not Weird"]
# def python_if_else_2(n: int, test):
#     assert python_if_else(n) == test


# def test_python_if_else():
#     for i in data_if:
#         for j in exitdata_if:
#             python_if_else_2(i, j)

test_data = {
    'python_if_else':[
        (1, 'Weird'),
        (4, 'Not Weird'),
        (3, 'Weird'),
        (6,'Weird'),
        (22, 'Not Weird'),
    ],
    'arithmetic_operators':[
        ([1, 2], [3, -1, 2]),
        ([10, 5], [15, 5, 50]),
        ([3, 5], [8, -2, 15]),
    ],
    'division': [
        ([3, 5], [0, 0.6]),
        ([2, 4], [0, 0.5]),
        ([2, 0], "Division by zero"),
    ],
    'loops': [
        ([3], [0, 1, 4]),
        ([4], [0, 1, 4, 9]),
        ([5], [0, 1, 4, 9, 16]),
    ],
    'print_function': [
        ([3],[0, 1, 2, 3]),
        ([4],[0, 1, 2, 3, 4],),
        ([5],[0, 1, 2, 3, 4, 5]),
    ],
    'second_score': [
        ([2, 3, 4, 5, 6],[5]),
        ([1, 1, 3, 7, 2],[3]),
        ([6, 1, 7, 2, 3],[6]),
        ],
    'nested_list': [
        ({5: {
            'Гарри': 37.21,
            'Берри': 37.21,
            'Тина' : 37.2,
            'Акрити' : 41,
            'Харш' : 39,
            }}),
    ],
    'max_word': [
        
    ]
}


@pytest.mark.parametrize("input_data, expected", test_data['arithmetic_operators'])
def test_arithmetic_operators(input_data, expected):
    assert arithmetic_operators(input_data[0], input_data[1]) == expected
    
@pytest.mark.parametrize("input_data, expected", test_data['python_if_else'])
def test_python_if_else(input_data, expected):
    assert python_if_else(input_data) == expected
    
@pytest.mark.parametrize("input_data, expected", test_data['division'])
def test_division(input_data, expected):
    assert division(input_data[0], input_data[1]) == expected
    
@pytest.mark.parametrize("input_data, expected", test_data['loops'])
def test_loops(input_data, expected):
    assert loops(input_data[0], input_data[1]) == expected

@pytest.mark.parametrize("input_data, expected", test_data['print_function'])
def test_print_function(input_data, expected):
    assert print_function(input_data[0], input_data[1]) == expected
    
@pytest.mark.parametrize("input_data, expected", test_data['second_score'])
def test_second_score(input_data, expected):
    assert second_score(input_data[0], input_data[1]) == expected
    
@pytest.mark.parametrize("input_data, expected", test_data['nested_list'])
def test_nested_list(input_data, expected):
    assert nested_list(input_data[0], input_data[1]) == expected
    
@pytest.mark.parametrize("input_data, expected", test_data['max_word'])
def test_max_word(input_data, expected):
    assert max_word(input_data[0], input_data[1]) == expected


    
# data_operators= [3, 5]
# exitdata_operators= [8, -2, 15]
# def test_arithmetic_operators(a,b: int, test):
#     assert arithmetic_operators(a,b) == test

# def arithmetic_operators_2():
#     for i in data_operators:
#         for j in exitdata_operators:
#             python_if_else_2(i, j)




# data_division= [3, 5]
# exitdata_division=[0, 0.6]
# def division_2():
#     assert division() == test 
    
# def division_2():
#     for i in data_division:
#         for j in exitdata_division:
#             division_2(i,j)













# @pytest.mark.parametrize("input_data, expected", test_data['python_if_else'])
# def test_python_if_else(input_data, expected):
#     assert run_script('python_if_else.py', [input_data]) == expected

# @pytest.mark.parametrize("input_data, expected", test_data['arithmetic_operators'])
# def test_arithmetic_operators(input_data, expected):
#     assert run_script('arithmetic_operators.py', input_data).split('\n') == expected
