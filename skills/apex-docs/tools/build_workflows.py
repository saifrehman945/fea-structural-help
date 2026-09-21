"""Extract per-tool step-by-step procedures from the Apex in-product help database.

Source: UI/XmlFiles/docSearchData_Apex_1.0_en.xml -> WorkflowInstructionList.
This content is NOT published on the web; it ships with the product. It is the
only genuine numbered-step procedural corpus in the archive.

    python tools/build_workflows.py [path to Documentation]

Writes ~11 grouped files under workflows/, one per functional area, plus
index/workflows-index.md. Grouped rather than one-file-per-tool to stay well
inside the 200-file limit for a web-published skill.
"""
import glob
import os
import re
import sys
import xml.etree.ElementTree as ET
from collections import OrderedDict

from common import (CITE_URL, PKG, find_archive, fix_text, read_config, slug,
                    strip_tags, write)

OUT = os.path.join(PKG, "workflows")

# The markup is rigidly consistent across all 2,143 records:
#   h1    section header ("Keyboard Shortcuts:")
#   table shortcut rows (key, action)
#   h2    "Instructions:" and then one per tool mode/variant
#   h3    "Step N: ..."
#   h4/h5 "Tip N: ..." and notes
HEAD_RE = re.compile(r"<(h[1-6])[^>]*>(.*?)</\1>", re.S | re.I)
ROW_RE = re.compile(r"<tr[^>]*>(.*?)</tr>", re.S | re.I)
CELL_RE = re.compile(r"<t[dh][^>]*>(.*?)</t[dh]>", re.S | re.I)
SECTION_RE = re.compile(r"^(keyboard shortcuts|instructions)\s*:?\s*$", re.I)
STEP_RE = re.compile(r"^step\s*\d+\s*:\s*", re.I)
TIP_RE = re.compile(r"^(tip|note)\s*\d*\s*:\s*", re.I)

# Functional areas. Most tools are placed by their position in the documentation
# book tree; the map below covers tools whose page is missing from the tree.
GROUPS = OrderedDict([
    ("geometry",                  "Geometry"),
    ("meshing",                   "Meshing and finite elements"),
    ("loads-and-constraints",     "Loads and constraints"),
    ("attribution",               "Attribution: materials, properties, fields"),
    ("connections",               "Interactions and connections"),
    ("measurement-and-sensors",   "Measurement, sensors and coordinate tools"),
    ("view-and-selection",        "View, selection and capture"),
    ("generative-design",         "Generative design"),
    ("postprocessing",            "Postprocessing"),
    ("adams",                     "Adams multibody entities"),
    ("other",                     "Other tools"),
])

# Third-level book-tree section -> group key.
TREE_TO_GROUP = {
    "Geometry": "geometry",
    "Finite Elements": "meshing",
    "Loads and Constraints": "loads-and-constraints",
    "Attribution": "attribution",
    "Fields": "attribution",
    "Interactions": "connections",
    "Measurement": "measurement-and-sensors",
    "Probe": "measurement-and-sensors",
    "Sensors and Instrumentation": "measurement-and-sensors",
    "Coordinate Tools": "measurement-and-sensors",
    "Reference System": "measurement-and-sensors",
    "Transform": "measurement-and-sensors",
    "Panel Selector": "view-and-selection",
    "Video and Image Capture": "view-and-selection",
    "Group Tools": "view-and-selection",
    "Design Exploration Tools": "generative-design",
    "Postprocessing": "postprocessing",
}

# Tools whose reference page is absent from the tree (or from every release).
ID_TO_GROUP = {
    "1267": "meshing", "2432": "meshing", "2990": "meshing",
    "1272": "loads-and-constraints", "2024": "loads-and-constraints",
    "2025": "loads-and-constraints", "2093": "loads-and-constraints",
    "2601": "loads-and-constraints", "2729": "loads-and-constraints",
    "2999": "loads-and-constraints", "3001": "loads-and-constraints",
    "3113": "loads-and-constraints", "2454": "loads-and-constraints",
    "1074": "attribution", "3051": "attribution", "1075": "attribution",
    "3127": "connections", "3128": "connections", "2804": "connections",
    "2234": "measurement-and-sensors", "2235": "measurement-and-sensors",
    "2450": "view-and-selection",
    "2291": "generative-design", "2420": "generative-design",
    "2584": "generative-design", "2788": "generative-design",
}


def load_tree(doc):
    """node id -> list of ancestor titles, from each page's parent link."""
    node_dir = os.path.join(doc, "UI", "node")
    parent, title = {}, {}
    for fp in glob.glob(os.path.join(node_dir, "*.html")):
        pid = os.path.splitext(os.path.basename(fp))[0]
        if not pid.isdigit():
            continue
        s = open(fp, encoding="utf-8", errors="replace").read()
        m = re.search(r"(?is)<title>([^<|]*)", s)
        title[pid] = fix_text(m.group(1).strip()) if m else ""
        u = re.search(r'(?is)<a href="(\d+)\.html"[^>]*class="page-up"', s)
        parent[pid] = u.group(1) if u else ""
    def chain(pid):
        out, seen, cur = [], set(), pid
        while cur and cur in parent and cur not in seen:
            seen.add(cur); out.append(title.get(cur, "")); cur = parent[cur]
        out.reverse(); return out
    return {p: chain(p) for p in parent}


