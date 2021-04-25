import json

import pytest
import requests


class TestWechat:
    def test_get_token(self):
        """获取企业微信的access_token，有效期为2h
        :return: dict
        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid": "ww7656ec7a420e3ef9",
            "corpsecret": "wcmnEAZsF2sm3TjumoU4iqoHAlMmMUxMsYYXuHGa6TA"
        }
        res = requests.get(url, params=params, verify=False)
        return res.json()["access_token"]

    @pytest.mark.parametrize("tmp", range(100))
    def test_get_member(self, tmp):
        """查询会员信息接口参数化为了验证用例并行的时间
        pytest -n auto  # 用例并行执行
        pytest -n 3  # 指定3个cpu
        :param tmp:
        :return:
        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
        params = {"access_token": self.test_get_token(),
                  "userid": "ChenXin"
                  }
        res = requests.get(url, params=params, verify=False)
        print(self.pretty_json(res.json()))

    def pretty_json(self, data: dict) -> str:
        """
        对接口返回的字典类型的数据美化成json格式的字符串
        :param data: dict
        :return: str
        """
        pretty_json = json.dumps(data, ensure_ascii=False, indent=2)
        return pretty_json
