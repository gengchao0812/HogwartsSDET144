import pytest
#conftest固定名,并且被测包要有__init__.py文件
#session跨模块执行一次  module为模块级别，每个模块执行一次
@pytest.fixture(scope="session")
def open():
    print("跨模块只执行一次")
    yield

    print("恭喜，到这里就都执行完了")
