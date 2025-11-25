from typing import Optional, Dict, Any
from urllib.parse import urljoin

import requests

from arkm.core import BaseArkmClient


class SyncArkmClient(BaseArkmClient):
    """同步 Arkm API 客户端"""

    def __init__(self, cookie: str):
        super().__init__(cookie)
        self.session = requests.Session()

    def request(
            self,
            method: str,
            path: str,
            params: Optional[Dict] = None,
            data: Optional[Dict] = None,
            **kwargs
    ) -> Dict[str, Any]:
        """
        发起同步请求

        Args:
            method: HTTP 方法 (GET, POST, etc.)
            path: API 路径
            params: 查询参数
            data: 请求体数据
            **kwargs: 其他传递给 requests 的参数

        Returns:
            解析后的 JSON 响应
        """
        url = urljoin(self.BASE_URL, path)
        headers = self._build_headers(path)

        response = self.session.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=data,
            timeout=10,
            **kwargs
        )

        response.raise_for_status()
        return response.json()

    def get(self, path: str, params: Optional[Dict] = None, **kwargs) -> Dict[str, Any]:
        """发起 GET 请求"""
        return self.request("GET", path, params=params, **kwargs)

    def post(self, path: str, data: Optional[Dict] = None, **kwargs) -> Dict[str, Any]:
        """发起 POST 请求"""
        return self.request("POST", path, data=data, **kwargs)