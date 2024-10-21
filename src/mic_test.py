import speech_recognition as sr

from adapter.openai import OpenAIClient

# 創建一個Recognizer對象
recognizer = sr.Recognizer()

# 使用麥克風作為音源
with sr.Microphone() as source:
    print("請開始說話...")

    # 調整環境噪音水平
    recognizer.adjust_for_ambient_noise(source)

    # 錄製音頻
    audio = recognizer.listen(source)

    try:
        # 使用Google Speech Recognition將音頻轉換為文字
        print("Google語音辨識結果：")
        text = recognizer.recognize_google(
            audio, language="zh-TW"
        )  # 可以根據需要更改語言
        print(f"你說的是：{text}")
    except sr.UnknownValueError:
        print("Google Speech Recognition無法理解音頻")
    except sr.RequestError as e:
        print(f"無法從Google Speech Recognition服務請求結果；{e}")


# 創建OpenAIClient對象
openai_client = OpenAIClient()
openai_client.text_to_speech(text, "output.mp3", voice="alloy")

system_prompt = f"""
請作為一個朋友，友好地告訴對方對方的需求，並提供一些建議。如果對方沒有提到他的需求，請祝福他有好的一天
"""

ans = openai_client.get_answer(system_prompt, text)
print(f"OpenAI回答：{ans}")
openai_client.text_to_speech(ans, "output_ans.mp3", voice="alloy")