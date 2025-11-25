import aiohttp
from typing import Optional, Dict, Any
from urllib.parse import urljoin

from arkm.core import BaseArkmClient

class AsyncArkmClient(BaseArkmClient):
    """异步 Arkm API 客户端"""

    def __init__(self, cookie: str):
        super().__init__(cookie)
        self.session: Optional[aiohttp.ClientSession] = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

    async def request(
            self,
            method: str,
            path: str,
            params: Optional[Dict] = None,
            data: Optional[Dict] = None,
            **kwargs
    ) -> Dict[str, Any]:
        """
        发起异步请求

        Args:
            method: HTTP 方法 (GET, POST, etc.)
            path: API 路径
            params: 查询参数
            data: 请求体数据
            **kwargs: 其他传递给 aiohttp 的参数

        Returns:
            解析后的 JSON 响应
        """
        if not self.session:
            self.session = aiohttp.ClientSession()

        url = urljoin(self.BASE_URL, path)
        headers = self._build_headers(path)

        # 处理请求参数
        request_kwargs = {
            "params": params,
            "headers": headers,
            "timeout": aiohttp.ClientTimeout(total=10),
            **kwargs
        }

        if data is not None:
            request_kwargs["json"] = data

        async with self.session.request(method, url, **request_kwargs) as response:
            response.raise_for_status()
            return await response.json()

    async def get(self, path: str, params: Optional[Dict] = None, **kwargs) -> Dict[str, Any]:
        """发起异步 GET 请求"""
        return await self.request("GET", path, params=params, **kwargs)

    async def post(self, path: str, data: Optional[Dict] = None, **kwargs) -> Dict[str, Any]:
        """发起异步 POST 请求"""
        return await self.request("POST", path, data=data, **kwargs)
