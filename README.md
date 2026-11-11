# Awesome Telegram Widgets

> Everything for building Telegram HTML Widgets (Bot API 10.4): docs, SDK support, tools, templates, open-source widgets and live demos.

English | [简体中文](README.zh-CN.md)

On 2026-11-09 Telegram [Bot API 10.4](https://core.telegram.org/bots/api-changelog#november-9-2026) let bots send **HTML widgets**: small interactive apps that live inside a message bubble. This list collects what you need to build one, plus real widgets you can read and try. Every entry was opened and checked by hand.

## Contents

- [Start here](#start-here)
- [Limits at a glance](#limits-at-a-glance)
- [Official](#official)
- [Docs & Guides](#docs--guides)
- [Libraries & SDK support](#libraries--sdk-support)
- [Developer Tools](#developer-tools)
- [Templates & Starters](#templates--starters)
- [Example Widgets](#example-widgets)
- [Bots you can try](#bots-you-can-try)
- [Articles & Talks](#articles--talks)
- [Communities](#communities)
- [Security](#security)
- [Contributing](#contributing)

## Start here

Ten links that cover most of what you need.

- [Telegram Widgets guide](https://core.telegram.org/bots/widgets) - The canonical guide: what a widget is, chat vs shared state, design rules, limits, the TelegramWidget JS object, testing, and a ready system-prompt block for LLM-written widgets.
- [widget-sandbox](https://github.com/TelegramMessenger/widget-sandbox) - The shared no-network sandbox every Telegram client runs widgets in: QuickJS isolate, DOM shim, allowlist validator, Shadow DOM renderer, SDK v1 and a Node CLI for local testing.
- [telegram-widget-kit](https://github.com/advanceddev/telegram-widget-kit) - Local Vue 3 playground: HTML/CSS/JS tabs, live bubble preview, minify + zlib-9 size readout, profile-1 linter and .tgw import/export (RU/EN UI).
- [telegram-html-bubbles](https://github.com/m0ln1z/telegram-html-bubbles) - Bilingual (EN/RU) technical guide to HTML widgets: API flow, runtime limits, silent-failure pitfalls, plus runnable Python examples.
- [telegram-doom-widget](https://github.com/ADanMan/telegram-doom-widget) - Doom E1M1 in a message: ViZDoom runs on the bot host and each tap returns a new frame squeezed into the 1 KB state limit.
- [remnawave-telegram-widget](https://github.com/run-script-dev/remnawave-telegram-widget) - VPN subscription card in a message: days left, traffic, devices, two-tap renewal with Telegram Stars, self-updating.
- [hermes-telegram-widgets](https://github.com/KirillAkimkin/hermes-telegram-widgets) - Native widgets for Hermes Agent: email, inbox, calendar, choices, task status, progress and the agent’s screen.
- [master-castle](https://github.com/alvaro-lox/master-castle) - Chess in private chats: lobby, friend challenges, timed matchmaking and a computer opponent, with SQLite persistence.
- [node-telegram-bot-api](https://github.com/yagop/node-telegram-bot-api) - Popular Node.js client; v2.4.0 adds all five widget methods, widget_query updates and a 19-widgets.ts example.
- [telegram-html-widget-skill](https://github.com/chistyar/telegram-html-widget-skill) - Agent skill plus spec digest and an automatic profile-1 linter for generating valid widgets (Russian docs).

## Limits at a glance

From the [official guide](https://core.telegram.org/bots/widgets) as of 2026-11-11.

| | |
|---|---|
| HTML size | ≤ 32 KB UTF-8 and ≤ 4 KB after zlib level 9 |
| Bubble size | width 200 px to bubble max, height 50–600 px, no scrolling |
| Runtime | QuickJS sandbox (ES2023), not a WebView; no network, no external resources |
| Input | click and pointer events only; no text fields, keyboard or wheel |
| State | `chatData` and `publicData`, ≤ 1 KB each, set by the bot |
| Bot round trip | `request()` ≤ 64 bytes → `answerWidgetQuery` within 15 s, ≤ 1 KB; 5 requests / 5 s per user |
| Storage | `localStorage` 4 KB per message, per device |
| Payments | TON wallet `sendTransaction` and `signData` from inside the widget |

**Where widgets work today**

| Feature | Test server | Production |
|---|:---:|:---:|
| Private chat with the bot (requests, wallet) | ✅ | ✅ |
| Forwarding widget messages | ✅ | ❌ |
| Groups | ✅ | ❌ |
| Inline mode | ✅ | ❌ |

## Official

### Docs & spec

- [Telegram Widgets guide](https://core.telegram.org/bots/widgets) - The canonical guide: what a widget is, chat vs shared state, design rules, limits, the TelegramWidget JS object, testing, and a ready system-prompt block for LLM-written widgets.
- [Telegram Widgets guide (Markdown)](https://core.telegram.org/bots/widgets.md) - Machine-readable Markdown copy of the widgets guide, handy for feeding to coding agents.
- [Bot API reference: sendWidget and friends](https://core.telegram.org/bots/api#sendwidget) - Method and type reference for sendWidget, sendSharedWidget, answerWidgetQuery, editMessageWidgetData, editSharedWidgetData, WidgetQuery and SharedWidgetQuery.
- [Bot API 10.4 changelog](https://core.telegram.org/bots/api-changelog#november-9-2026) - The November 9, 2026 changelog entry that introduced HTML widgets, shared widgets, TON wallet types and ephemeral button replies.
- [Widget runtime profile (authors’ guide)](https://github.com/TelegramMessenger/widget-sandbox/blob/main/docs/widget-runtime-profile.md) - Telegram’s author-facing rules for profile 1: allowed HTML/CSS/JS, how to test at bubble widths, and the LLM prompt block; sits next to sdk-v1.md, profile-v1.md and tgw-format.md.

### Announcements

- [Bot API 10.4 announcement (@BotNews)](https://t.me/BotNews/122) - “Widget Revolution”: the official Bot API 10.4 post covering widgets, queries, in-place updates, shared widgets and TON wallet integration.
- [Durov: “Any Telegram message can now become an app”](https://t.me/durov/554) - Pavel Durov’s launch post pitching widgets as 4 KB, natively rendered message apps with payments and viral mechanics.

### Runtime & renderers

- [widget-sandbox](https://github.com/TelegramMessenger/widget-sandbox) - The shared no-network sandbox every Telegram client runs widgets in: QuickJS isolate, DOM shim, allowlist validator, Shadow DOM renderer, SDK v1 and a Node CLI for local testing.
- [twidget](https://github.com/TelegramMessenger/twidget) - Native widget renderers built on an optimized litehtml fork: a portable C++20 core with Windows, Android, Qt, web (WASM) and Apple backends; powers widgets in Telegram for macOS.
- [quickjs](https://github.com/TelegramMessenger/quickjs) - Telegram’s QuickJS fork used as the widget JavaScript engine (git submodule of widget-sandbox).

### Client implementations

- [tdesktop](https://github.com/telegramdesktop/tdesktop) - Telegram Desktop source; recent commits move its widget engine to widget-sandbox v0.6.x.
- [Telegram](https://github.com/DrKLO/Telegram) - Official Android client source; bundles widget-sandbox under TMessagesProj/jni/twidget.
- [Telegram-iOS](https://github.com/TelegramMessenger/Telegram-iOS) - Official iOS client source; contains the widget host glue (WKWebView renderer path).
- [td](https://github.com/tdlib/td) - TDLib: client library with widget message support and permission checks (e.g. widgets cannot be copied).
- [tweb](https://github.com/morethanwords/tweb) - Telegram Web K source, which embeds the widget runtime with the Shadow DOM renderer.
- [telegram-macos](https://github.com/TelegramMessenger/telegram-macos) - Public source of the new Telegram for macOS client, which ships HTML widget rendering via twidget/widget-sandbox.

## Docs & Guides

### Guides

- [telegram-html-bubbles](https://github.com/m0ln1z/telegram-html-bubbles) - Bilingual (EN/RU) technical guide to HTML widgets: API flow, runtime limits, silent-failure pitfalls, plus runnable Python examples.

### Example collections

- [telegram-widget-lab](https://github.com/VyacheslavTeplyakov/telegram-widget-lab) - Unofficial set of mini-HTML cards (weather, commute picker, live inbox, etc.) with fictional data and a synthetic demo bot.

### Lists

- [awesome-telegram-widgets](https://github.com/ADanMan/awesome-telegram-widgets) - The first curated list of widgets (games and tools) plus a companion catalog bot that runs each entry inside a message.

## Libraries & SDK support

### Framework support status

Checked 2026-11-11 against releases, merged PRs and default branches.

| Framework | Language | Stars | Status | Evidence |
|---|---|---:|---|---|
| [node-telegram-bot-api](https://github.com/yagop/node-telegram-bot-api) | JS/TS | 9.2k | ✅ Released | v2.4.0 (2026-11-09) |
| [puregram + @puregram/widgets](https://github.com/puregram/puregram) | TS | 210 | ✅ Released | puregram 3.11.0 / widgets 3.0.0 |
| [Telegram.Bot](https://github.com/TelegramBots/Telegram.Bot) | C# | 3.6k | ✅ Released | NuGet 22.10.4 |
| [Telegram.BotAPI](https://github.com/Eptagone/Telegram.BotAPI) | C# | 181 | ✅ Released | v10.4 |
| [go-telegram/bot](https://github.com/go-telegram/bot) | Go | 1.9k | ✅ Released | v1.28.0 |
| [OvyFlash/telegram-bot-api](https://github.com/OvyFlash/telegram-bot-api) | Go | 149 | 🟡 Merged, not released | PR #89 (no tags) |
| [swift-telegram-bot](https://github.com/nerzh/swift-telegram-bot) | Swift | 269 | ✅ Released | 10.4.0 |
| [phptg/bot-api](https://github.com/phptg/bot-api) | PHP | 131 | ✅ Released | 0.23 |
| [westacks/telebot](https://github.com/westacks/telebot) | PHP | 310 | ✅ Released | 4.11.0 |
| [vendelieu/telegram-bot](https://github.com/vendelieu/telegram-bot) | Kotlin | 249 | ✅ Released | 9.8.0 |
| [gramiojs/types](https://github.com/gramiojs/types) | TS | 16 | ✅ Released | types v10.4.0 (framework: issue #38) |
| [mtcute](https://github.com/mtcute/mtcute) | TS | 590 | 🟡 Merged, not released | code on main |
| [telegramium](https://github.com/apimorphism/telegramium) | Scala | 95 | 🟡 Merged, not released | PR #720, not released |
| [telego](https://github.com/mymmrac/telego) | Go | 1.1k | 🟡 Merged, not released | on main, not tagged |
| [gotd/td](https://github.com/gotd/td) | Go | 2.4k | 🟡 Merged, not released | PR #1947, not released |
| [telegrinder](https://github.com/timoniq/telegrinder) | Python | 70 | 🟡 Merged, not released | #481, not released |
| [TDLib](https://github.com/tdlib/td) | C++ | 9.3k | 🟡 Merged, not released | commits, no tag |
| [aiogram](https://github.com/aiogram/aiogram) | Python | 5.9k | 🟠 PR open | PR #2004 open (use widgetgram meanwhile) |
| [gotgbot](https://github.com/PaulSonOfLars/gotgbot) | Go | 725 | 🟠 PR open | #303–#305 open |
| [rubenlagus/TelegramBots](https://github.com/rubenlagus/TelegramBots) | Java | 5.6k | 🟠 PR open | #1612 open |
| [java-telegram-bot-api](https://github.com/pengrad/java-telegram-bot-api) | Java | 2.0k | 🟠 PR open | #441 open |
| [nutgram](https://github.com/nutgram/nutgram) | PHP | 759 | 🟠 PR open | #1019 open |
| [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) | Python | 29.6k | ❌ No support yet | no activity yet (PyPI 22.8) |
| [grammY](https://github.com/grammyjs/grammY) | TS | 3.8k | ❌ No support yet | no activity yet (1.46.0) |
| [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) | Python | 8.8k | ❌ No support yet | no activity yet |
| [teloxide](https://github.com/teloxide/teloxide) | Rust | 4.3k | ❌ No support yet | no activity yet |
| [Telegraf](https://github.com/telegraf/telegraf) | TS | 9.2k | ❌ No support yet | dormant since 2024 |

### Released with widget support

- [node-telegram-bot-api](https://github.com/yagop/node-telegram-bot-api) - Popular Node.js client; v2.4.0 adds all five widget methods, widget_query updates and a 19-widgets.ts example.
- [Telegram.Bot (.NET)](https://github.com/TelegramBots/Telegram.Bot) - The main .NET client; NuGet 22.10.4 tracks Bot API 10.4 including widget methods.
- [bot](https://github.com/go-telegram/bot) - Go Bot API framework; v1.28.0 adds Bot API 10.4 and widget-query-aware update helpers.
- [telebot](https://github.com/westacks/telebot) - PHP bot framework with generated Bot API bindings that include the widget methods.
- [swift-telegram-bot](https://github.com/nerzh/swift-telegram-bot) - Swift Bot API wrapper; release 10.4.0 mirrors every widget class and method.
- [telegram-bot](https://github.com/vendelieu/telegram-bot) - Kotlin DSL Bot API wrapper; 9.8.0 covers widgets, shared widgets and widget_query updates.
- [puregram](https://github.com/puregram/puregram) - Type-safe Node.js Bot API SDK; puregram 3.11.0 sends typed widget definitions via tg.sendWidget / message.sendWidget.
- [Telegram.BotAPI](https://github.com/Eptagone/Telegram.BotAPI) - .NET Bot API library; v10.4 adds widgets (with breaking parameter-order changes).
- [telegram-bot-api](https://github.com/OvyFlash/telegram-bot-api) - Maintained fork of go-telegram-bot-api with Bot API 10.4 widget types and methods merged.
- [bot-api](https://github.com/phptg/bot-api) - PHP Bot API library; 0.23 adds SendWidget, SendSharedWidget, AnswerWidgetQuery and the two edit methods.
- [types](https://github.com/gramiojs/types) - Code-generated Bot API TypeScript types for GramIO, already at v10.4.0.
- [@puregram/widgets](https://www.npmjs.com/package/@puregram/widgets) - Dedicated widget package for puregram: immutable widget objects, typed state codecs, shared/inline helpers, query filters and safe HTML interpolation.

### Merged, release unconfirmed

- [td](https://github.com/gotd/td) - Go MTProto client; supports HTML widget messages on main.
- [telego](https://github.com/mymmrac/telego) - Go Bot API library; methods and handlers updated to 10.4 on main.
- [mtcute](https://github.com/mtcute/mtcute) - TypeScript MTProto client whose sources already reference widget methods.
- [telegramium](https://github.com/apimorphism/telegramium) - Pure-functional Scala Bot API; the 10.4 update with widgets is merged.
- [telegrinder](https://github.com/timoniq/telegrinder) - Python bot framework with 10.4 schema (incl. widget types) on main.

### Add-ons for frameworks without support

- [richgram](https://github.com/Badmunda05/richgram) - Rich-message builders for Pyrogram/Pyrofork/Kurigram; its richgram.widgets module adds 10.4 widget sending and query handling.
- [widgetgram](https://github.com/krendel001/widgetgram) - Bridges the aiogram gap: aiogram-style routers and filters for widget_query plus the five widget methods.

### Smaller frameworks with support

- [lumex](https://github.com/kbgod/lumex) - Go bot framework with widget query handling.
- [nyagram](https://github.com/Kaleert/nyagram) - Java Bot API framework with widget methods already generated.
- [yaebal](https://github.com/neverlane/yaebal) - Node/Deno/Bun Bot API library with widget methods.
- [Moonlygram](https://github.com/AtarixiaFamine/Moonlygram) - Pure-HTTP async Python Bot API framework with widget_query handling.
- [hermes](https://github.com/sidwiskers/hermes) - Zero-allocation Go bot framework with widget methods and handlers (not the Nous Hermes agent).
- [gramless](https://github.com/sidwiskers/gramless) - Zero-dependency framework for Telegram Serverless (tgcloud) that includes widget sending.
- [bindings](https://github.com/phenogram/bindings) - Strict, dependency-free PHP Bot API bindings including widget methods.
- [TGWrapper](https://github.com/jilimb0/TGWrapper) - Serverless-first TypeScript bot framework; adds widgets, shared widgets and TON wallet types.

## Developer Tools

### Playgrounds & size checkers

- [htmlbubble-widget-bot](https://github.com/fikysS/htmlbubble-widget-bot) - Self-hosted test bot that turns an uploaded .html file or pasted code into a widget message for quick device checks.
- [telegram-widget-kit](https://github.com/advanceddev/telegram-widget-kit) - Local Vue 3 playground: HTML/CSS/JS tabs, live bubble preview, minify + zlib-9 size readout, profile-1 linter and .tgw import/export (RU/EN UI).

### Mocks & testing

- [telegym](https://github.com/kolomiichenko/telegym) - Drop-in Bot API mock and k6 extension for load-testing bots; now runs and validates widgets in its debug chat.

### AI agent skills

- [telegram-skills](https://github.com/serejaris/telegram-skills) - Agent Skills pack for Telegram bots; its tg-widgets skill covers writing widgets to spec, input, state and where they render, with example widgets and a widget_tool.py helper.
- [telegram-dev](https://github.com/ssheleg/telegram-dev) - Agent plugin for building bots, userbots and Mini Apps; its bots skill includes sendWidget and widget_query guidance.
- [skills](https://github.com/puregram/skills) - Agent skills for puregram, including a framework-neutral telegram-widgets skill (lifecycle, limits, bridge) with evals.
- [telegram-html-widget-skill](https://github.com/chistyar/telegram-html-widget-skill) - Agent skill plus spec digest and an automatic profile-1 linter for generating valid widgets (Russian docs).
- [telegram-bot-widgets-skill](https://github.com/gulivan/telegram-bot-widgets-skill) - SKILL.md for Claude Code and similar agents condensing sendWidget, widget_query, TelegramWidget, limits and examples.
- [aurifex](https://github.com/lukavtz/aurifex) - Bot scaffolding toolkit for coding agents (MCP/Claude Code) with a Bot API 10.4 widgets feature module for grammY and aiogram.
- [telegram-craft](https://github.com/bisnuray/telegram-craft) - Agent skill for production Telegram bots with runnable checks; lists rich messages and 10.4 widgets among covered topics.

### Generative UI bridges

- [openui-telegram](https://github.com/pavel-voronin/openui-telegram) - Bridge that renders OpenUI generative-UI output as a widget in an existing bot, routes button presses and updates state in place.

## Templates & Starters

- [shipuchka-widget-bot](https://github.com/fedor-barulin/shipuchka-widget-bot) - Minimal Telethon (MTProto) bot template that sends widgets, with a probe widget that reports what the engine supports.
- [telegram-mini-widget-demo](https://github.com/clawgeek/telegram-mini-widget-demo) - Minimal Bot API 10.4 demo (Chinese docs): a sub-4 KB TON wallet card with interaction, in-place updates and tapper-only replies.
- [reactive-tg-bot](https://github.com/kvazzie/reactive-tg-bot) - Prototype of persistent, declarative widgets backed by Cloudflare Durable Objects and grammY.
- [telegram-bot-new-api](https://github.com/shongeorg/telegram-bot-new-api) - Ukrainian sandbox bot exercising sendRichMessage and sendWidget with editMessageWidgetData.
- [taskflow](https://github.com/volchek903/taskflow) - Starter that runs a widget bot and a React Mini App in one Python container, showing when to use each.
- [tg-cloud-sandbox](https://github.com/abhijeetpatil2122/tg-cloud-sandbox) - Multi-bot workspace for Telegram Serverless bots, including a widget bot and a check-widget-size script.
- [bots](https://github.com/chethober/bots) - Collection of small self-hosted serverless bots sharing a reusable widget base library (games, music, VPN and more).

## Example Widgets

### Games

- [rubezh](https://github.com/JJSGxKD/rubezh) - Cross-platform HTML5 dungeon-runner that adds live widget cards for Telegram.
- [master-castle](https://github.com/alvaro-lox/master-castle) - Chess in private chats: lobby, friend challenges, timed matchmaking and a computer opponent, with SQLite persistence.
- [glowgrid](https://github.com/ErwannRobin/glowgrid) - Daily Lights Out puzzle; a widget edition plus bot keeps player streaks, with a local widget mock script.
- [kartinkomet-bot](https://github.com/StonerHand/kartinkomet-bot) - Friends-group meme bot whose casino mini-games (mines, safe, slots) run as widgets.
- [telegram-doom-widget](https://github.com/ADanMan/telegram-doom-widget) - Doom E1M1 in a message: ViZDoom runs on the bot host and each tap returns a new frame squeezed into the 1 KB state limit.
- [Doom-bot](https://github.com/TEAM-PIXEL-CAT/Doom-bot) - “TIPO DOOM”: a canvas raycaster FPS with pixel monsters and procedurally changing mazes, all under 4 KB compressed.
- [telegram-widget-shooter](https://github.com/tapatuli4kaa/telegram-widget-shooter) - Dependency-free Node bot serving a raycaster shooter widget.
- [pacman](https://github.com/ronakserry/pacman) - Pacman as a standalone widget with ghost AI, lives and a browser build.
- [fly-over-dubai-telegram-widget-demo](https://github.com/run-script-dev/fly-over-dubai-telegram-widget-demo) - Flight game over Dubai in 4 KB, with the bot hosted free on Cloudflare Workers.
- [vacuum-widget](https://github.com/x4m/vacuum-widget) - One-minute PostgreSQL VACUUM arcade game sized for a message; also playable in the browser.
- [wordle-amharic-bot](https://github.com/MubarekAdem/wordle-amharic-bot) - Amharic-language Wordle played inside a widget via sendWidget and answerWidgetQuery.
- [TgBotGamesbyRoku](https://github.com/wazafab/TgBotGamesbyRoku) - Bot with four widget games: tic-tac-toe, rock-paper-scissors, Snake and 2048.
- [fifteen-widget-telegram](https://github.com/mdgfox/fifteen-widget-telegram) - Single-file 15-puzzle widget.
- [telegrart](https://github.com/Berezhnyk/telegrart) - Pixel-art editor sent as a message: /new gives a tap-to-paint canvas whose state the bot saves.
- [relaksacher](https://github.com/itashki/relaksacher) - Ollama-powered Discord/Telegram bot that adds a Snake widget with a chat leaderboard.
- [Diamond Ore widget](https://github.com/koroseyocl/test) - Minecraft-style “Diamond Ore” animation widget: ore falls and shatters into pieces on the grass.

### Commerce & Payments

- [remnawave-STEALTHNET-Bot](https://github.com/STEALTHNET-APP/remnawave-STEALTHNET-Bot) - Remnawave VPN subscription sales bot and admin site with widget cards in the bot.
- [tetherify](https://github.com/mohamadkhoshnava/tetherify) - Iranian USDT market bot that filters bad quotes from ~90 exchanges and can show them in a widget.
- [amnezia-shared-panel](https://github.com/wyrtensi/amnezia-shared-panel) - Self-hosted AmneziaWG VPN control plane that sends a reachability widget.
- [remnawave-telegram-widget](https://github.com/run-script-dev/remnawave-telegram-widget) - VPN subscription card in a message: days left, traffic, devices, two-tap renewal with Telegram Stars, self-updating.
- [monoclo-quick-order](https://github.com/yvysotskis-bit/monoclo-quick-order) - One-click order flow for a Shopify store that pushes orders to Telegram as widgets.
- [ton](https://github.com/AbdullahBalfaqih/ton) - QATTA: shared-goal widgets where participants track verified payments and invite joins inside the bubble.
- [Freebie-token-bot](https://github.com/Freebielife/Freebie-token-bot) - Demo TON token catalog bot on Cloudflare Workers Free; the token page opens as a widget with sample prices and chart.
- [WidgetTgBot](https://github.com/AndreyErmol/WidgetTgBot) - Crypto price widget (BTC, ETH, SOL and more over two pages) fed by CoinMarketCap via the bot.
- [Tgju](https://github.com/mehdi5naderi-sudo/Tgju) - Persian market-price tools with a Telegram webhook that answers widget queries.
- [poolmaster-tg](https://github.com/DrKarpov/poolmaster-tg) - JETTON market and DeFi farming analytics bot whose v1.1.0 adds interactive message widgets.

### AI Agents

- [aeon](https://github.com/aeonfun/aeon) - Autonomous agent framework running on GitHub Actions; its webhook app sends panel widgets and ephemeral widget replies.
- [iva-agent](https://github.com/smixs/iva-agent) - Self-hosted Telegram life-assistant agent with long-term memory and a widgets skill for sending interactive cards.
- [corgi](https://github.com/Andriiklymiuk/corgi) - Local-stack runner for AI agents that reports agent status to Telegram as widget cards.
- [osinara](https://github.com/nyxandro/osinara) - Self-hosted family assistant agent with a send-widget tool and link guard for generated widgets.
- [dashi-plugin-claude-code](https://github.com/qwwiwi/dashi-plugin-claude-code) - Turns a live Claude Code session into a Telegram agent; documents and implements widget output.
- [ag2-assistant](https://github.com/ag2ai/ag2-assistant) - AG2 Beta personal assistant whose Telegram channel can send generative-UI widgets.
- [temporality](https://github.com/RuslanGabbasov/temporality) - Agent runtime/control loop that renders human-in-the-loop prompts as interactive Telegram widgets.
- [Macron-Agent](https://github.com/Metixpro/Macron-Agent) - Persian self-hosted personal agent with a seeded telegram-widgets skill.
- [minclaw](https://github.com/ashishsubedi/minclaw) - Self-improving personal agent daemon with a Telegram widget formatter.
- [pi-telegram-operator](https://github.com/JohnsonRan/pi-telegram-operator) - TelegraPi: one forum topic per Pi coding session, with widget-based interactions.
- [ours-tg-connector](https://github.com/adapt-toolkit/ours-tg-connector) - Bridges ours.network agents into Telegram chats, with documented widget choice cards.
- [after-school-tea-time-telegram-bot](https://github.com/zilewang7/after-school-tea-time-telegram-bot) - Group AI bot that lets the model author widgets using an embedded widget guide.
- [codex-agent](https://github.com/rzaytsev/codex-agent) - Codex-powered personal Telegram assistant with widget templates (e.g. a music-assistant card).
- [hermes-telegram-widgets](https://github.com/KirillAkimkin/hermes-telegram-widgets) - Native widgets for Hermes Agent: email, inbox, calendar, choices, task status, progress and the agent’s screen.
- [hermes-telegram-widgets](https://github.com/Ghir0/hermes-telegram-widgets) - Live Kanban task board for Hermes Agent that refreshes in place as tasks change.
- [hermes-telegram-enhanced](https://github.com/alanzchen/hermes-telegram-enhanced) - Hermes Agent plugin adding 10.x features (rich messages, status cards, widgets with tracker/weather templates) without patching Hermes.
- [household](https://github.com/underwear/household) - Runs Claude Code/Codex bots in sandboxes and lets them answer through Telegram widgets.
- [kaa-bot](https://github.com/Udavkaa-ai/kaa-bot) - Claude-based Telegram bot with memory that ships a dice widget.
- [My_ai_assistent](https://github.com/grunvald91/My_ai_assistent) - Personal AI assistant running on Telegram Serverless that answers with HTML widgets.
- [tg-bot-mydeepseek](https://github.com/SowingSadness/tg-bot-mydeepseek) - DeepSeek-powered bot (inline + chat) with widget responses.

### Productivity

- [teleseerr](https://github.com/Nikamura/teleseerr) - Seerr/Jellyseerr media-request bot and Mini App, now with widget cards for requests and downloads.
- [hackabot](https://github.com/hacka-network/hackabot) - Community network bot that sends a weekly summary widget.
- [Telclaw](https://github.com/abolfazl260/Telclaw) - Report bot that sends cargo-by-country summaries as widgets.
- [sgbus-timings](https://github.com/augy-studios/sgbus-timings) - Singapore bus-arrival app family whose Telegram bot adds widget panels.
- [FundsFlow](https://github.com/Loafer19/FundsFlow) - Personal finance tracker with AI; Telegram channel adds budget and add-expense widgets.
- [tg-taskmgr](https://github.com/romankaveev/tg-taskmgr) - Live Linux task manager in chat: processes, CPU, RAM, disk and network with one hour of history, zero dependencies.
- [koori](https://github.com/karin0/koori) - Monitors several Linux servers and keeps a pinned widget in the bot chat as a live status panel.
- [telegram_ha_bot](https://github.com/Anykei/telegram_ha_bot) - Home Assistant bot (Rust) with an HTML widget UI for rooms, devices and cameras.
- [tgtorrentbot](https://github.com/minya/tgtorrentbot) - Transmission torrent bot that reports download progress in a live widget.
- [Lunara](https://github.com/LeezyWannaFall/Lunara) - University class-schedule bot (MIIGAiK) rendering the timetable as a widget.
- [DB_Telegram](https://github.com/kiarash6k/DB_Telegram) - Unofficial Deutsche Bahn departures/connections bot with interactive widget boards.
- [forecast](https://github.com/morfalespi/forecast) - Portuguese-language weather bot using Open-Meteo data with an interactive widget.
- [telegram-weather](https://github.com/gopellooo/telegram-weather) - Minimal weather widget (Russian) with a browser preview page and demo data; the bot fetches Open-Meteo since widgets have no network.
- [poopbot](https://github.com/drewssche/poopbot) - Group habit-tracker bot with a daily widget for answers and stats.
- [FinanceTracker](https://github.com/andrew-belikov/FinanceTracker) - Self-hosted T-Invest portfolio tracker that posts a daily portfolio widget.
- [skarb](https://github.com/tess1o/skarb) - Two-person household money tracker (bot + MCP server) that can reply with widgets.
- [hh-resume-bot-tg](https://github.com/rorythebreaker/hh-resume-bot-tg) - Telegram control panel for hh-applicant-tool (job applications) with a widget menu.
- [hirify-bot](https://github.com/Pechenje101/hirify-bot) - aiogram job-feed bot for remote/crypto vacancies offering a widget (“bubble”) display mode.
- [AI-Speaking-Bot](https://github.com/zvadym/AI-Speaking-Bot) - Language-learning bot family whose settings screen runs as a widget.
- [EspaLuzFamilybot](https://github.com/ElenaRevicheva/EspaLuzFamilybot) - Spanish-learning family bot with widget lesson cards and a progress-road widget.
- [platform](https://github.com/sachkov-inside/platform) - Membership platform whose Telegram app ships a trainer widget, documented in an ADR with a build/review pipeline.
- [deadstick](https://github.com/marvinli001/deadstick) - Airport liveness monitoring with Telegram incident cards rendered as widgets.
- [ScreenPeek](https://github.com/SudiptoKumar/ScreenPeek) - Movie/TV catalogue on Cloudflare with a Telegram widget layer.

### Utilities

- [file-from-link](https://github.com/rzashakeri/file-from-link) - yt-dlp downloader bot (1,700+ sites) with a widget module for job status.
- [skynet_bot](https://github.com/attid/skynet_bot) - MTL ecosystem tools bot with widget tooling and a test mountain-game widget.
- [telegram-htmlbubbles-verification-bot](https://github.com/null0null0xyz-max/telegram-htmlbubbles-verification-bot) - Image-grid verification widget: the bot slices a picture into 3×3 data-URL tiles and checks the user’s picks via widget_query.
- [telegram-widgets](https://github.com/Hamedshahi5/telegram-widgets) - Persian-interface calculator widget.
- [portfolio-otp-bot](https://github.com/Hawkay002/portfolio-otp-bot) - OTP bot for gated downloads that delivers the code as a widget card with a text fallback.
- [telegram-totp-widgets](https://github.com/talgatiko/telegram-totp-widgets) - TOTP authenticator widgets on Telegram Serverless; the author warns it is insecure and a proof of concept only.
- [tapreview](https://github.com/kypol52/tapreview) - Guest-review service that sends the owner a weekly stats widget.
- [myJAM](https://github.com/romastefale/myJAM) - Last.fm now-playing bot on Telegram Serverless prototyping a live music card widget.

## Bots you can try

- [@awesomewidget_bot](https://t.me/awesomewidget_bot) - Catalog bot that plays every awesome-telegram-widgets entry (Doom, Pacman, calculator, inbox...) inside messages.
- [@ADanManDoomMessageBot](https://t.me/ADanManDoomMessageBot) - Play Doom E1M1 in a message.
- [@MasterCastleApp](https://t.me/MasterCastleApp) - Chess against friends, matchmaking or the computer inside messages.
- [@game_barulin_cv_bot](https://t.me/game_barulin_cv_bot) - “Shipuchka” minibar promo game bot built on the Telethon widget template.
- [@chthgamesbot](https://t.me/chthgamesbot) - Poker, slots, blackjack, crash and trivia with free chips.
- [@kartinkomet_bot](https://t.me/kartinkomet_bot) - Group meme bot with casino mini-game widgets.
- [@JETTONPOOL_BOT](https://t.me/JETTONPOOL_BOT) - JETTON DeFi analytics with interactive widgets (closed source).
- [@funds_flow_bot](https://t.me/funds_flow_bot) - Finance tracker with budget widgets.
- [@sgbus_app](https://t.me/sgbus_app) - Singapore bus timings bot.
- [@FileFromLinkBot](https://t.me/FileFromLinkBot) - Downloader for 1,700+ sites.
- [@tetherifybot](https://t.me/tetherifybot) - Iranian USDT market rates.
- [@the_hackabot](https://t.me/the_hackabot) - Hacka* network bot with a weekly widget.

## Articles & Talks

### Habr

- [Testing interactive HTML messages in Telegram for macOS](https://habr.com/ru/articles/1092168/) - Early Habr report on the HTMLBubbles experiment found in a macOS beta.
- [HTML widgets before Bot API 10.4: sending via MTProto from Telethon](https://habr.com/ru/articles/1105576/) - How to send widgets through MTProto with a layer-233 patch before the HTTP API existed, and the pitfalls hit on the way.
- [What Telegram messages can do now: buttons, animations and your own JavaScript](https://habr.com/ru/articles/1105854/) - Builds a sub-3 KB tower game and sketches a pizzeria order card updated with editMessageWidgetData.
- [I moved chess into Telegram messages and hit the 4 KB limit](https://habr.com/ru/articles/1106354/) - Build log of the Master Castle chess widget and how it fits the size and 64-byte request limits.
- [How I ran Doom in a Telegram message and fit a frame into 1024 bytes](https://habr.com/ru/articles/1106384/) - Explains server-side rendering of Doom frames packed into widget state.

### Telegram channel posts

- [TBetaLeak: developer notes on Telegram Widgets](https://t.me/TBetaLeak/124) - Leak channel’s developer digest of widget limits (32 KB / 4 KB, 200–600 px, no scroll) with links to widget-sandbox, twidget and quickjs.
- [@tginfo: HTMLBubbles found in Telegram for macOS](https://t.me/tginfo/4438) - First public report of the HTMLBubbles subsystem in a macOS build, with security concerns.
- [@tginfo: more HTML message capabilities in 13.2 beta](https://t.me/tginfo/4447) - Beta report: bot queries, server updates, saved state, touch games, inline mode on the test server.
- [@tginfo: Telegram 13.2 / Desktop 7.4 release notes](https://t.me/tginfo/4448) - Client release roundup that lists HTML messages and Gram Wallet integration with widgets.

### News

- [Telegram Bot API 10.4: what’s new (kod.ru)](https://kod.ru/telegram-bot-api-10-4) - Russian tech-news summary of Bot API 10.4.
- [HTML widgets in Telegram (hi-tech.mail.ru)](https://hi-tech.mail.ru/news/160085-boty-v-telegram-poluchili-podderzhku-html-vidzhetov-v/) - Mainstream Russian news piece on bots getting HTML widgets.
- [Bot API 10.4 with HTML widgets and hidden replies (metaratings)](https://cybersport.metaratings.ru/news/telegram-vypustil-obnovlenie-bot-api-10-4-s-interaktivnymi-vidzhetami-i-skrytymi-otvetami-669708/) - Short news on widgets and ephemeral replies.
- [Telegram launched web widgets for bots (nnets.ru)](https://nnets.ru/news/telegram-zapustil-veb-vidzhety-dlja-botov-interaktivnye-soobschenija-s-html-i-javascript) - Pre-API news on HTML/JS widgets.
- [Telegram Bot API 10.4 released with interactive message widgets (The Tech Outlook)](https://www.thetechoutlook.com/news/apps/telegram-bot-api-10-4-released-with-interactive-message-widgets-ton-wallet-support-and-more/) - English summary of 10.4: widgets, TON wallet, ephemeral replies.
- [Telegram is turning chat messages into mini-apps (Digital Trends)](https://www.digitaltrends.com/phones/telegram-is-turning-chat-messages-into-mini-apps-because-apparently-switching-apps-is-so-last-year/) - Consumer-tech take on widgets, QuickJS sandbox and the test-server-only group features.
- [Any Telegram message can become an app (TechFlow)](https://www.techflowpost.com/en-US/newsletter/144050) - Crypto-media angle: widgets plus bots reading TON wallet balances.
- [Telegram 13.2 adds interactive HTML widgets and games (VGTimes)](https://vgtimes.com/tech-and-hardware/173701-telegram-13.2-adds-interactive-html-widgets-and-games-to-chats.html) - Gaming-site coverage of the 13.2 client release.

## Communities

### Chats

- [@BotTalk](https://t.me/BotTalk) - Large English-language Telegram bot developer chat; not widget-specific but the main general venue.

### Channels

- [@TBetaLeak](https://t.me/TBetaLeak) - Small leak channel that first spotted HTMLBubbles and posts widget developer notes.
- [@betainfo](https://t.me/betainfo) - Telegram beta-build tracker (sister of @tginfo) covering widget betas.

### Issue trackers

- [widget-sandbox issue tracker](https://github.com/TelegramMessenger/widget-sandbox/issues) - Official place to report runtime bugs and limits; already has reports on forwarding, zlib limits and Desktop number truncation.

## Security

- [telegram-widget-dos](https://github.com/Kkuwkl/telegram-widget-dos) - Proof that a 29-byte SVG path widget permanently freezes Telegram Desktop 7.4.1 via an infinite loop in the path parser.

## Contributing

Built a widget, a tool or a guide? Open a pull request or an [issue](../../issues/new/choose) — PRs are reviewed the same day during launch week. See [CONTRIBUTING.md](CONTRIBUTING.md) for the inclusion rules.

## License

[CC0 1.0](LICENSE). Entry descriptions are written by the maintainers.
