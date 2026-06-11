from __future__ import annotations

import html
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def page_shell(title: str, body: str, css_href: str, home_href: str, zh_href: str, en_href: str) -> str:
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <meta name="description" content="Public articles on enterprise AI analytics, trustworthy data retrieval, and governed insight generation.">
  <link rel="stylesheet" href="{css_href}">
</head>
<body>
  <header class="site-header">
    <div class="site-header-inner">
      <a class="brand" href="{home_href}">AI Data Insights Series</a>
      <nav class="nav" aria-label="Primary">
        <a href="{zh_href}">中文 P0</a>
        <a href="{en_href}">English P0</a>
        <a href="https://github.com/Ericyoung-183/ai-data-insights-series/discussions/1">Discussion</a>
        <a href="https://github.com/Ericyoung-183/ai-data-insights-series">GitHub</a>
      </nav>
    </div>
  </header>
{body}
  <footer class="site-footer">
    Copyright © 2026 Eric Young. All rights reserved.
  </footer>
</body>
</html>
"""


def build_index() -> None:
    body = """  <main class="page">
    <section class="hero">
      <p class="eyebrow">可信取数 + 深度业务洞察</p>
      <h1>把数取准，把问题问深。</h1>
      <p class="subtitle">企业 AI 分析的核心，不是 Text-to-SQL，也不是把 Dashboard 换成聊天框，而是让 AI 在受治理的数据资产、数据知识、确定性计算和业务认知之上，形成能支撑管理判断的深度业务洞察。</p>
      <div class="actions">
        <a class="button primary" href="zh/p0-eight-layer-architecture.html">阅读中文 P0</a>
        <a class="button" href="en/p0-eight-layer-architecture.html">Read English P0</a>
      </div>
    </section>

    <section class="grid" aria-label="Published articles">
      <article class="article-card">
        <h2>中文 P0</h2>
        <p><strong>可信取数+深度业务洞察：企业 AI 分析师的八层架构</strong></p>
        <p>一篇总论，解释为什么企业 AI 分析不能停在 Text-to-SQL，而需要把数据资产、数据知识、确定性计算、业务认知、分析方法、战略问题、报告行动和运行治理放进同一张图。</p>
        <p><a href="zh/p0-eight-layer-architecture.html">打开文章</a></p>
      </article>

      <article class="article-card">
        <h2>English P0</h2>
        <p><strong>Trustworthy Numbers, Deeper Business Questions</strong></p>
        <p>The English companion version of the overview article, framing an eight-layer architecture for enterprise AI analysts and governed insight generation.</p>
        <p><a href="en/p0-eight-layer-architecture.html">Open article</a></p>
      </article>
    </section>

    <section class="note" style="margin-top:18px">
      <p><strong>Note.</strong> All examples in these articles are synthetic. They do not refer to any real business, metric, data table, or internal system.</p>
      <p>Author: Eric Young-ANT Group (Ericyang.nna@gmail.com)</p>
      <p><a href="https://github.com/Ericyoung-183/ai-data-insights-series/discussions/1">Join the discussion on GitHub</a></p>
    </section>
  </main>
"""
    (ROOT / "index.html").write_text(
        page_shell(
            "AI Data Insights Series",
            body,
            "site.css",
            "./",
            "zh/p0-eight-layer-architecture.html",
            "en/p0-eight-layer-architecture.html",
        )
    )


def markdown_fragment(path: Path) -> str:
    result = subprocess.run(
        ["pandoc", str(path), "--from=gfm", "--to=html5"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout


def build_article(src: str, dst: str, title: str, zh_href: str, en_href: str) -> None:
    fragment = markdown_fragment(ROOT / src)
    body = f"""  <main class="page">
    <article class="prose">
{fragment}
    </article>
  </main>
"""
    out = ROOT / dst
    out.write_text(page_shell(title, body, "../site.css", "../", zh_href, en_href))


def main() -> None:
    build_index()
    build_article(
        "zh/p0-eight-layer-architecture.md",
        "zh/p0-eight-layer-architecture.html",
        "可信取数+深度业务洞察：企业 AI 分析师的八层架构",
        "p0-eight-layer-architecture.html",
        "../en/p0-eight-layer-architecture.html",
    )
    build_article(
        "en/p0-eight-layer-architecture.md",
        "en/p0-eight-layer-architecture.html",
        "Trustworthy Numbers, Deeper Business Questions",
        "../zh/p0-eight-layer-architecture.html",
        "p0-eight-layer-architecture.html",
    )


if __name__ == "__main__":
    main()
