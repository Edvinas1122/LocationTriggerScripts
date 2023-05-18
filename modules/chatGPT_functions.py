import openai

def	getResponse(request, responseCount, chatGPT_api_key, organization, max_token_count=30):
	openai.organization = organization
	openai.api_key = chatGPT_api_key

	chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": request}], n=responseCount, max_tokens=max_token_count)

	responses = [choice.message.content for choice in chat_completion.choices]
	return responses
