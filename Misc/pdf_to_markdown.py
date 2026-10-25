#!/usr/bin/env python3
"""Convert Algorithms_Dasgupta.pdf into one Markdown file per chapter.

Math is emitted as LaTeX ($...$ / $$...$$). Vector figures, which this PDF
draws with lines rather than embedding images, are rebuilt as Mermaid diagrams.
Embedded images, if any, are saved beside the chapter files.

Usage:
    python pdf_to_markdown.py Algorithms_Dasgupta.pdf -o algorithms_md
"""

from __future__ import annotations

import argparse
import html
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

import pdfplumber
from pdfminer.high_level import extract_pages
from pdfminer.layout import (
    LTAnno,
    LTChar,
    LTCurve,
    LTFigure,
    LTImage,
    LTLine,
    LTRect,
    LTTextBox,
    LTTextLine,
)

# Computer Modern math italic (CMMI) and symbol (CMSY) private-use glyphs
# that pdfminer returns for this PDF. Identity mappings are omitted.
CMMI = {
    "\uf0a1": r"\Gamma", "\uf0a2": r"\Delta", "\uf0a3": r"\Theta", "\uf0a4": r"\Lambda",
    "\uf0a5": r"\Xi", "\uf0a6": r"\Pi", "\uf0a7": r"\Sigma", "\uf0a8": r"\Upsilon",
    "\uf0a9": r"\Phi", "\uf0aa": r"\Psi", "\uf0ab": r"\Omega",
    "\uf0ae": r"\alpha", "\uf0af": r"\beta", "\uf0b0": r"\gamma", "\uf0b1": r"\delta",
    "\uf0b2": r"\epsilon", "\uf0b3": r"\zeta", "\uf0b4": r"\eta", "\uf0b5": r"\theta",
    "\uf0b6": r"\iota", "\uf0b7": r"\kappa", "\uf0b8": r"\lambda", "\uf0b9": r"\mu",
    "\uf0ba": r"\nu", "\uf0bb": r"\xi", "\uf0bc": r"\pi", "\uf0bd": r"\rho",
    "\uf0be": r"\sigma", "\uf0bf": r"\tau", "\uf0c0": r"\upsilon", "\uf0c1": r"\phi",
    "\uf0c2": r"\chi", "\uf0c3": r"\psi", "\uf0c4": r"\omega",
    "\uf0c5": r"\varepsilon", "\uf0c6": r"\vartheta", "\uf0c7": r"\varpi",
    "\uf0c8": r"\varrho", "\uf0c9": r"\varsigma", "\uf0ca": r"\varphi",
    "\uf0cb": r"\ell", "\uf0cd": r"\wp", "\uf0ce": r"\partial",
    "\uf03a": r"\infty",
}
CMSY = {
    "\uf021": r"\cdot", "\uf022": r"\times", "\uf023": r"\ast", "\uf024": r"\div",
    "\uf025": r"\diamond", "\uf026": r"\pm", "\uf027": r"\mp", "\uf028": r"\oplus",
    "\uf029": r"\ominus", "\uf02a": r"\otimes", "\uf02b": r"\oslash",
    "\uf02c": r"\odot", "\uf02d": r"\bigcirc", "\uf02e": r"\circ", "\uf02f": r"\bullet",
    "\uf030": r"\asymp", "\uf031": r"\equiv", "\uf032": r"\subseteq",
    "\uf033": r"\supseteq", "\uf034": r"\leq", "\uf035": r"\geq",
    "\uf036": r"\preceq", "\uf037": r"\succeq", "\uf038": r"\sim",
    "\uf039": r"\approx", "\uf03a": r"\subset", "\uf03b": r"\supset",
    "\uf03c": r"\ll", "\uf03d": r"\gg", "\uf03e": r"\prec", "\uf03f": r"\succ",
    "\uf040": r"\leftarrow", "\uf041": r"\rightarrow",
    "\uf042": r"\uparrow", "\uf043": r"\downarrow",
    "\uf044": r"\leftrightarrow", "\uf045": r"\nearrow",
    "\uf046": r"\searrow", "\uf047": r"\simeq",
    "\uf048": r"\Leftarrow", "\uf049": r"\Rightarrow",
    "\uf04a": r"\Uparrow", "\uf04b": r"\Downarrow",
    "\uf04c": r"\Leftrightarrow", "\uf04d": r"\nwarrow",
    "\uf04e": r"\swarrow", "\uf04f": r"\propto",
    "\uf050": r"\prime", "\uf051": r"\infty",
    "\uf05c": r"\cup", "\uf05b": r"\cap",
    "\uf05e": r"\vee", "\uf05f": r"\wedge",
    "\uf060": r"\vdash", "\uf061": r"\dashv",
    "\uf06e": r"\setminus", "\uf06f": r"\wr",
    "\uf070": r"\sqrt", "\uf071": r"\coprod",
    "\uf072": r"\int", "\uf073": r"\sqcup", "\uf074": r"\sqcap",
    "\uf078": r"\sum", "\uf079": r"\prod",
    "\uf0a6": r"\in", "\uf0a7": r"\ni",
    "\uf0a8": r"\notin", "\uf0a9": r"\angle",
    "\uf0ae": r"\forall", "\uf0af": r"\exists",
    "\uf0ac": r"\neg", "\uf0ad": r"\backslash",
}
CMR_PUA = {
    "\uf020": " ", "\uf02d": "-", "\uf0a1": "!", "\uf0a2": '"', "\uf0a3": "#",
    "\uf0a4": "$", "\uf0a5": "%", "\uf0a6": "&", "\uf0a7": "'",
    "\uf0a8": "(", "\uf0a9": ")", "\uf0aa": "*", "\uf0ab": "+",
    "\uf0ac": ",", "\uf0ad": "-", "\uf0ae": ".", "\uf0af": "/",
    "\uf0b0": "0", "\uf0b1": "1", "\uf0b2": "2", "\uf0b3": "3",
    "\uf0b4": "4", "\uf0b5": "5", "\uf0b6": "6", "\uf0b7": "7",
    "\uf0b8": "8", "\uf0b9": "9", "\uf0ba": ":", "\uf0bb": ";",
    "\uf0bc": "<", "\uf0bd": "=", "\uf0be": ">", "\uf0bf": "?",
    "\uf0c0": "@", "\uf0c1": "A", "\uf0c2": "B", "\uf0c3": "C",
    "\uf0c4": "D", "\uf0c5": "E", "\uf0c6": "F", "\uf0c7": "G",
    "\uf0c8": "H", "\uf0c9": "I", "\uf0ca": "J", "\uf0cb": "K",
    "\uf0cc": "L", "\uf0cd": "M", "\uf0ce": "N", "\uf0cf": "O",
    "\uf0d0": "P", "\uf0d1": "Q", "\uf0d2": "R", "\uf0d3": "S",
    "\uf0d4": "T", "\uf0d5": "U", "\uf0d6": "V", "\uf0d7": "W",
    "\uf0d8": "X", "\uf0d9": "Y", "\uf0da": "Z",
    "\uf0e1": "a", "\uf0e2": "b", "\uf0e3": "c", "\uf0e4": "d",
    "\uf0e5": "e", "\uf0e6": "f", "\uf0e7": "g", "\uf0e8": "h",
    "\uf0e9": "i", "\uf0ea": "j", "\uf0eb": "k", "\uf0ec": "l",
    "\uf0ed": "m", "\uf0ee": "n", "\uf0ef": "o", "\uf0f0": "p",
    "\uf0f1": "q", "\uf0f2": "r", "\uf0f3": "s", "\uf0f4": "t",
    "\uf0f5": "u", "\uf0f6": "v", "\uf0f7": "w", "\uf0f8": "x",
    "\uf0f9": "y", "\uf0fa": "z",
    "\uf07b": "{", "\uf07c": "|", "\uf07d": "}",
    "\uf05b": "[", "\uf05d": "]",
}
LIGATURES = {
    "\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl", "\ufb03": "ffi", "\ufb04": "ffl",
    "\u2013": "--", "\u2014": "---", "\u2018": "'", "\u2019": "'",
    "\u201c": "``", "\u201d": "''", "\u2212": "-", "\u00ad": "",
    "\uf020": " ",
}

