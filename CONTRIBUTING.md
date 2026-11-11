# Contributing

Thanks for adding to the list. During launch week pull requests are reviewed the same day.

## What gets in

An entry must be about **Telegram HTML widgets** (Bot API 10.4 `sendWidget`, `window.TelegramWidget`). Not the Telegram Login Widget, not post-embed widgets, not website chat widgets.

It must also meet at least one of these:

- Public source code that really uses the widget API, or
- A bot people can open in Telegram and try today, or
- A guide, tool or library that a widget developer would actually use.

Not accepted: closed products with no demo, pure marketing pages, and duplicates of an existing entry. One entry per project.

## How to add

1. Add an object to `data/entries.json` with `name`, `url`, `category`, `subcategory`, `description_en` and `verified: true`.
2. Write the description yourself: one sentence, what it does, no hype.
3. Run `python3 scripts/gen_readme.py` and commit both READMEs.

Or just [open an issue](../../issues/new/choose) with the link and we will add it.

If you maintain the project you are adding, say so in the PR. The same rules apply to everyone, including the maintainers of this list.
