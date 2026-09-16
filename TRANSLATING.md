# Translation guide

English is the canonical editorial source. Structured protocol IDs and factual fields are language-neutral. Translations may improve sentence structure for their readers but must preserve technical meaning.

## Supported languages

| Code | Language | Status |
|---|---|---|
| en | English | Canonical |
| zh-CN | 简体中文 | Maintained |
| zh-TW | 繁體中文 | Community |
| ja | 日本語 | Community |
| ko | 한국어 | Community |
| es | Español | Community |
| pt-BR | Português do Brasil | Community |
| fr | Français | Community |
| de | Deutsch | Community |
| ru | Русский | Community |
| ar | العربية | Community, RTL |

Documentation languages are registered in data/languages.json. Per-protocol prose translations are registered separately in data/protocols.json, so community navigation support does not imply that every protocol summary has been reviewed in that language.

## Alignment rules

- Match entries using protocol ID, never heading text or line number.
- Keep protocol names, port numbers, RFC numbers, and standards unchanged.
- Translate explanatory prose, not code, packet fields, or command examples.
- Link each translated home page to English and every maintained language.
- Record incomplete translations in a pull request checklist.

## Terminology

Create docs/LANGUAGE_CODE/glossary.md when a language is introduced. Reuse established technical translations and retain the English term where ambiguity would harm learning.