CHAPTER_RE = re.compile(r"^Chapter\s+(\d+)\b", re.I)
SECTION_RE = re.compile(r"^(\d+(?:\.\d+)+)\s+(\S.*)$")
EXERCISE_HEAD_RE = re.compile(r"^Exercises\s*$", re.I)
FIGURE_CAP_RE = re.compile(r"^Figure\s+(\d+\.\d+)\b", re.I)
BOX_HEAD_RE = re.compile(
    r"^(Bases and logs|Two.?s complement|Trees|Entropy|Reductions|Memoization)\b",
    re.I,
)


def font_kind(fontname: str) -> str:
    name = (fontname or "").lower()
    if "cmsy" in name or "msam" in name or "msbm" in name:
        return "sym"
    if "cmmi" in name:
        return "mathit"
    if "cmex" in name:
        return "sym"
    if "cmr" in name or "cmbx" in name or "cmss" in name or "cmtt" in name:
        return "mathrm"
    if "italic" in name or name.endswith("it"):
        return "italic"
    if "bold" in name:
        return "bold"
    if "courier" in name or "cmtt" in name or "mono" in name:
        return "code"
    return "text"


def decode_glyph(ch: str, kind: str) -> str:
    if not ch:
        return ""
    if ch in LIGATURES and kind in {"text", "italic", "bold", "code"}:
        return LIGATURES[ch]
    if kind == "sym":
        return CMSY.get(ch, CMMI.get(ch, ch if ch.isprintable() and ord(ch) < 0xF000 else ""))
    if kind == "mathit":
        if ch in CMMI:
            return CMMI[ch]
        if "\uf000" <= ch <= "\uf0ff":
            # CMMI letters sit at the ASCII code point plus 0xF000, minus the
            # usual Type-1 offset used by this file (0x20 -> space).
            base = chr(ord(ch) - 0xF000)
            return base if base.isalnum() else CMR_PUA.get(ch, "")
        return ch
    if kind == "mathrm":
        if ch in CMR_PUA:
            return CMR_PUA[ch]
        if "\uf000" <= ch <= "\uf0ff":
            return chr(ord(ch) - 0xF000)
        return LIGATURES.get(ch, ch)
    if "\uf000" <= ch <= "\uf0ff":
        return CMR_PUA.get(ch, LIGATURES.get(ch, ""))
    return LIGATURES.get(ch, ch)


