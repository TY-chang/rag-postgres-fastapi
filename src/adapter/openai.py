from typing import List

from openai import OpenAI

from settings import OPENAI_API_KEY


class OpenAIClient:
    def __init__(
        self,
    ):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def get_embedding(
        self, text: str, model: str = "text-embedding-3-large"
    ) -> List[float]:
        """
        Get the embedding for a given text using OpenAI's API.

        :param text: The text to embed
        :return: A list of floats representing the embedding
        """
        text = text.replace("\n", " ")
        response = (
            self.client.embeddings.create(input=[text], model=model).data[0].embedding
        )
        return response

    def get_answer(self, system_prompt: str, user_prompt: str) -> str:
        ans = (
            self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
            )
            .choices[0]
            .message.content
        )
        return ans

    def text_to_speech(self, text: str, output_path: str, **kwargs) -> str:
        """
        Convert text to speech using OpenAI's API.

        :param text: The text to convert to speech
        :return: The URL of the generated speech
        """
        response = self.client.audio.speech.create(
            model=kwargs.get("model", "tts-1"),
            voice=kwargs.get("voice", "alloy"),
            input=text,
        )
        response.stream_to_file(output_path)
        return
