from revChatGPT.revChatGPT import Chatbot
import json

# Get your config in JSON
config = {
        "Authorization": "STwpk30JGxuogPQI3hPwJEi2Y3_suGFuYIm37A1FzQzslp"
    }

chatbot = Chatbot(config, conversation_id=None)
prompt = "How are you?"
response = chatbot.get_chat_response(prompt)
print(response["message"])
print(response["conversation_id"])
print(response["parent_id"])