def is_math_char(ch: LTChar) -> bool:
    kind = font_kind(ch.fontname)
    text = ch.get_text()
    if kind in {"sym", "mathit", "mathrm"}:
        return True
    if kind == "text" and text in {"=", "+", "<", ">", "|"}:
        return False
    return False


class Token:
    def __init__(self, text, x0, y0, x1, y1, size, kind, raw_font):
        self.text = text
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.size = size
        self.kind = kind
        self.raw_font = raw_font

    @property
    def mid_y(self):
        return (self.y0 + self.y1) / 2

    @property
    def height(self):
        return self.y1 - self.y0


def chars_of(line: LTTextLine) -> list[LTChar]:
    out = []
    for obj in line:
        if isinstance(obj, LTChar):
            out.append(obj)
    return out


def line_tokens(line: LTTextLine) -> list[Token]:
    tokens = []
    for ch in chars_of(line):
        kind = font_kind(ch.fontname)
        text = decode_glyph(ch.get_text(), kind)
        if text == "" and ch.get_text().strip() == "":
            text = " "
            kind = "text"
        tokens.append(Token(text, ch.x0, ch.y0, ch.x1, ch.y1, ch.size, kind, ch.fontname))
    return tokens


def plain_line(line: LTTextLine) -> str:
    return "".join(t.text for t in line_tokens(line)).strip()


def script_of(token: Token, base_size: float, base_y: float) -> str | None:
    if token.size < base_size * 0.82:
        if token.mid_y > base_y + base_size * 0.18:
            return "sup"
        if token.mid_y < base_y - base_size * 0.12:
            return "sub"
    return None


