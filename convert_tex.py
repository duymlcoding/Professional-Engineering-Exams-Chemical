"""Convert PE LaTeX study-guide files to Jupyter Book Markdown."""
import re, pathlib, textwrap


def strip_nested_braces(cmd, src):
    """Remove \\cmd{...} where the arg may contain nested braces."""
    result = []
    i = 0
    pat = re.compile(r'\\' + re.escape(cmd) + r'\s*\{')
    while i < len(src):
        m = pat.search(src, i)
        if not m:
            result.append(src[i:])
            break
        result.append(src[i:m.start()])
        # find matching closing brace
        depth = 1
        j = m.end()
        while j < len(src) and depth > 0:
            if src[j] == '{' and (j == 0 or src[j-1] != '\\'):
                depth += 1
            elif src[j] == '}' and (j == 0 or src[j-1] != '\\'):
                depth -= 1
            j += 1
        inner = src[m.end():j-1]
        result.append(inner)  # keep the content, drop \cmd{ and }
        i = j
    return ''.join(result)


def wrap_nested_braces(cmd, prefix, suffix, src):
    """Replace \\cmd{...} with prefix+content+suffix; handles nested braces."""
    result = []
    i = 0
    pat = re.compile(r'\\' + re.escape(cmd) + r'\s*\{')
    while i < len(src):
        m = pat.search(src, i)
        if not m:
            result.append(src[i:])
            break
        result.append(src[i:m.start()])
        depth = 1
        j = m.end()
        while j < len(src) and depth > 0:
            if src[j] == '{' and (j == 0 or src[j-1] != '\\'):
                depth += 1
            elif src[j] == '}' and (j == 0 or src[j-1] != '\\'):
                depth -= 1
            j += 1
        inner = src[m.end():j-1]
        result.append(prefix + inner + suffix)
        i = j
    return ''.join(result)


def strip_nested_braces_no_content(cmd, src):
    """Remove \\cmd{...} entirely (content also removed)."""
    result = []
    i = 0
    pat = re.compile(r'\\' + re.escape(cmd) + r'\s*\{')
    while i < len(src):
        m = pat.search(src, i)
        if not m:
            result.append(src[i:])
            break
        result.append(src[i:m.start()])
        depth = 1
        j = m.end()
        while j < len(src) and depth > 0:
            if src[j] == '{' and (j == 0 or src[j-1] != '\\'):
                depth += 1
            elif src[j] == '}' and (j == 0 or src[j-1] != '\\'):
                depth -= 1
            j += 1
        i = j
    return ''.join(result)


def find_matching_brace(src, start):
    """Return index after the matching } for the { at start."""
    depth = 1
    j = start + 1
    while j < len(src) and depth > 0:
        if src[j] == '{' and src[j - 1] != '\\':
            depth += 1
        elif src[j] == '}' and src[j - 1] != '\\':
            depth -= 1
        j += 1
    return j


def replace_heading(cmd, prefix, src):
    """Convert a LaTeX heading command whose title may contain nested braces."""
    result = []
    i = 0
    pat = re.compile(r'\\' + re.escape(cmd) + r'\*?\s*\{')
    while i < len(src):
        m = pat.search(src, i)
        if not m:
            result.append(src[i:])
            break
        result.append(src[i:m.start()])
        end = find_matching_brace(src, m.end() - 1)
        title = src[m.end():end - 1].strip()
        result.append(prefix + title)
        i = end
    return ''.join(result)


def replace_exampleboxes(src, label_prefix):
    """Convert examplebox environments whose titles may contain nested math."""
    result = []
    i = 0
    count = 0
    pat = re.compile(r'\\begin\{examplebox\}(?:\[[^\]]*\])?\s*\{')
    end_pat = re.compile(r'\\end\{examplebox\}')
    while i < len(src):
        m = pat.search(src, i)
        if not m:
            result.append(src[i:])
            break
        result.append(src[i:m.start()])
        title_end = find_matching_brace(src, m.end() - 1)
        title = src[m.end():title_end - 1].strip()
        end_m = end_pat.search(src, title_end)
        if not end_m:
            result.append(src[m.start():])
            break
        body = src[title_end:end_m.start()].strip()
        label = f'{label_prefix}-example-{count}'
        result.append(format_examplebox(title, body, label))
        count += 1
        i = end_m.end()
    return ''.join(result)


