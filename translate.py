import json
import asyncio
from aiogoogletrans import Translator

async def translate_arb(file_path, output_languages):
    # Load the ARB file
    with open(file_path, 'r', encoding='utf-8') as file:
        arb_data = json.load(file)

    # Extract translatable keys (excluding metadata keys starting with "@")
    translatable_keys = {key: value for key, value in arb_data.items() if not key.startswith("@")}

    # Initialize the translator
    translator = Translator()

    # Prepare translations for each language
    translations = {lang: {} for lang in output_languages}
    for lang_code in output_languages:
        for key, text in translatable_keys.items():
            try:
                # Await translation
                translated_text = await translator.translate(text, src="en", dest=lang_code)
                translations[lang_code][key] = translated_text.text
            except Exception as e:
                translations[lang_code][key] = f"Error: {e}"

    # Save translations to new ARB files
    for lang_code, translated_content in translations.items():
        output_file_path = f'app_{lang_code}.arb'
        with open(output_file_path, 'w', encoding='utf-8') as file:
            json.dump({**translated_content, **{k: arb_data[k] for k in arb_data if k.startswith("@")}}, file, ensure_ascii=False, indent=2)
        print(f"Translation saved: {output_file_path}")

# Define the input ARB file and languages
input_file = "app_en.arb"
output_languages = ["tr", "de", "es", "it", "fr", "ar", "en"]

# Run the translation process
asyncio.run(translate_arb(input_file, output_languages))
