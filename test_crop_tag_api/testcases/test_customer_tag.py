import pytest
import requests

from test_crop_tag_api.req_page.tag_api_method import TagGeneral

"""
管理企业标签
  |--1、获取企业标签库
  |--2、添加企业客户标签
  |--3、编辑企业客户标签
  |--4、删除企业客户标签
"""


class TestCustomerTag:
    # 数据清洗操作，即添加数据之前删除所有的数据
    def setup_class(self):
        self.tg = TagGeneral()
        self.token = self.tg.get_token()

    def teardown_class(self):
        pass

    def test_tags_list(self):
        """测试获取企业标签库"""
        res = self.tg.query_tag_lists()
        assert res.json()['errcode'] == 0

    def test_tags_add(self):
        """
        增加添加企业客户标签
        如何保证添加的数据的唯一性
        （1）加上时间戳保证测试数据的唯一性；
        （2）维护可重复使用的测试数据；
        """
        group_name = '测试1'
        tag_name = '小小鑫1'
        res = self.tg.tags_add(group_name, tag_name)
        assert res.json()['errmsg'] == 'ok'

    @pytest.mark.parametrize('tag_name', ['del_tag', '星仔', '-*', '123'])
    def test_delete_tags(self, tag_name):
        """
        1、删除之前先进性添加标签组和标签名称，进行断言，目的保证测试用例的唯一性；
        2、删除之后进行查询标签组是否存在，并进行断言；
        3、参数化，添加不同数据类型的标签名称；
        :return:
        """
        self.tg.tags_add('del', tag_name)
        res = self.tg.query_tag_lists()
        tag_id = [tag['id'] for group in res.json()['tag_group'] for tag in
                  group['tag'] if tag['name'] == tag_name]
        assert len(tag_id) == 1
        self.tg.tags_delete(tag_id)
        res = self.tg.query_tag_lists()
        tag_id = [tag['id'] for group in res.json()['tag_group'] for tag in
                  group['tag'] if tag['name'] == tag_name]
        assert len(tag_id) == 0
