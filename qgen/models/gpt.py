import logging
from openai import OpenAI
import time

logger = logging.getLogger(__name__)


class GPT:
    def __init__(
        self,
        model_name: str = "",
        api_type="",
        base_url: str = "",
        api_key: str = "",
        wait_time: float = 1.0,
        max_retry: int = 5,
    ) -> None:
        if api_type == "openai":
            self.client = OpenAI(api_key)
        else:
            self.client = OpenAI(base_url=base_url, api_key=api_key)
        self.model = model_name
        self.wait_time = wait_time
        self.max_retry = max_retry

    def generate(
        self,
        messages: list[dict[str, str]],
        max_tokens: int = 32,
        temperature: float = 1.0,
        top_p: float = 1.0,
    ):
        response = ""
        cnt = 0
        while response == "":
            try:
                res = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=messages,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    top_p=top_p,
                    # top_k=top_k,
                )
                if res.choices:
                    response = res.choices[0].message.content.strip()
                    logger.debug(f"Retrieved response from model:{response}")
                    return response
            except Exception as err:
                logger.error(f"Unexpected error: {err}")
                cnt += 1
                if cnt == self.max_retry:
                    logger.info("Maximum retry exceeded")
                    break
                if self.wait_time > 0:
                    time.sleep(self.wait_time)

        if response == "":
            logger.info("Failed to generate text after retries.")
        return response
