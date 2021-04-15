"""Send a reply from the proxy without sending any data to the remote server."""
from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    if "baidu" in flow.request.pretty_url:
        flow.response = http.HTTPResponse.make(
            200,  # (optional) status code
            b"xinzai",  # (optional) content
            {"Content-Type": "text/html"}  # (optional) headers
        )