def emit_math_run(tokens: list[Token]) -> str:
    if not tokens:
        return ""
    base_size = max(t.size for t in tokens)
    base_y = sum(t.mid_y for t in tokens if t.size >= base_size * 0.9) / max(
        1, sum(1 for t in tokens if t.size >= base_size * 0.9)
    )
    parts: list[str] = []
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        role = script_of(tok, base_size, base_y)
        if role:
            group = [tok]
            j = i + 1
            while j < len(tokens) and script_of(tokens[j], base_size, base_y) == role:
                if tokens[j].x0 - group[-1].x1 > base_size * 0.8:
                    break
                group.append(tokens[j])
                j += 1
            body = "".join(t.text for t in group).strip()
            op = "^" if role == "sup" else "_"
            if len(body) == 1 or (body.startswith("\\") and " " not in body):
                parts.append(op + body)
            else:
                parts.append(op + "{" + body + "}")
            i = j
            continue
        text = tok.text
        if tok.kind == "mathit" and len(text) == 1 and text.isalpha():
            parts.append(text)
        elif tok.kind == "mathrm" and text.isalpha() and len(text) > 1:
            parts.append(r"\mathrm{" + text + "}")
        else:
            parts.append(text)
        i += 1
    expr = "".join(parts)
    expr = re.sub(r"\s+", " ", expr).strip()
    expr = expr.replace(" .", ".").replace("( ", "(").replace(" )", ")")
    return expr


def line_to_markdown(line: LTTextLine, in_code: bool) -> str:
    tokens = line_tokens(line)
    if not tokens:
        return ""
    if in_code or all(t.kind == "code" for t in tokens if t.text.strip()):
        return "".join(t.text for t in tokens).rstrip()

    # A line that is mostly math, or a short display equation, becomes display math.
    mathish = [t for t in tokens if t.kind in {"sym", "mathit", "mathrm"} or t.text in "=<>+-|"]
    textish = [t for t in tokens if t.kind in {"text", "italic", "bold"} and t.text.strip()]
    if mathish and not textish and len("".join(t.text for t in tokens).strip()) < 80:
        expr = emit_math_run(tokens)
        if expr:
            return "$$" + expr + "$$"

    out = []
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        if tok.kind in {"sym", "mathit", "mathrm"}:
            j = i
            while j < len(tokens) and (
                tokens[j].kind in {"sym", "mathit", "mathrm"}
                or (tokens[j].text in "=<>+-|,()[]{}" and j > i)
            ):
                j += 1
            expr = emit_math_run(tokens[i:j])
            if expr:
                out.append("$" + expr + "$")
            i = j
            continue
        text = tok.text
        if tok.kind == "italic" and text.strip():
            j = i
            while j < len(tokens) and tokens[j].kind == "italic":
                j += 1
            body = "".join(t.text for t in tokens[i:j])
            out.append("*" + body.strip() + "*" if body.strip() else body)
            i = j
            continue
        if tok.kind == "bold" and text.strip():
            j = i
            while j < len(tokens) and tokens[j].kind == "bold":
                j += 1
            body = "".join(t.text for t in tokens[i:j]).strip()
            out.append("**" + body + "**" if body else "")
            i = j
            continue
        out.append(text)
        i += 1
    text = "".join(out)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" \n", "\n", text)
    return text.strip()


def is_header_or_footer(text: str, y0: float, page_h: float) -> bool:
    if y0 > page_h - 70 or y0 < 55:
        if re.fullmatch(r"\d{1,3}", text.strip()):
            return True
        if text.strip() in {"Algorithms", "S. Dasgupta, C. H. Papadimitriou, and U. V. Vazirani"}:
            return True
        if re.match(r"^S\.\s*Dasgupta", text):
            return True
        if text.strip() == "Algorithms":
            return True
    return False


def looks_like_code(line: LTTextLine) -> bool:
    tokens = line_tokens(line)
    if not tokens:
        return False
    code = sum(1 for t in tokens if t.kind == "code")
    return code >= max(3, 0.6 * len([t for t in tokens if t.text.strip()]))


def heading_for(text: str, size: float, body_size: float) -> str | None:
    clean = re.sub(r"\s+", " ", text).strip()
    if not clean or clean.startswith("$$"):
        return None
    m = CHAPTER_RE.match(clean)
    if m and size >= body_size * 1.15:
        return "chapter"
    if SECTION_RE.match(clean) and size >= body_size * 1.05:
        return "section"
    if EXERCISE_HEAD_RE.match(clean):
        return "exercises"
    if size >= body_size * 1.25 and len(clean) < 80 and not clean.endswith("."):
        return "title"
    return None


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-").lower()
    return text[:80] or "chapter"


