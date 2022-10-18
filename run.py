import pytest
from comman import base
from config.conf import get_report_json_path, get_report_index_path



if __name__ == '__main__':
    pytest.main()
    base.allure_report(get_report_json_path(),get_report_index_path())  # 根据json文件生成html
