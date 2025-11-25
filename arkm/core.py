from arkm.utils import make_payload
import time
from typing import Dict
class BaseArkmClient:
    """Arkm API 客户端基类"""

    BASE_URL = "https://api.arkm.com"
    SALT = "gh67j345kl6hj5k432"

    def __init__(self, cookie: str):
        self.cookie = cookie

    def _build_headers(self, path: str) -> Dict[str, str]:
        """构建请求头"""
        ts = str(int(time.time()))
        payload = make_payload(path, self.SALT, ts)

        return {
            "accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "origin": "https://intel.arkm.com",
            "referer": "https://intel.arkm.com/",
            "sec-ch-ua": '"Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0",
            "x-timestamp": ts,
            "x-payload": payload,
            "cookie": self.cookie
        }
