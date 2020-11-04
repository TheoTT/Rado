import pytest
import requests

from ..utilse import write_excel


@pytest.fixture(scope='session')
def token_admin():
    return None


@pytest.fixture(scope='session')
def token_simple():
    return None 


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    out = yield
#    excel_file = pytest.excel_file
#    sheet_num = pytest.sheet_num
    excel_file = item.module.excel_file
    sheet_num = item.module.sheet_num
    report = out.get_result()
    case_id = report.nodeid.split('::')[-1]
    if report.outcome == 'failed':
        result = 'FAILED'
    else:
        result = 'PASSED'
    if report.when == "call": # 默认会调用三次'setup, call, teardown'
        write_excel(case_id, result, excel_file, sheet_num)

# 需要再test_case处传入参数，加入如下代码：
# globals()['excel_file'] = 'preparedData/Dashboard_yl.xls' # 参考https://www.coder.work/article/4984403
# globals()['sheet_num'] = 0
# test_datas, ids = get_test_data_from_excel(excel_file, sheet_num)
# ...