def protect_math(src):
    """Temporarily stash math so text/table cleanup cannot alter TeX syntax."""
    math_blocks = {}

    def stash(m):
        key = f'@@MATH_BLOCK_{len(math_blocks)}@@'
        math_blocks[key] = m.group(0)
        return key

    # Display math emitted by this converter has delimiters on their own lines.
    # Do not match adjacent inline math like m$^2$$\cdot$K as a $$...$$ block.
    src = re.sub(r'(?ms)^[ \t]*\$\$[ \t]*\n.*?\n[ \t]*\$\$[ \t]*(?=\n|$)', stash, src)
    src = re.sub(r'\$[^$\n]+\$', stash, src)
    return src, math_blocks


def restore_math(src, math_blocks):
    """Restore stashed math in reverse order in case placeholders were nested."""
    for key in reversed(list(math_blocks)):
        src = src.replace(key, math_blocks[key])
    return src


def normalize_display_math_spacing(src):
    """Ensure $$ display blocks are separated from prose for MyST parsing."""
    out = []
    in_display = False
    lines = src.splitlines()

    for i, line in enumerate(lines):
        if line.strip() != '$$':
            if in_display and not line.strip() and out and out[-1].strip() == '$$':
                continue
            out.append(line)
            continue

        if not in_display:
            if out and out[-1].strip():
                out.append('')
            out.append('$$')
            in_display = True
        else:
            while out and not out[-1].strip():
                out.pop()
            out.append('$$')
            in_display = False
            if i + 1 < len(lines) and lines[i + 1].strip():
                out.append('')

    return '\n'.join(out)


