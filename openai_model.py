import openai

class OpenAIModel:
    model_path: str
    engine: str = ""
    use_azure: bool = False
    timeout: int = 60
    temperature: float = 1

    def load(self):
        openai.api_key = "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"
        # openai.api_key = "sk-proj-dvhW7f2JAWx0ovDsb89nT3BlbkFJn1L7bv90yM0ypwiJpHfz"
        self.engine = "gpt-4o-mini"

    def run(self, prompt: str) -> str:
        self.load()
        output = ""
        error_message = "The response was filtered"

        while not output:
            try:
                key = "engine" if self.use_azure else "model"
                kwargs = {key: self.engine}
                response = openai.ChatCompletion.create(
                    messages=[{"role": "user", "content": prompt}],
                    timeout=self.timeout,
                    request_timeout=self.timeout,
                    temperature=1,
                    **kwargs,
                )
                if response.choices[0].finish_reason == "content_filter":
                    raise ValueError(error_message)
                output = response.choices[0].message.content
            except Exception as e:
                print(e)
                if error_message in str(e):
                    output = error_message

            if not output:
                print("OpenAIModel request failed, retrying.")

        return output