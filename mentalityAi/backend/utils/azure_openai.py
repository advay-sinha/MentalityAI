import openai

# Set your Azure OpenAI credentials
openai.api_key = "2DENF6UvocnLSvBwcxyDjgJgbwisNLPXAW6lWdXak9thsJNvMNq4JQQJ99BAAC77bzfXJ3w3AAABACOGBAql"
openai.api_base = "https://openaimentality.openai.azure.com/" #endpoint
openai.api_version = "2024-10-21"  # Replace with the correct API version
openai.api_type = "azure"

def get_chatbot_response(user_input):
    try:
        # Call Azure OpenAI API
        response = openai.ChatCompletion.create(
            engine="Microsoft.CognitiveServicesOpenAI-20250118112718",  # Replace with your Azure deployment name
            messages=[
                {"role": "system", "content": "Create a Generative AI-Based Therapist Assistant that provides personalized coping strategies, mental health resources, and suggestions based on user inputs. This assistant will help users manage their mental well-being by offering real-time support tailored to their emotional state and concerns.,some features:provide strategies, advice, and resources that are tailored to their specific mental health needs.,Use AI models to analyze user inputs (e.g., feelings, moods, and specific challenges) and suggest personalized coping strategies such as breathing exercises, journaling prompts, mindfulness practices, or cognitive-behavioral techniques (CBT),Use natural language processing (NLP) to understand and respond empathetically to user concerns, offering relevant advice and guidance.,Suggest resources based on user concerns, such as dealing with anxiety, overcoming negative thoughts, or building resilience."},
                {"role": "user", "content": user_input},
            ],
        )
        # Extract the chatbot's reply
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"
   