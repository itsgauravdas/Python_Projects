from googletrans import Translator, LANGUAGES
import asyncio
# pip install googletrans==4.0.0-rc1
async def translate_tool(text, target_language):
    try:
        translator  =Translator()
        translated_text  = translator.translate(text, dest=target_language)
        return translated_text.text
    except Exception as e:
        print(e)
        
async def main():
    for code,languages in LANGUAGES.items():
        print(f'{code}:{languages}')
        
    text = input("Enter the text you want to translarte: - ")
    target_language = input("Enter the target language (e.g., 'fr' for French, 'es' for Spanish): ")
    
    if target_language not in LANGUAGES:
        print("Invalid language code. Please choose a valid language code from the list above.")
        return
    translated_text = await translate_tool(text, target_language)
    print(f"Translated text:- {translated_text}")

if __name__ == "__main__":
    asyncio.run(main())