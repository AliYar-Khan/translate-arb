# ARB File Translator

A Python script to translate `.arb` (Application Resource Bundle) files into multiple languages using the `aiogoogletrans` library. It reads the source `.arb` file, translates the translatable keys into specified target languages, and generates new `.arb` files for each language.

## Features
- Translates `.arb` files into multiple languages asynchronously.
- Preserves metadata keys in the `.arb` file (keys starting with `@`).
- Saves translated content into separate `.arb` files for each target language.
- Utilizes the `aiogoogletrans` library for Google Translate API integration.

## Requirements
- Python 3.7 or higher
- Dependencies:
  - `aiogoogletrans`
  - `asyncio`

## Installation
1. Clone this repository or copy the script to your local machine.
2. Install the required dependencies:
   ```bash
   pip install aiogoogletrans
   ```

## Usage
1. Place the source `.arb` file (e.g., `app_en.arb`) in the same directory as the script.
2. Update the script's `input_file` variable with the path to your `.arb` file.
3. Specify the desired output languages in the `output_languages` list. For example:
   ```python
   output_languages = ["tr", "de", "es", "it", "fr", "ar", "en"]
   ```
4. Run the script:
   ```bash
   python script_name.py
   ```

## Example
Given a source `app_en.arb` file:
```json
{
  "title": "Hello, World!",
  "description": "Welcome to our app.",
  "@title": {
    "description": "Title of the app"
  },
  "@description": {
    "description": "Description of the app"
  }
}
```

If `output_languages = ["tr", "de"]`, the script generates:
- `app_tr.arb` (Turkish translation)
- `app_de.arb` (German translation)

Example output in `app_tr.arb`:
```json
{
  "title": "Merhaba, Dünya!",
  "description": "Uygulamamıza hoş geldiniz.",
  "@title": {
    "description": "Title of the app"
  },
  "@description": {
    "description": "Description of the app"
  }
}
```

## Notes
- Translations are performed using the Google Translate API via `aiogoogletrans`.
- Any translation errors are logged in the output file under the respective key.

## Contributing
Feel free to open issues or submit pull requests to improve the script.

## License
This project is licensed under the MIT License.
