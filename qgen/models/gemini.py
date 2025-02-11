import google.generativeai as genai
import logging
import time

logger = logging.getLogger(__name__)


class Gemini:
    def __init__(
        self,
        model_name: str = "gemini-1.5-flash",
        api_key: None | str = None,
        wait_time: float = 1.0,
        max_retry: int = 5,
    ) -> None:
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)
        logger.info(f"Created client for `{model_name}`")
        self.wait_time = wait_time
        self.max_retry = max_retry

    def generate(
        self,
        prompt,
        max_tokens: int = 32,
        temperature: float = 1.0,
        top_p: float = 1.0,
        top_k: int = 50,
    ):
        config = genai.GenerationConfig(
            max_output_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
        )
        response = ""
        cnt = 0
        while response == "":
            try:
                res = self.model.generate_content(prompt, generation_config=config)
                response = res.text.strip()
            except Exception as err:
                logger.error(f"Unexpected error: {err}")
                try:
                    finish_reason = res.candidates[0].finish_reason.__str__()
                    logger.info(f"Empty response due to: {finish_reason}")
                    if not ("STOP" in finish_reason or "MAX_TOKENS" in finish_reason):
                        return ""
                except Exception as err:
                    pass
                cnt += 1
                if cnt == self.max_retry:
                    logger.info("Maximum retry exceeded")
                    break
                time.sleep(self.wait_time)

        if response == "":
            logger.info("Failed to generate text after retries.")
        return response


    def chat(
        self,
        prompt,
        history,
        max_tokens: int = 32,
        wait_time: float = 0,
        temperature: float = 1.0,
        top_p: float = 1.0,
        top_k: int = 50,
    ):
        config = genai.GenerationConfig(
            max_output_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
        )
        response = ""
        cnt = 0
        chat_session = self.model.start_chat(history=history)
        while response == "":
            try:
                res = chat_session.send_message(prompt, generation_config=config)
                response = res.text.strip()
            except Exception as err:
                logger.error(f"Unexpected error: {err}")
                try:
                    finish_reason = res.candidates[0].finish_reason.__str__()
                    logger.info(f"Empty response due to: {finish_reason}")
                    if not ("STOP" in finish_reason or "MAX_TOKENS" in finish_reason):
                        return ""
                except Exception as err:
                    pass
                cnt += 1
                if cnt == self.max_retry:
                    logger.info("Maximum retry exceeded")
                    break
                time.sleep(self.wait_time)

        if response == "":
            logger.info("Failed to generate text after retries.")
        return response
