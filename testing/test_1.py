#测试文件
from pythononcode.calc import Calculator
import pytest
import yaml
# import sys
# import os
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)

test_data = []
#-m 加标签
def setup_function():
    print("setup_function开始计算")

def teardown_function():
    print("teardown_function计算结束")
#加法
@pytest.mark.parametrize("first,second,end1",[(1,2,3),(0,-1,-1),(-1,-2,-3),(1.1,-1,0.1)])
def test_sub(open,first,second,end1):
    cal = Calculator()
    print(f'计算{first}+{second}是否等于{end1}')
    assert end1 == cal.add(first,second)


#yaml一直调不通，must be equal to the number of values (1):
# @pytest.mark.parametrize("first,second,end1",yaml.safe_load(open("add.yml")))
# def test_sub(open,first,second,end1):
#     cal = Calculator()
#     print(f'计算{first}+{second}是否等于{end1}')
#     assert end1 == cal.add(first,second)

#减法
@pytest.mark.parametrize("first,second,end1",[(4.1,1,3.1),(4,5,-1),(-1,-5,4),(0,2,-2)])
def test_sub(open,first,second,end1):
    cal = Calculator()
    print(f'计算{first}-{second}是否等于{end1}')
    assert end1 == cal.sub(first,second)

#除法
@pytest.mark.parametrize("first,second,end1",[(20,4,5),(0,1.1,0),(-1,2,-0.5),(1,0,1)])
def test_sub(open,first,second,end1):
    cal = Calculator()
    print(f'计算{first}/{second}是否等于{end1}')
    assert end1 == cal.div(first,second)

#乘法
@pytest.mark.parametrize("first,second,end1",[(5,4,20),(2.5,1.0,2.5),(-1,0,0),(-1,2,-2)])
def test_sub(open,first,second,end1):
    cal = Calculator()
    print(f'计算{first}*{second}是否等于{end1}')
    assert end1 == cal.mul(first,second)