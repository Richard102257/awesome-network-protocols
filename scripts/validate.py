#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "protocols.json"
LANGUAGES = ROOT / "data" / "languages.json"
ALLOWED_LAYERS = {"physical", "data-link", "network", "transport", "session", "presentation", "application"}
ALLOWED_STATUS = {"current", "historic", "experimental", "proprietary"}
REQUIRED = {"id", "name", "layer", "category", "status", "ports", "standard", "url"}


def validate():
    errors = []
    try:
        document = json.loads(DATA.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"Cannot read {DATA.relative_to(ROOT)}: {exc}"]

    languages = document.get("languages", [])
    language_document = json.loads(LANGUAGES.read_text(encoding="utf-8"))
    documentation_languages = [item["code"] for item in language_document.get("languages", [])]
    entries = document.get("protocols", [])
    if languages[:2] != ["en", "zh-CN"]:
        errors.append("languages must begin with en and zh-CN")
    if not isinstance(entries, list) or not entries:
        errors.append("protocols must be a non-empty list")
        return errors

    seen = set()
    for index, entry in enumerate(entries, 1):
        label = f"protocols[{index}]"
        missing = REQUIRED - set(entry)
        if missing:
            errors.append(f"{label}: missing {', '.join(sorted(missing))}")
            continue
        protocol_id = entry["id"]
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", protocol_id):
            errors.append(f"{label}: invalid id {protocol_id!r}")
        if protocol_id in seen:
            errors.append(f"{label}: duplicate id {protocol_id!r}")
        seen.add(protocol_id)
        if entry["layer"] not in ALLOWED_LAYERS:
            errors.append(f"{protocol_id}: unknown layer {entry['layer']!r}")
        if entry["status"] not in ALLOWED_STATUS:
            errors.append(f"{protocol_id}: unknown status {entry['status']!r}")
        if not isinstance(entry["standard"], list) or not entry["standard"]:
            errors.append(f"{protocol_id}: standard must be a non-empty list")
        parsed = urlparse(entry["url"])
        if parsed.scheme != "https" or not parsed.netloc:
            errors.append(f"{protocol_id}: url must be an absolute HTTPS URL")
        for language in languages:
            locale = entry.get(language)
            if not isinstance(locale, dict):
                errors.append(f"{protocol_id}: missing locale {language}")
                continue
            for field in ("fullName", "summary"):
                if not isinstance(locale.get(field), str) or not locale[field].strip():
                    errors.append(f"{protocol_id}: {language}.{field} is empty")

    if documentation_languages != ["en", "zh-CN", "zh-TW", "ja", "ko", "es", "pt-BR", "fr", "de", "ru", "ar"]:
        errors.append("documentation language registry is incomplete or out of order")
    arabic = next((item for item in language_document["languages"] if item["code"] == "ar"), {})
    if arabic.get("direction") != "rtl":
        errors.append("Arabic must declare RTL direction")

    for language in documentation_languages:
        docs = ROOT / "docs" / language
        for filename in ("README.md", "catalog.md", "taxonomy.md", "learning-paths.md", "protocol-entry.md"):
            if not (docs / filename).is_file():
                errors.append(f"missing translated navigation file: docs/{language}/{filename}")
        taxonomy = docs / "taxonomy.md"
        if taxonomy.is_file():
            taxonomy_text = taxonomy.read_text(encoding="utf-8")
            section_count = len(re.findall(r"^### ", taxonomy_text, flags=re.MULTILINE))
            official_link_count = len(re.findall(r"https://", taxonomy_text))
            minimum_sections = 21
            minimum_links = 65
            if section_count < minimum_sections:
                errors.append(f"{language}: taxonomy has {section_count} detailed sections; expected at least {minimum_sections}")
            if official_link_count < minimum_links:
                errors.append(f"{language}: taxonomy has {official_link_count} official links; expected at least {minimum_links}")

    catalogs = {language: ((ROOT / "README.md") if language == "en" else (ROOT / "docs" / language / "catalog.md")).read_text(encoding="utf-8") for language in documentation_languages}
    for entry in entries:
        expected_link = f"[{entry['name']}]({entry['url']})"
        for language, catalog in catalogs.items():
            if language == "en":
                catalog = (ROOT / "docs" / "en" / "catalog.md").read_text(encoding="utf-8")
            if expected_link not in catalog:
                errors.append(f"{entry['id']}: missing or mismatched link in {language} catalog")
    return errors


if __name__ == "__main__":
    failures = validate()
    if failures:
        print("Validation failed:")
        for failure in failures:
            print(f"- {failure}")
        sys.exit(1)
    count = len(json.loads(DATA.read_text(encoding="utf-8"))["protocols"])
    doc_count = len(json.loads(LANGUAGES.read_text(encoding="utf-8"))["languages"])
    print(f"Validation passed: {count} protocols, {doc_count} documentation languages")
