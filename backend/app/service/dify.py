import httpx
import logging
from app.models.dify import PromptRequest, PromptResponse, DifyResponse
import uuid


class DifyService:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url
        self._client = None

    @property
    async def client(self) -> httpx.AsyncClient:
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient()
        return self._client

    async def optimize_prompt(self, request: PromptRequest) -> PromptResponse:
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            request_data = {
                "inputs": {
                    "background": request.background,
                    "role": request.role,
                    "expectation": request.expectation
                },
                "response_mode": "blocking",  # 使用阻塞模式
                "user": str(uuid.uuid4())  # 生成唯一用户标识
            }

            logging.info(f"Sending request to Dify API: {request_data}")
            
            try:
                client = await self.client
                resp = await client.post(
                    url=f"{self.base_url}/workflows/run",
                    headers=headers,
                    json=request_data,
                    timeout=30.0  # 添加超时设置
                )
            except httpx.RequestError as e:
                logging.error(f"HTTP Request failed: {str(e)}")
                raise Exception(f"Failed to send request to Dify API: {str(e)}")
            except Exception as e:
                logging.error(f"Unexpected error during HTTP request: {str(e)}")
                raise Exception(f"Unexpected error during API call: {str(e)}")

            logging.info(f"Received response with status code: {resp.status_code}")
            
            if resp.status_code == 200:
                try:
                    response_json = resp.json()
                    logging.debug(f"Response JSON: {response_json}")
                    dify_response = DifyResponse.model_validate(response_json)
                    return PromptResponse.from_dify_response(dify_response)
                except ValueError as e:
                    logging.error(f"JSON parsing error: {str(e)}")
                    raise Exception(f"Failed to parse API response: {str(e)}")
                except Exception as validation_error:
                    logging.error(f"Response validation error: {str(validation_error)}")
                    raise Exception(f"Failed to validate API response: {str(validation_error)}")
            else:
                error_message = f"API call failed with status {resp.status_code}"
                try:
                    error_detail = resp.json()
                    error_message += f": {error_detail}"
                except:
                    error_message += f": {resp.text}"
                logging.error(error_message)
                raise Exception(error_message)

        except Exception as e:
            logging.error(f"Error in optimize_prompt: {str(e)}", exc_info=True)
            raise Exception(f"Failed to optimize prompt: {str(e)}")

    async def close(self):
        if self._client is not None and not self._client.is_closed:
            await self._client.aclose()
            self._client = None