"""Language code mapping and helpers."""

from typing import Optional

# BCP-47 -> qwen-asr expected language string (must match the model's vocabulary)
LANGUAGE_MAP = {
    "de": "German", "de-DE": "German",
    "nl": "Dutch", "nl-NL": "Dutch", "nl-BE": "Dutch",
    "sv": "Swedish", "sv-SE": "Swedish",
    "el": "Greek", "el-GR": "Greek",
    "en": "English", "en-US": "English", "en-GB": "English",
    "es": "Spanish", "es-ES": "Spanish", "es-US": "Spanish",
    "fr": "French", "fr-FR": "French", "fr-CA": "French",
    "it": "Italian", "it-IT": "Italian",
    "pt": "Portuguese", "pt-BR": "Portuguese", "pt-PT": "Portuguese",
    "ar": "Arabic", "ar-AR": "Arabic",
    "zh": "Chinese", "zh-CN": "Chinese",
    "ja": "Japanese", "ja-JP": "Japanese",
    "ko": "Korean", "ko-KR": "Korean",
    "ru": "Russian", "ru-RU": "Russian",
    "hi": "Hindi", "hi-IN": "Hindi",
    "id": "Indonesian", "id-ID": "Indonesian",
    "fil": "Filipino",
    "fa": "Persian", "fa-IR": "Persian",
    "tr": "Turkish", "tr-TR": "Turkish",
    "pl": "Polish", "pl-PL": "Polish",
    "cs": "Czech", "cs-CZ": "Czech",
    "da": "Danish", "da-DK": "Danish",
    "fi": "Finnish", "fi-FI": "Finnish",
    "th": "Thai", "th-TH": "Thai",
    "vi": "Vietnamese", "vi-VN": "Vietnamese",
    "hu": "Hungarian",
    "ro": "Romanian",
    "mk": "Macedonian",
    "ms": "Malay",
}


def resolve_language(code: str) -> Optional[str]:
    """Resolve a BCP-47 code (or simple lowercase) to the language string the model expects.
    Returns None if unsupported."""
    if not code:
        return None
    if code in LANGUAGE_MAP:
        return LANGUAGE_MAP[code]
    base = code.split("-")[0].lower()
    return LANGUAGE_MAP.get(base)