def collect_drawings(page) -> list[dict]:
    drawings = []
    for obj in page:
        if isinstance(obj, (LTLine, LTRect, LTCurve)):
            drawings.append({
                "kind": type(obj).__name__,
                "bbox": obj.bbox,
                "pts": getattr(obj, "pts", None) or [obj.bbox[:2], obj.bbox[2:]],
            })
        elif isinstance(obj, LTFigure):
            for child in obj:
                if isinstance(child, (LTLine, LTRect, LTCurve)):
                    drawings.append({
                        "kind": type(child).__name__,
                        "bbox": child.bbox,
                        "pts": getattr(child, "pts", None) or [child.bbox[:2], child.bbox[2:]],
                    })
    return drawings


def cluster_drawings(drawings: list[dict], gap: float = 18) -> list[list[dict]]:
    clusters: list[list[dict]] = []
    for d in sorted(drawings, key=lambda x: -x["bbox"][1]):
        x0, y0, x1, y1 = d["bbox"]
        placed = False
        for cluster in clusters:
            cx0 = min(i["bbox"][0] for i in cluster) - gap
            cy0 = min(i["bbox"][1] for i in cluster) - gap
            cx1 = max(i["bbox"][2] for i in cluster) + gap
            cy1 = max(i["bbox"][3] for i in cluster) + gap
            if x0 <= cx1 and x1 >= cx0 and y0 <= cy1 and y1 >= cy0:
                cluster.append(d)
                placed = True
                break
        if not placed:
            clusters.append([d])
    return [c for c in clusters if len(c) >= 2]


def mermaid_from_drawings(cluster: list[dict], caption: str) -> str:
    """Turn a cluster of vector strokes into a readable Mermaid diagram.

    Exact geometry cannot be recovered as a picture, so the diagram records
    the figure's nodes (text is added by the caller) and its edges.
    """
    lines = []
    nodes = []
    for d in cluster:
        pts = d["pts"] or []
        if len(pts) >= 2:
            a, b = pts[0], pts[-1]
            lines.append((a, b, d["kind"]))
        x0, y0, x1, y1 = d["bbox"]
        if (x1 - x0) < 30 and (y1 - y0) < 30 and d["kind"] == "LTRect":
            nodes.append(((x0 + x1) / 2, (y0 + y1) / 2))
    if not lines and not nodes:
        return ""
    # Quantize endpoints so nearby strokes share a node id.
    def key(pt):
        return (round(pt[0] / 12) * 12, round(pt[1] / 12) * 12)

    ids = {}
    def nid(pt):
        k = key(pt)
        if k not in ids:
            ids[k] = f"n{len(ids)}"
        return ids[k]

    edges = []
    for a, b, kind in lines:
        if abs(a[0] - b[0]) < 2 and abs(a[1] - b[1]) < 2:
            continue
        left, right = nid(a), nid(b)
        if left == right:
            continue
        arrow = "-->" if kind != "LTRect" else "---"
        edges.append(f"    {left} {arrow} {right}")
    # Drop duplicate edges and cap the diagram so a hatch-filled figure
    # does not explode into thousands of Mermaid edges.
    uniq = []
    seen = set()
    for e in edges:
        if e not in seen:
            seen.add(e)
            uniq.append(e)
        if len(uniq) >= 40:
            break
    if not uniq and not ids:
        return ""
    title = caption.replace('"', "'") if caption else "figure"
    body = ["```mermaid", "flowchart TD", f'    %% {title}']
    for k, name in ids.items():
        body.append(f'    {name}[" "]')
        if len(body) > 48:
            break
    body.extend(uniq[:40])
    if len(edges) > 40:
        body.append(f"    %% {len(edges) - 40} additional strokes omitted")
    body.append("```")
    return "\n".join(body)