def convert_file(tex_path: pathlib.Path, md_path: pathlib.Path, title: str, frontmatter: str):
    src = tex_path.read_text(encoding='utf-8')

    # ── 1. Strip preamble / \begin{document} / \end{document} ───────────────
    src = re.sub(r'(?s)^.*?\\begin\{document\}', '', src)
    src = re.sub(r'\\end\{document\}.*$', '', src, flags=re.DOTALL)

    # ── 2. Strip title block (\begin{center}…\end{center} + \hrule) ─────────
    src = re.sub(r'(?s)\\begin\{center\}.*?\\end\{center\}', '', src)
    src = re.sub(r'\\hrule\s*', '', src)
    src = re.sub(r'\\vspace\{[^}]+\}', '', src)

    # ── 3. Strip comments ────────────────────────────────────────────────────
    # Only strip % NOT preceded by \ (don't eat escaped percent signs)
    src = re.sub(r'(?m)^%.*\n', '', src)
    src = re.sub(r'(?m)(?<!\\)\s*%.*$', '', src)

    # ── 4. Sections → markdown headings ─────────────────────────────────────
    src = replace_heading('section', '## ', src)
    src = replace_heading('subsection', '### ', src)
    src = replace_heading('subsubsection', '#### ', src)

    # ── 4b. LaTeX quote ligatures — before box conversion to protect ``` fences
    src = src.replace('``', '"')
    src = src.replace("''", '"')

    # ── 4c. LaTeX special text characters — before text formatting ───────────
    src = re.sub(r'\\AA\s*\{?\}?', 'Å', src)
    src = re.sub(r'\\"a', 'ä', src)
    src = re.sub(r'\\"o', 'ö', src)
    src = re.sub(r'\\"u', 'ü', src)
    src = re.sub(r'\\"A', 'Ä', src)
    src = re.sub(r'\\"O', 'Ö', src)
    src = re.sub(r'\\"U', 'Ü', src)
    src = re.sub(r"\\'\{a\}", 'á', src)
    src = re.sub(r"\\'\{e\}", 'é', src)
    src = re.sub(r"\\'\{o\}", 'ó', src)
    src = re.sub(r'\\c\{c\}', 'ç', src)

    # ── 5. Custom boxes ──────────────────────────────────────────────────────
    src = replace_exampleboxes(src, md_path.stem)
    src = re.sub(
        r'\\begin\{stepbox\}(?:\[[^\]]*\])?((?:[^\\]|\\(?!end\{stepbox\}))*?)\\end\{stepbox\}',
        lambda m: wrap_box('dropdown', 'Solution Steps', m.group(1)),
        src, flags=re.DOTALL
    )
    def clean_title(t):
        """Strip outer {braces} LaTeX uses when title contains commas."""
        t = (t or '').strip()
        if t.startswith('{') and t.endswith('}'):
            t = t[1:-1]
        return t

    src = re.sub(
        r'\\begin\{conceptbox\}(?:\[title=([^\]]*)\])?((?:[^\\]|\\(?!end\{conceptbox\}))*?)\\end\{conceptbox\}',
        lambda m: wrap_box('note', clean_title(m.group(1)), m.group(2)),
        src, flags=re.DOTALL
    )
    src = re.sub(
        r'\\begin\{formulabox\}(?:\[title=([^\]]*)\])?((?:[^\\]|\\(?!end\{formulabox\}))*?)\\end\{formulabox\}',
        lambda m: wrap_box('important', clean_title(m.group(1)), m.group(2)),
        src, flags=re.DOTALL
    )
    src = re.sub(
        r'\\begin\{keybox\}(?:\[title=([^\]]*)\])?((?:[^\\]|\\(?!end\{keybox\}))*?)\\end\{keybox\}',
        lambda m: wrap_box('tip', clean_title(m.group(1)), m.group(2)),
        src, flags=re.DOTALL
    )

    # ── 6. Math environments ─────────────────────────────────────────────────
    # standalone $$...$$ FIRST (before align/equation, to avoid double-wrapping)
    # Only match when content is non-empty and on one line
    src = re.sub(r'(?m)^\s*\$\$\s*(\S[^\n]*?)\s*\$\$\s*$',
                 lambda m: '\n\n$$\n' + m.group(1).strip() + '\n$$\n\n',
                 src)
    # Strip $$ wrappers already surrounding \begin{align} (from LaTeX $$..align..$$ style)
    src = re.sub(r'\$\$\s*\n(\\begin\{align\*?\}.*?\\end\{align\*?\})\s*\n\s*\$\$',
                 r'\1', src, flags=re.DOTALL)
    # align* / align → $$\begin{align}...\end{align}$$
    src = re.sub(r'\\begin\{align\*?\}(.*?)\\end\{align\*?\}',
                 lambda m: '\n\n$$\n\\begin{align}\n' + m.group(1).strip() + '\n\\end{align}\n$$\n\n',
                 src, flags=re.DOTALL)
    src = re.sub(r'\\begin\{equation\*?\}(.*?)\\end\{equation\*?\}',
                 lambda m: '\n\n$$\n' + m.group(1).strip() + '\n$$\n\n',
                 src, flags=re.DOTALL)
    # \[...\] displaymath
    src = re.sub(r'\\\[(.*?)\\\]',
                 lambda m: '\n\n$$\n' + m.group(1).strip() + '\n$$\n\n',
                 src, flags=re.DOTALL)

    # ── 7. Lists ─────────────────────────────────────────────────────────────
    src = re.sub(r'\\begin\{itemize\}(?:\[[^\]]*\])?', '', src)
    src = re.sub(r'\\end\{itemize\}', '', src)
    src = re.sub(r'\\begin\{enumerate\}(?:\[[^\]]*\])?', '', src)
    src = re.sub(r'\\end\{enumerate\}', '', src)
    src = re.sub(r'\\item\[([^\]]+)\]', r'- **\1**', src)
    src = re.sub(r'\\item\s+', '- ', src)

    # ── 8. Text formatting (balanced-brace to handle nested $...$ inside args) ─
    src = wrap_nested_braces('textbf', '**', '**', src)
    src = wrap_nested_braces('textit', '*', '*', src)
    src = wrap_nested_braces('emph', '*', '*', src)
    src = wrap_nested_braces('texttt', '`', '`', src)
    src = wrap_nested_braces('underline', '**', '**', src)
    src = re.sub(r'\\color\{[^}]+\}', '', src)
    src = re.sub(r'\{\\color\{[^}]+\}([^}]*)\}', r'\1', src)

    # ── 9. Tables ────────────────────────────────────────────────────────────
    src = re.sub(r'\\begin\{tabular\}\{[^}]+\}', '', src)
    src = re.sub(r'\\end\{tabular\}', '', src)
    src = re.sub(r'\\hline', '', src)
    # Protect math blocks so & alignment markers inside align are not turned into |
    src, _math_stash = protect_math(src)
    src = re.sub(r' & ', ' | ', src)
    src = re.sub(r'\\\\(\s*)', r'\n', src)
    src = restore_math(src, _math_stash)

    # ── 9b. Backslash-space (e.g.\ abbreviation spacing) ─────────────────────
    src = re.sub(r'\\ ', ' ', src)

    # ── 10. Misc LaTeX commands ──────────────────────────────────────────────
    src = re.sub(r'\\noindent\s*', '', src)
    src = re.sub(r'\\medskip\s*', '\n', src)
    src = re.sub(r'\\bigskip\s*', '\n\n', src)
    src = re.sub(r'\\smallskip\s*', '\n', src)
    src = re.sub(r'\\newline\s*', '\n', src)
    src = re.sub(r'\\par\s*', '\n\n', src)
    src = re.sub(r'\\centering\s*', '', src)
    src = re.sub(r'\\begin\{center\}(.*?)\\end\{center\}', r'\1', src, flags=re.DOTALL)
    src = re.sub(r'\\rule\{[^}]+\}\{[^}]+\}', '', src)

    # Special characters (keep \{ and \} as-is — they render in MathJax)
    src = src.replace(r'\&', '&')
    src = src.replace(r'\%', r'\%')   # keep \% — MathJax renders it as %, bare % is a comment char
    src = src.replace(r'\$', r'\$')
    src = src.replace(r'\_', '_')
    src = src.replace(r'\#', '#')
    # Convert --- to hyphen (no em-dashes per user preference), then -- to hyphen
    src = src.replace('---', ' - ')
    src = src.replace('--', '-')
    src = src.replace(r'\ldots', '...')
    src = src.replace(r'\dots', '...')

    # Non-breaking space ~ → space
    src = re.sub(r'(?<!\\)~', ' ', src)


    # Remove \label, \ref, \cite, \footnote etc.
    src = re.sub(r'\\label\{[^}]+\}', '', src)
    src = re.sub(r'\\ref\{[^}]+\}', '', src)
    src = re.sub(r'\\cite\{[^}]+\}', '', src)
    src = re.sub(r'\\footnote\{[^}]+\}', '', src)
    src = re.sub(r'\\pagebreak\s*', '', src)
    src = re.sub(r'\\newpage\s*', '', src)
    src = re.sub(r'\\clearpage\s*', '', src)

    # ── 11. Math commands ─────────────────────────────────────────────────────
    # \boxed{...} with possible nested braces — keep content
    src = strip_nested_braces('boxed', src)
    # Math font commands — keep content (safe in MathJax)
    for cmd in ('mathcal', 'mathbb', 'mathbf', 'mathit', 'mathsf', 'mathtt',
                'boldsymbol', 'hat', 'bar', 'vec', 'tilde', 'dot', 'ddot',
                'widehat', 'widetilde', 'overline', 'underbrace', 'overbrace'):
        src = re.sub(r'\\' + cmd + r'\{([^}]+)\}', r'\1', src)
    # \text{...} inside math — keep content; add space when following \circ to avoid \circX
    src = re.sub(r'(\\circ)\\text\{([^}]*)\}', r'\1 \2', src)
    src = re.sub(r'\\text\{([^}]*)\}', r'\1', src)
    # \left and \right — remove command, keep delimiter
    src = re.sub(r'\\(?:left|right)\s*([(\[|\])\.])', r'\1', src)
    src = re.sub(r'\\(?:left|right)\s*\\([{}|])', r'\\\1', src)
    src = re.sub(r'\\(?:left|right)\s*\\.', '', src)  # \left\langle etc
    # Math spacing: \, \; \! → space (avoids \tau\,s → \taus)
    src = re.sub(r'\\[,;!]', ' ', src)
    # \quad \qquad → space
    src = re.sub(r'\\q?quad\b', ' ', src)
    # \: \> → space
    src = re.sub(r'\\[>:]', ' ', src)

    # ── 12. Remaining unknown commands ───────────────────────────────────────
    src = re.sub(r'\\(?:large|Large|LARGE|huge|Huge|small|footnotesize|normalsize|bfseries|sffamily|normalfont)\s*', '', src)
    src = re.sub(r'\\(?:vspace|hspace|setlength|setcounter|addtolength)\{[^}]*\}(\{[^}]*\})?', '', src)
    src = re.sub(r'\\(?:pagestyle|fancyhf|fancyhead|fancyfoot|renewcommand|titleformat)\{[^}]*\}[^{]*(\{[^}]*\})*', '', src)

    # ── 13. Clean up whitespace ───────────────────────────────────────────────
    # Remove leading spaces/tabs on lines (prevents Markdown from treating
    # indented LaTeX source lines as code blocks)
    src = re.sub(r'(?m)^[ \t]+(?=[^\s])', '', src)
    src = re.sub(r'\n{4,}', '\n\n\n', src)
    src = re.sub(r'[ \t]+\n', '\n', src)
    src = normalize_display_math_spacing(src)
    src = src.strip()

    # ── 14. Write output ─────────────────────────────────────────────────────
    out = frontmatter + '\n\n' + src + '\n'
    md_path.write_text(out, encoding='utf-8')
    print(f'  Written: {md_path}')


