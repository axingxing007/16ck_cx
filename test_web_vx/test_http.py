import requests

# 使用代理
proxies = {
    'http': 'http://127.0.0.1:8888',
    'https': 'https://127.0.0.1:8888'
}


class TestHttp:

    def test_get(self):
        res = requests.get('https://httpbin.testing-studio.com/get')
        print(res.text)
        assert res.status_code == 200

    def test_post(self):
        res = requests.post(
            'https://httpbin.testing-studio.com/post',
            data={'name': 'cx'}
        )
        print(res.text)
        assert res.status_code == 200

    def test_json(self):
        res = requests.post(
            'https://httpbin.testing-studio.com/post',
            json={'name': 'cx'},
        )
        print(res.text)
        assert res.status_code == 200

    def test_files(self):
        res = requests.post(
            url='https://httpbin.testing-studio.com/post',
            files={'name': 'cx'}
        )
        print(res.text)
        assert res.status_code == 200