def mermaid_from_labels(labels: list[tuple[str, float, float]], caption: str) -> str:
    """Fallback when a figure is only a cloud of math labels (a graph drawing)."""
    if len(labels) < 2:
        return ""
    labels = sorted(labels, key=lambda t: (-t[2], t[1]))
    ids = []
    for i, (text, x, y) in enumerate(labels[:24]):
        safe = text.replace('"', "'").replace("[", "(").replace("]", ")")
        ids.append((safe, x, y, f"v{i}"))
    edges = []
    for i, a in enumerate(ids):
        for b in ids[i + 1:]:
            dx, dy = a[1] - b[1], a[2] - b[2]
            dist = (dx * dx + dy * dy) ** 0.5
            if 18 <= dist <= 90:
                edges.append((dist, a[3], b[3]))
    edges.sort()
    kept = []
    used = defaultdict(int)
    for dist, u, v in edges:
        if used[u] >= 3 or used[v] >= 3:
            continue
        kept.append(f"    {u} --- {v}")
        used[u] += 1
        used[v] += 1
        if len(kept) >= 30:
            break
    title = (caption or "figure").replace('"', "'")
    lines = ["```mermaid", "flowchart TD", f"    %% {title}"]
    for text, x, y, name in ids:
        lines.append(f'    {name}["{text}"]')
    lines.extend(kept)
    lines.append("```")
    return "\n".join(lines)


def save_image(obj: LTImage, dest: Path) -> str | None:
    if not getattr(obj, "stream", None):
        return None
    data = obj.stream.get_data()
    ext = "bin"
    if data.startswith(b"\x89PNG"):
        ext = "png"
    elif data.startswith(b"\xff\xd8"):
        ext = "jpg"
    path = dest.with_suffix("." + ext)
    path.write_bytes(data)
    return path.name


def page_body_size(lines) -> float:
    sizes = []
    for line in lines:
        for ch in chars_of(line):
            if font_kind(ch.fontname) == "text":
                sizes.append(round(ch.size, 1))
    if not sizes:
        return 11.0
    return max(set(sizes), key=sizes.count)


def iter_lines(page):
    items = []
    for obj in page:
        if isinstance(obj, LTTextBox):
            for line in obj:
                if isinstance(line, LTTextLine):
                    items.append(line)
        elif isinstance(line := obj, LTTextLine):
            items.append(line)
    items.sort(key=lambda ln: (-ln.y1, ln.x0))
    return items