def wrap_box(kind, box_title, body):
    body = convert_body(body or '')
    body = body.strip()
    if kind == 'dropdown':
        hdr = f'```{{dropdown}} {box_title}'.rstrip()
    else:
        if box_title:
            hdr = f'```{{{kind}}}\n**{box_title.strip()}**'
        else:
            hdr = f'```{{{kind}}}'
    return f'{hdr}\n{body}\n```\n'


def replace_examplebox_inner(m):
    etitle = m.group(1).strip()
    body   = m.group(2).strip()
    return format_examplebox(etitle, body)


def format_examplebox(etitle, body, label=None):
    body   = convert_body(body)
    label_block = f':label: {label}\n\n' if label else ''
    return (
        f'```{{prf:example}} {etitle}\n'
        f'{label_block}'
        f'{body}\n'
        f'```\n'
    )


def convert_body(body):
    """Apply inline conversions to box body content."""
    body = wrap_nested_braces('textbf', '**', '**', body)
    body = wrap_nested_braces('textit', '*', '*', body)
    body = wrap_nested_braces('emph', '*', '*', body)
    body = wrap_nested_braces('texttt', '`', '`', body)
    body = re.sub(r'\\item\[([^\]]+)\]\s*', r'\n- **\1** ', body)
    body = re.sub(r'\\item\s+', '\n- ', body)
    body = re.sub(r'\\begin\{itemize\}(?:\[[^\]]*\])?', '', body)
    body = re.sub(r'\\end\{itemize\}', '', body)
    body = re.sub(r'\\begin\{enumerate\}(?:\[[^\]]*\])?', '', body)
    body = re.sub(r'\\end\{enumerate\}', '', body)
    # Math environments
    body = re.sub(r'\\\[(.*?)\\\]',
                  lambda m: '\n\n$$\n' + m.group(1).strip() + '\n$$\n\n',
                  body, flags=re.DOTALL)
    body = re.sub(r'\$\$\s*\n(\\begin\{align\*?\}.*?\\end\{align\*?\})\s*\n\s*\$\$',
                  r'\1', body, flags=re.DOTALL)
    body = re.sub(r'\\begin\{align\*?\}(.*?)\\end\{align\*?\}',
                  lambda m: '\n\n$$\n\\begin{align}\n' + m.group(1).strip() + '\n\\end{align}\n$$\n\n',
                  body, flags=re.DOTALL)
    # standalone $$...$$ inside box (non-empty content only)
    body = re.sub(r'(?m)^\s*\$\$\s*(\S[^\n]*?)\s*\$\$\s*$',
                  lambda m: '\n\n$$\n' + m.group(1).strip() + '\n$$\n\n',
                  body)
    # Special chars
    body = body.replace(r'\&', '&')
    body = body.replace(r'\%', r'\%')   # keep \% — MathJax renders it as %, bare % is a comment char
    body = body.replace(r'\_', '_')
    body = body.replace('---', ' - ')
    body = body.replace('--', '-')
    body = body.replace('``', '"')
    body = body.replace("''", '"')
    # Math commands
    body = strip_nested_braces('boxed', body)
    for cmd in ('mathcal', 'mathbb', 'mathbf', 'mathit', 'mathsf', 'mathtt',
                'boldsymbol', 'hat', 'bar', 'vec', 'tilde', 'dot', 'ddot',
                'widehat', 'widetilde', 'overline', 'underbrace'):
        body = re.sub(r'\\' + cmd + r'\{([^}]+)\}', r'\1', body)
    body = re.sub(r'(\\circ)\\text\{([^}]*)\}', r'\1 \2', body)
    body = re.sub(r'\\text\{([^}]*)\}', r'\1', body)
    body = re.sub(r'\\(?:left|right)\s*([(\[|\])\.])', r'\1', body)
    body = re.sub(r'\\(?:left|right)\s*\\([{}|])', r'\\\1', body)
    body = re.sub(r'\\[,;!]', ' ', body)
    body = re.sub(r'\\q?quad\b', ' ', body)
    body = re.sub(r'\\[>:]', ' ', body)
    body = re.sub(r'\\ ', ' ', body)
    # Strip font/size commands
    body = re.sub(r'\\(?:large|Large|LARGE|huge|Huge|small|normalsize|bfseries|sffamily|normalfont)\s*', '', body)
    body = re.sub(r'\\color\{[^}]+\}', '', body)
    body = re.sub(r'\n{3,}', '\n\n', body)
    # Dedent: remove leading spaces from all lines to prevent Markdown code blocks
    body = re.sub(r'(?m)^[ \t]+', '', body)
    body = normalize_display_math_spacing(body)
    return body.strip()


