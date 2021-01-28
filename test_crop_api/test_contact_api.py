import requests


class TestContact:
    _url = "https://qyapi.weixin.qq.com"

    def test_get_contact_token(self):
        """
        获取通讯录token，token失效时间为2h
        :return: str
        """
        path = "/cgi-bin/gettoken"
        payload = {
            "corpid": 'ww7656ec7a420e3ef9',
            "corpsecret": '_ClGki10rdYFEGFLJ2ZG0noOH9pt9vIQJILlR7jQ0bU'
        }
        res = requests.get(url=self._url + path, params=payload)
        return res.json()['access_token']

    def test_create_member(self):
        """
        创建成员
        :return:
        """
        payload = {'access_token': self.test_get_contact_token()}
        path = "/cgi-bin/user/create"
        data = {
            'userid': 'cx008',
            'name': '小小秋',
            'department': [1],
            'mobile': '18652992813'
        }
        res = requests.post(url=self._url + path, params=payload, json=data)
        print(res.json())

    def test_read_member(self):
        """
        读取成员
        :return:
        """
        path = '/cgi-bin/user/get'
        payload = {
            'access_token': self.test_get_contact_token(),
            'userid': 'cx008'
        }
        res = requests.get(url=self._url + path, params=payload)
        print(res.json())

    def test_update_member(self):
        """
        更新成员
        :return:
        """
        payload = {'access_token': self.test_get_contact_token()}
        path = '/cgi-bin/user/update'
        data = {
            'userid': 'cx008',
            'name': 'zzx'
        }
        res = requests.post(url=self._url + path, params=payload, json=data)
        print(res.json())

    def test_delete_member(self):
        """
        删除成员
        :return:
        """
        path = "/cgi-bin/user/delete"
        payload = {
            'access_token': self.test_get_contact_token(),
            'userid': 'cx008'
        }
        res = requests.get(url=self._url + path, params=payload)
        print(res.json())
