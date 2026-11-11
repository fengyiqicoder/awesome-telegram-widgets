#!/usr/bin/env python3
"""Build README.md and README.zh-CN.md from data/entries.json and data/frameworks.json."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
entries = [e for e in json.loads((ROOT / "data/entries.json").read_text()) if e.get("verified")]
frameworks = json.loads((ROOT / "data/frameworks.json").read_text())

START_HERE = [
    "https://core.telegram.org/bots/widgets",
    "https://github.com/TelegramMessenger/widget-sandbox",
    "https://github.com/advanceddev/telegram-widget-kit",
    "https://github.com/m0ln1z/telegram-html-bubbles",
    "https://github.com/ADanMan/telegram-doom-widget",
    "https://github.com/run-script-dev/remnawave-telegram-widget",
    "https://github.com/KirillAkimkin/hermes-telegram-widgets",
    "https://github.com/alvaro-lox/master-castle",
    "https://github.com/yagop/node-telegram-bot-api",
    "https://github.com/chistyar/telegram-html-widget-skill",
]

# (category, [subcategories in order]); None = all subcategories in data order
SECTIONS = [
    ("Official", ["Docs & spec", "Announcements", "Runtime & renderers", "Client implementations"]),
    ("Docs & Guides", None),
    ("Libraries & SDK support", ["Released with widget support", "Merged, release unconfirmed",
                                 "Add-ons for frameworks without support", "Smaller frameworks with support"]),
    ("Developer Tools", None),
    ("Templates & Starters", None),
    ("Example Widgets", ["Games", "Commerce & Payments", "AI Agents", "Productivity", "Utilities"]),
    ("Bots you can try", None),
    ("Articles & Talks", None),
    ("Communities", None),
    ("Security", None),
]

STATUS = {
    "released": ("✅", "Released", "已发布"),
    "merged": ("🟡", "Merged, not released", "已合并未发布"),
    "pr": ("🟠", "PR open", "PR 未合并"),
    "none": ("❌", "No support yet", "暂无支持"),
}

T = {
    "en": {
        "title": "# Awesome Telegram Widgets",
        "tagline": "> Everything for building Telegram HTML Widgets (Bot API 10.4): docs, SDK support, tools, templates, open-source widgets and live demos.",
        "lang": "English | [简体中文](README.zh-CN.md)",
        "intro": ("On 2026-11-09 Telegram [Bot API 10.4](https://core.telegram.org/bots/api-changelog#november-9-2026) "
                  "let bots send **HTML widgets**: small interactive apps that live inside a message bubble. "
                  "This list collects what you need to build one, plus real widgets you can read and try. "
                  "Every entry was opened and checked by hand."),
        "contents": "## Contents",
        "facts": "## Limits at a glance",
        "facts_intro": "From the [official guide](https://core.telegram.org/bots/widgets) as of 2026-11-11.",
        "facts_rows": [
            ("HTML size", "≤ 32 KB UTF-8 and ≤ 4 KB after zlib level 9"),
            ("Bubble size", "width 200 px to bubble max, height 50–600 px, no scrolling"),
            ("Runtime", "QuickJS sandbox (ES2023), not a WebView; no network, no external resources"),
            ("Input", "click and pointer events only; no text fields, keyboard or wheel"),
            ("State", "`chatData` and `publicData`, ≤ 1 KB each, set by the bot"),
            ("Bot round trip", "`request()` ≤ 64 bytes → `answerWidgetQuery` within 15 s, ≤ 1 KB; 5 requests / 5 s per user"),
            ("Storage", "`localStorage` 4 KB per message, per device"),
            ("Payments", "TON wallet `sendTransaction` and `signData` from inside the widget"),
        ],
        "avail": "Where widgets work today",
        "avail_rows": [
            ("Private chat with the bot (requests, wallet)", "✅", "✅"),
            ("Forwarding widget messages", "✅", "❌"),
            ("Groups", "✅", "❌"),
            ("Inline mode", "✅", "❌"),
        ],
        "avail_head": "| Feature | Test server | Production |",
        "facts_head": "| | |",
        "start": "## Start here",
        "start_intro": "Ten links that cover most of what you need.",
        "fw_title": "### Framework support status",
        "fw_intro": "Checked 2026-11-11 against releases, merged PRs and default branches.",
        "fw_head": "| Framework | Language | Stars | Status | Evidence |",
        "contrib": "## Contributing",
        "contrib_text": ("Built a widget, a tool or a guide? Open a pull request or an "
                         "[issue](../../issues/new/choose) — PRs are reviewed the same day during launch week. "
                         "See [CONTRIBUTING.md](CONTRIBUTING.md) for the inclusion rules."),
        "license": "## License",
        "license_text": "[CC0 1.0](LICENSE). Entry descriptions are written by the maintainers.",
    },
    "zh": {
        "title": "# Awesome Telegram Widgets",
        "tagline": "> 开发 Telegram HTML Widget（Bot API 10.4）需要的一切：文档、框架支持、工具、模板、开源 Widget 和可试玩的演示。",
        "lang": "[English](README.md) | 简体中文",
        "intro": ("2026-11-09，Telegram [Bot API 10.4](https://core.telegram.org/bots/api-changelog#november-9-2026) "
                  "允许机器人发送 **HTML Widget**：直接活在消息气泡里的可交互小应用。"
                  "这里收集做 Widget 需要的资料，以及可以读源码、可以试玩的真实 Widget。每一条都人工打开核实过。"
                  "条目描述暂时保留英文。"),
        "contents": "## 目录",
        "facts": "## 限制速查",
        "facts_intro": "来自[官方指南](https://core.telegram.org/bots/widgets)，截至 2026-11-11。",
        "facts_rows": [
            ("HTML 体积", "UTF-8 不超过 32 KB，zlib 9 级压缩后不超过 4 KB"),
            ("气泡尺寸", "宽 200 px 到气泡最大宽度，高 50–600 px，不能滚动"),
            ("运行环境", "QuickJS 沙箱（ES2023），不是 WebView；没有网络，不加载任何外部资源"),
            ("输入", "只有点击和指针事件；没有输入框、键盘和滚轮"),
            ("状态", "`chatData` 和 `publicData`，各不超过 1 KB，由机器人设置"),
            ("和机器人通信", "`request()` 不超过 64 字节 → 15 秒内 `answerWidgetQuery`，不超过 1 KB；每个用户 5 秒最多 5 次"),
            ("本地存储", "`localStorage` 每条消息、每台设备 4 KB"),
            ("付款", "Widget 内可调用 TON 钱包的 `sendTransaction` 和 `signData`"),
        ],
        "avail": "现在哪里能用",
        "avail_rows": [
            ("和机器人的私聊（请求、钱包）", "✅", "✅"),
            ("转发 Widget 消息", "✅", "❌"),
            ("群聊", "✅", "❌"),
            ("Inline 模式", "✅", "❌"),
        ],
        "avail_head": "| 功能 | 测试服务器 | 正式环境 |",
        "facts_head": "| | |",
        "start": "## 从这里开始",
        "start_intro": "覆盖大部分需求的十个链接。",
        "fw_title": "### 框架支持状态",
        "fw_intro": "2026-11-11 按 release、已合并 PR 和默认分支核对。",
        "fw_head": "| 框架 | 语言 | 星 | 状态 | 依据 |",
        "contrib": "## 参与贡献",
        "contrib_text": ("做了 Widget、工具或教程？直接提 PR 或[开 issue](../../issues/new/choose)，首发这一周当天审核。"
                         "收录规则见 [CONTRIBUTING.md](CONTRIBUTING.md)。"),
        "license": "## 协议",
        "license_text": "[CC0 1.0](LICENSE)。条目描述由维护者撰写。",
    },
}

SEC_ZH = {
    "Official": "官方", "Docs & Guides": "文档与教程", "Libraries & SDK support": "框架与 SDK 支持",
    "Developer Tools": "开发工具", "Templates & Starters": "模板与起步项目", "Example Widgets": "Widget 示例",
    "Bots you can try": "可以试玩的机器人", "Articles & Talks": "文章", "Communities": "社区", "Security": "安全",
    "Games": "游戏", "Commerce & Payments": "电商与付款", "AI Agents": "AI Agent", "Productivity": "效率",
    "Utilities": "工具类",
}


def anchor(text):
    return re.sub(r"[^\w\- ]", "", text.lower()).strip().replace(" ", "-")


def line(e):
    desc = e["description_en"].strip()
    if not desc.endswith("."):
        desc += "."
    return f"- [{e['name']}]({e['url']}) - {desc}"


def build(lang):
    t = T[lang]
    name = (lambda s: SEC_ZH.get(s, s)) if lang == "zh" else (lambda s: s)
    by_url = {e["url"]: e for e in entries}
    out = [t["title"], "", t["tagline"], "", t["lang"], "", t["intro"], "", t["contents"], ""]
    toc = [t["start"][3:], t["facts"][3:]] + [name(c) for c, _ in SECTIONS] + [t["contrib"][3:]]
    out += [f"- [{x}](#{anchor(x)})" for x in toc] + [""]

    out += [t["start"], "", t["start_intro"], ""]
    out += [line(by_url[u]) for u in START_HERE if u in by_url] + [""]

    out += [t["facts"], "", t["facts_intro"], "", t["facts_head"], "|---|---|"]
    out += [f"| {a} | {b} |" for a, b in t["facts_rows"]] + [""]
    out += [f"**{t['avail']}**", "", t["avail_head"], "|---|:---:|:---:|"]
    out += [f"| {a} | {b} | {c} |" for a, b, c in t["avail_rows"]] + [""]

    for cat, subs in SECTIONS:
        items = [e for e in entries if e["category"] == cat]
        if not items:
            continue
        out += [f"## {name(cat)}", ""]
        if cat == "Libraries & SDK support":
            out += [t["fw_title"], "", t["fw_intro"], "", t["fw_head"], "|---|---|---:|---|---|"]
            for f in frameworks:
                icon, en, zh = STATUS[f["status"]]
                out.append(f"| [{f['name']}]({f['url']}) | {f['lang']} | {f['stars']} | {icon} {en if lang == 'en' else zh} | {f['evidence']} |")
            out.append("")
        order = subs or list(dict.fromkeys(e["subcategory"] for e in items))
        multi = len(order) > 1
        for sub in order:
            group = sorted([e for e in items if e["subcategory"] == sub], key=lambda e: -(e.get("stars") or 0))
            if not group:
                continue
            if multi:
                out += [f"### {name(sub)}", ""]
            out += [line(e) for e in group] + [""]

    out += [t["contrib"], "", t["contrib_text"], "", t["license"], "", t["license_text"], ""]
    return "\n".join(out)


(ROOT / "README.md").write_text(build("en"))
(ROOT / "README.zh-CN.md").write_text(build("zh"))
print(f"{len(entries)} verified entries written")