# ── File definitions ─────────────────────────────────────────────────────────
BASE = pathlib.Path('/Users/thinhdho/Desktop/PE')
OUT  = pathlib.Path('/Users/thinhdho/Desktop/PE_Chemical/mynotes/chapters')

files = [
    (
        BASE / 'Process_Design.tex',
        OUT  / 'processdesign.md',
        'Process Design',
        '---\ntitle: "Process Design"\nauthor: "PE Study Guide"\ndate: "2025"\n---\n\n# Process Design',
    ),
    (
        BASE / 'Process_Equipment_Design.tex',
        OUT  / 'processequipmentdesign.md',
        'Process Equipment Design',
        '---\ntitle: "Process Equipment Design"\nauthor: "PE Study Guide"\ndate: "2025"\n---\n\n# Process Equipment Design',
    ),
    (
        BASE / 'Instrumentation_and_Process_Control.tex',
        OUT  / 'instrumentationandcontrol.md',
        'Instrumentation & Process Control',
        '---\ntitle: "Instrumentation & Process Control"\nauthor: "PE Study Guide"\ndate: "2025"\n---\n\n# Instrumentation & Process Control',
    ),
    (
        BASE / 'Materials_of_Construction.tex',
        OUT  / 'materialsofconstruction.md',
        'Materials of Construction',
        '---\ntitle: "Materials of Construction"\nauthor: "PE Study Guide"\ndate: "2025"\n---\n\n# Materials of Construction',
    ),
]

for tex, md, title, fm in files:
    print(f'Converting: {tex.name}')
    convert_file(tex, md, title, fm)

print('\nDone.')
