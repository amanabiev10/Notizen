import openai

# Setze deinen API-Schlüssel
openai.api_key = 'sk-proj-VXSBf1aXx07JPUmo3lkOT3BlbkFJv5tVOroind86C5FOQci2'

# Beispielanfrage an GPT-3
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="Erkläre, wie man die OpenAI API mit Python verwendet.",
    max_tokens=150
)

# Ausgabe der Antwort
print(response.choices[0].text.strip())