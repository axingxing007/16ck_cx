import json

import requests


class TagGeneral:
    def get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        payload = {
            'corpid': 'ww7656ec7a420e3ef9',
            'corpsecret': 'wcmnEAZsF2sm3TjumoU4im8d_W9CnIT64Xhjtc75PyQ'
        }
        res = requests.get(url=url, params=payload)
        return res.json()['access_token']

    def query_tag_lists(self):
        """封装查询企业标签库，进行复用"""
        url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list'
        payload = {
            'access_token': self.get_token()
        }
        res = requests.get(url=url, params=payload)
        return res

    def tags_add(self, group_name, tag_name):
        """
        :param group_name: 标签组的名称
        :param tag_name:   标签的名称
        :return:
        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag"
        payload = {
            'access_token': self.get_token()
        }
        data = {
            "group_name": group_name,
            "tag": [{
                "name": tag_name
            }
            ]
        }
        res = requests.post(url=url, params=payload, json=data)
        return res

    def tags_delete(self, tag_id: list):
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag"
        payload = {
            'access_token': self.get_token()
        }
        data = {
            "tag_id": tag_id,
            "group_id": [

            ]
        }
        res = requests.post(url=url, params=payload, json=data)
        return res

    def pretty_json(self, dict_obj):
        """将字典类型的对象转成json字符串并进行打印"""
        print(json.dumps(dict_obj, ensure_ascii=False, indent=2))
