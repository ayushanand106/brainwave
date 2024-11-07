import requests

class ChatSession:
    def __init__(self, api_key="", external_user_id=""):
        self.api_key = api_key
        self.external_user_id = external_user_id
        self.session_id = None
        self.base_url = 'https://api.on-demand.io/chat/v1'
        self.create_session()
        self.image_no=0
        self.document_no=0
        self.youtube_no=0

    def create_session(self):
        create_session_url = f'{self.base_url}/sessions'
        headers = {'apikey': self.api_key}
        body = {
            "pluginIds": [],
            "externalUserId": self.external_user_id
        }
        response = requests.post(create_session_url, headers=headers, json=body)
        response_data = response.json()
        self.session_id = response_data['data']['id']

    def submit_query(self, query, endpoint_id="predefined-openai-gpt4turbo", plugin_ids=None):
        if not self.session_id:
            raise ValueError("Session has not been created or has ended.")
        
        submit_query_url = f'{self.base_url}/sessions/{self.session_id}/query'
        headers = {'apikey': self.api_key}
        body = {
            "endpointId": endpoint_id,
            "query": query,
            "pluginIds": ["plugin-1712327325", "plugin-1713962163", "plugin-1723275191",
                                        "plugin-1718945102", "plugin-1717458428", "plugin-1717340460",
                                        "plugin-1713965172", "plugin-1713924030"],
            "responseMode": "sync"
        }
        query_response = requests.post(submit_query_url, headers=headers, json=body)
        query_response_data = query_response.json()
        return query_response_data["data"]["answer"]

    def upload_image(self,image):
        url = 'https://api.on-demand.io/media/v1/public/file'

        headers = {
            'Content-Type': 'application/json',
            'apikey': f'{self.api_key}'
        }
        data = {
        "createdBy":f"{self.external_user_id}",
        "updatedBy":f"{self.external_user_id}",
        "sessionId":f"{self.session_id}",
        "url":image,
        "name":f"{self.image_no}",
        "plugins":["plugin-1713958591"],
        "sizeBytes":7834093,
        "responseMode":"sync"
        
        }
        self.image_no+=1
        
        
        response=requests.post(url, headers=headers, json=data)
        query_response_data =response.json()
        return query_response_data
    
    def upload_youtube(self,youtube):
        url = 'https://api.on-demand.io/media/v1/public/file'

        headers = {
            'Content-Type': 'application/json',
            'apikey': f'{self.api_key}'
        }
        data = {
        "createdBy":f"{self.external_user_id}",
        "updatedBy":f"{self.external_user_id}",
        "sessionId":f"{self.session_id}",
        "url":"https://www.youtube.com/watch?v=JrL6M9oRUn8",
        "plugins":["plugin-1713961903"],
        "sizeBytes":7834093,
        "responseMode":"sync"
        
        }
        self.youtube_no+=1
        
        
        response=requests.post(url, headers=headers, json=data)
        query_response_data =response.json()
        return query_response_data
    
    def upload_docs(self,docs):
        url = 'https://api.on-demand.io/media/v1/public/file'

        headers = {
            'Content-Type': 'application/json',
            'apikey': f'{self.api_key}'
        }
        data = {
        "createdBy":f"{self.external_user_id}",
        "updatedBy":f"{self.external_user_id}",
        "sessionId":f"{self.session_id}",
        "url":docs,
        "name":f"{self.document_no}",
        "plugins":["plugin-1713961903"],
        "sizeBytes":7834093,
        "responseMode":"sync"
        
        }
        self.document_no+=1
        
        
        response=requests.post(url, headers=headers, json=data)
        query_response_data =response.json()
        return query_response_data
    
    def delete_chat_session(self):

        if isinstance(self, ChatSession):
            del self
            print("Session_deleted")
        else:
            print("Provided object is not an instance of ChatSession.")


# # Create a chat session
# chat = ChatSession()

# # Submit queries
# # response1 = chat.submit_query("Hello, tell me about naruto")
# # print(response1)

# # response2 = chat.submit_query("Tell me about bleach")
# # print(response2)
# print(chat.upload_image("https://www.kasandbox.org/programming-images/avatars/leaf-green.png"))
# # End the conversation
# response2 = chat.submit_query("Tell me about the image")
# print(f"{response2=}")

# chat.delete_chat_session()

# # chat.end_conversation()
# response2 = chat.submit_query("Tell me about bleach")