def convert(pdf_path: Path, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    fig_dir = out_dir / "figures"
    fig_dir.mkdir(exist_ok=True)

    chapters: list[dict] = []
    current = {
        "number": "front",
        "title": "Front matter",
        "parts": ["# Front matter\n"],
    }
    chapters.append(current)
    fig_seq = 0

    plumber = pdfplumber.open(str(pdf_path))
    try:
        for page_index, layout in enumerate(extract_pages(str(pdf_path))):
            lines = iter_lines(layout)
            body = page_body_size(lines)
            page_h = layout.height
            drawings = collect_drawings(layout)
            clusters = cluster_drawings(drawings)
            used_clusters = set()

            # Embedded images, rare in this file.
            image_blocks = []
            for obj in layout:
                if isinstance(obj, LTImage) or (isinstance(obj, LTFigure) and any(isinstance(c, LTImage) for c in obj)):
                    image_blocks.append(obj)

            pending_caption = None
            in_code = False
            code_buf: list[str] = []

            def flush_code():
                nonlocal in_code, code_buf
                if code_buf:
                    current["parts"].append("```text\n" + "\n".join(code_buf) + "\n```\n")
                code_buf = []
                in_code = False

            for line in lines:
                raw = plain_line(line)
                if not raw:
                    continue
                if is_header_or_footer(raw, line.y0, page_h):
                    continue

                size = max((ch.size for ch in chars_of(line)), default=body)
                kind = heading_for(raw, size, body)

                if kind == "chapter":
                    flush_code()
                    m = CHAPTER_RE.match(raw)
                    number = m.group(1) if m else "x"
                    title = re.sub(r"^Chapter\s+\d+\s*", "", raw).strip() or f"Chapter {number}"
                    current = {
                        "number": number,
                        "title": title,
                        "parts": [f"# Chapter {number}: {title}\n"],
                    }
                    chapters.append(current)
                    continue

                if kind == "title" and current["number"] == "front" and raw.lower().startswith("preface"):
                    flush_code()
                    current["parts"].append(f"## {raw}\n")
                    continue

                if kind in {"section", "exercises", "title"}:
                    flush_code()
                    level = "###" if kind == "section" and raw.count(".") >= 2 else "##"
                    if kind == "exercises":
                        level = "##"
                    current["parts"].append(f"{level} {raw}\n")
                    continue

                if FIGURE_CAP_RE.match(raw):
                    flush_code()
                    pending_caption = raw
                    # Attach the nearest unused drawing cluster above this caption.
                    cap_top = line.y1
                    best = None
                    best_dy = 1e9
                    for i, cluster in enumerate(clusters):
                        if i in used_clusters:
                            continue
                        bottom = min(d["bbox"][1] for d in cluster)
                        dy = cap_top - bottom
                        if -20 <= dy <= 220 and abs(dy) < best_dy:
                            best, best_dy = i, abs(dy)
                    diagram = ""
                    if best is not None:
                        used_clusters.add(best)
                        diagram = mermaid_from_drawings(clusters[best], raw)
                    if not diagram:
                        # Use math labels sitting just above the caption.
                        labels = []
                        for other in lines:
                            if other.y0 > line.y1 and other.y0 < line.y1 + 180:
                                label = plain_line(other)
                                if label and not FIGURE_CAP_RE.match(label) and len(label) <= 12:
                                    labels.append((label, other.x0, other.y0))
                        diagram = mermaid_from_labels(labels, raw)
                    if not diagram:
                        fig_seq += 1
                        diagram = (
                            "```mermaid\n"
                            "flowchart TD\n"
                            f'    fig["{raw.replace(chr(34), chr(39))}"]\n'
                            "```"
                        )
                    current["parts"].append(diagram + "\n")
                    current["parts"].append(f"*{raw}*\n")
                    pending_caption = None
                    continue

                if looks_like_code(line):
                    in_code = True
                    code_buf.append("".join(t.text for t in line_tokens(line)).rstrip())
                    continue
                if in_code:
                    flush_code()

                md = line_to_markdown(line, in_code=False)
                if not md:
                    continue
                # Join hyphenated line breaks later; keep paragraph breaks on large gaps.
                current["parts"].append(md + "\n")

            flush_code()
            current["parts"].append("\n")
    finally:
        plumber.close()

    written = []
    for chap in chapters:
        text = "\n".join(chap["parts"])
        text = reflow(text)
        name = f"{chap['number'].zfill(2) if chap['number'].isdigit() else chap['number']}-{slugify(chap['title'])}.md"
        path = out_dir / name
        path.write_text(text, encoding="utf-8")
        written.append(path)
    index = ["# Algorithms — Dasgupta, Papadimitriou, Vazirani\n",
             "Converted to Markdown. Math is LaTeX; figures are Mermaid.\n"]
    for path in written:
        index.append(f"- [{path.stem}]({path.name})")
    (out_dir / "README.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    print(f"Wrote {len(written)} chapter files to {out_dir}")


def reflow(text: str) -> str:
    lines = text.splitlines()
    out = []
    buf = []

    def flush():
        if not buf:
            return
        para = " ".join(s.strip() for s in buf)
        para = re.sub(r"(\w)-\s+(\w)", r"\1\2", para)
        para = re.sub(r"\s+", " ", para).strip()
        para = para.replace("$$ ", "$$\n").replace(" $$", "\n$$")
        out.append(para)
        buf.clear()

    for line in lines:
        s = line.strip()
        if not s:
            flush()
            if out and out[-1] != "":
                out.append("")
            continue
        if s.startswith("#") or s.startswith("```") or s.startswith("$$") or s.startswith("*Figure") or s.startswith("- ["):
            flush()
            out.append(s)
            continue
        if s.endswith("$$") and s.startswith("$$"):
            flush()
            out.append(s)
            continue
        buf.append(s)
    flush()
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path, help="Path to Algorithms_Dasgupta.pdf")
    parser.add_argument("-o", "--output", type=Path, default=Path("algorithms_md"))
    args = parser.parse_args()
    convert(args.pdf, args.output)


if __name__ == "__main__":
    main()