def group_of(eid, tree):
    if eid in ID_TO_GROUP:
        return ID_TO_GROUP[eid]
    if eid.startswith("Adams"):
        return "adams"
    a = tree.get(eid, [])
    if len(a) > 3 and a[3] in TREE_TO_GROUP:
        return TREE_TO_GROUP[a[3]]
    for lvl in reversed(a):
        if lvl in TREE_TO_GROUP:
            return TREE_TO_GROUP[lvl]
    return "other"


def anchor(title, eid):
    base = "%s-node-%s" % (title, eid)
    return re.sub(r"[^a-z0-9]+", "-", base.lower()).strip("-")


def body_of(v):
    return v.split("<body>", 1)[-1] if "<body>" in v else v


def parse_shortcuts(body):
    """Pull (key, action) pairs out of the shortcut table."""
    out = []
    for row in ROW_RE.findall(body):
        cells = [strip_tags(c) for c in CELL_RE.findall(row)]
        cells = [c for c in cells if c]
        if len(cells) >= 2:
            key = cells[0].rstrip(":").strip()
            action = " ".join(cells[1:]).strip()
            if key and action:
                out.append((key, action))
    return out


def parse_record(v):
    """-> (variants, tips) where variants is [(name, [steps])]."""
    body = body_of(v)
    variants, tips = [], []
    current = None
    for tag, raw in HEAD_RE.findall(body):
        text = strip_tags(raw)
        if not text:
            continue
        if SECTION_RE.match(text):
            continue
        if STEP_RE.match(text):
            if current is None:
                current = ["", []]
                variants.append(current)
            current[1].append(STEP_RE.sub("", text).strip())
        elif TIP_RE.match(text):
            t = TIP_RE.sub("", text).strip()
            if t:
                tips.append(t)
        elif tag.lower() in ("h2", "h3"):
            # a named mode/variant introduces a fresh step list
            current = [text.rstrip(":").strip(), []]
            variants.append(current)
        elif tag.lower() in ("h4", "h5"):
            tips.append(text)
    variants = [(n, s) for n, s in variants if s]
    return variants, tips


def load_titles(doc, root):
    """EntityId -> best human title, from the XML lists then the node pages."""
    titles = {}
    for listname in ("DocumentationSearchList", "AdvancedTooltipList"):
        sec = root.find(listname)
        if sec is None:
            continue
        for n in sec:
            eid = n.findtext("EntityId") or n.findtext("NodeId")
            t = fix_text((n.findtext("Title") or "").strip())
            if eid and t and eid not in titles:
                titles[eid] = t
    node_dir = os.path.join(doc, "UI", "node")
    if os.path.isdir(node_dir):
        for eid in list(titles) or []:
            pass
    return titles, node_dir


# Some node pages are gated or missing in the archive; their titles are useless
# even though the workflow content itself is fine.
JUNK_TITLE = re.compile(r"^\s*(access denied|page not found|untitled)?\s*$", re.I)


def title_from_page(node_dir, eid):
    p = os.path.join(node_dir, "%s.html" % eid)
    if not os.path.exists(p):
        return ""
    s = open(p, encoding="utf-8", errors="replace").read(4000)
    m = re.search(r"(?is)<title>([^<|]*)", s)
    t = fix_text(m.group(1).strip()) if m else ""
    return "" if JUNK_TITLE.match(t) else t


def title_from_variant(name):
    """'Create Constant Pressure - Auto mode' -> 'Create Constant Pressure'."""
    t = re.sub(r"\s*[-–—]\s*(auto|manual)(\s*mode)?\s*$", "", name, flags=re.I)
    t = re.sub(r"\s+tool\s*$", "", t, flags=re.I)
    return t.strip()


def main():
    doc = find_archive(sys.argv[1] if len(sys.argv) > 1 else None)
    bundle = read_config()["bundle"]
    xml = os.path.join(doc, "UI", "XmlFiles", "docSearchData_Apex_1.0_en.xml")
    if not os.path.exists(xml):
        sys.exit("missing %s" % xml)

    root = ET.parse(xml).getroot()
    wl = root.find("WorkflowInstructionList")
    if wl is None:
        sys.exit("no WorkflowInstructionList in %s" % xml)

    titles, node_dir = load_titles(doc, root)

    # group records by tool
    by_tool = OrderedDict()
    for n in wl:
        eid = (n.findtext("EntityId") or "").strip()
        if not eid:
            continue
        by_tool.setdefault(eid, []).append(n)

    tree = load_tree(doc)

    buckets = {k: [] for k in GROUPS}
    skipped = 0
    total_steps = 0
    index_rows = []

    for eid, recs in by_tool.items():
        variants, tips = OrderedDict(), OrderedDict()
        shortcuts = OrderedDict()
        for n in recs:
            v = n.findtext("WorkflowValue") or ""
            body = body_of(v)
            for k, a in parse_shortcuts(body):
                shortcuts.setdefault(k, a)
            vs, ts = parse_record(v)
            for name, steps in vs:
                # the ~3x record inflation repeats identical variants verbatim
                key = (name.lower(), tuple(s.lower() for s in steps))
                variants.setdefault(key, (name, steps))
            for t in ts:
                tips.setdefault(t.lower(), t)

        if not variants:
            skipped += 1
            continue

        first_variant = next(iter(variants.values()))[0]
        title = (titles.get(eid)
                 or title_from_page(node_dir, eid)
                 or title_from_variant(first_variant)
                 or ("Tool %s" % eid))
        title = re.sub(r"\s*\|.*$", "", title).strip()

        nsteps = sum(len(s) for _, s in variants.values())
        total_steps += nsteps
        g = group_of(eid, tree)
        buckets[g].append((title, eid, shortcuts, variants, tips))
        index_rows.append((title, eid, g, nsteps))

    # ---- one file per functional area ----
    written = 0
    for key, heading in GROUPS.items():
        entries = sorted(buckets[key], key=lambda e: e[0].lower())
        if not entries:
            continue
        L = ["# %s — tool procedures" % heading, "",
             "Numbered procedures from the MSC Apex in-product workflow database "
             "(`docSearchData_Apex_1.0_en.xml`). **This content is not published "
             "on the web** — it ships with the installation, so it cannot be "
             "fetched and has no online equivalent.", "",
             "Read `references/interaction-conventions.md` first: MMB ends a "
             "selection stage in most tools, and Auto vs Manual variants differ by "
             "exactly that click.", "",
             "## Contents", ""]
        for title, eid, _, _, _ in entries:
            L.append("- [%s](#%s)" % (title, anchor(title, eid)))
        L.append("")

        for title, eid, shortcuts, variants, tips in entries:
            L.append("---")
            L.append("")
            L.append("## %s (node %s)" % (title, eid))
            L.append("")
            if str(eid).isdigit():
                L.append("Reference page: %s"
                         % CITE_URL.format(bundle=bundle, id=eid))
                L.append("")
            if shortcuts:
                L += ["**Keyboard shortcuts**", "", "| Key | Action |", "|---|---|"]
                for k, a in shortcuts.items():
                    L.append("| `%s` | %s |" % (k, a))
                L.append("")
            multi = len(variants) > 1
            for name, steps in variants.values():
                if multi or name:
                    L.append("**%s**" % (name or "Procedure"))
                    L.append("")
                for i, s in enumerate(steps, 1):
                    L.append("%d. %s" % (i, s))
                L.append("")
            if tips:
                L.append("Tips:")
                L.append("")
                for t in tips.values():
                    L.append("- %s" % t)
                L.append("")

        write(os.path.join(OUT, "%s.md" % key), "\n".join(L).rstrip() + "\n")
        written += 1

    # ---- index ----
    L = ["# Workflow index", "",
         "Per-tool numbered procedures, grouped by functional area. **This "
         "content exists nowhere online** — it is extracted from the Apex "
         "in-product help database.", "",
         "Check here before fetching a reference page: the web pages describe "
         "what a control *is*, these describe what to actually *do*. Of 589 "
         "documentation pages, exactly one contains the string \"Step 1\".", "",
         "| Tool | Node | Steps | Procedure |", "|---|---|---|---|"]
    for title, eid, g, nsteps in sorted(index_rows, key=lambda r: r[0].lower()):
        L.append("| %s | `%s` | %d | [%s](../workflows/%s.md#%s) |"
                 % (title, eid, nsteps, GROUPS[g], g, anchor(title, eid)))
    L += ["", "## Files", "", "| File | Area | Tools |", "|---|---|---|"]
    for key, heading in GROUPS.items():
        n = len(buckets[key])
        if n:
            L.append("| [%s.md](../workflows/%s.md) | %s | %d |" % (key, key, heading, n))
    write(os.path.join(PKG, "index", "workflows-index.md"), "\n".join(L) + "\n")

    print("workflow records : %d" % len(wl))
    print("tools            : %d" % len(index_rows))
    print("tools skipped    : %d (no steps)" % skipped)
    print("total steps      : %d" % total_steps)
    print("group files      : %d" % written)
    for key, heading in GROUPS.items():
        if buckets[key]:
            print("   %-26s %3d" % (key, len(buckets[key])))


if __name__ == "__main__":
    main()
