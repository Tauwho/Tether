"""Build YouTube captions (SRT) for the demo video from the narration script.

Usage: python scripts/srt.py   -> video/youtube/Tether-Demo.en.srt

SPANS holds the start and end of each narration line in the final cut, measured with
ffmpeg silencedetect on "video/Tether Demo v2.mp4" (-40 dB, 0.6 s). Re-measure and edit
SPANS if the edit changes. Text is the on-screen form of docs/VIDEO.md section 5.
"""
import math
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "video" / "youtube" / "Tether-Demo.en.srt"

SPANS = [
    (0.67, 13.47, "Here's a ticket asking the payment service to retry failed transactions exactly five times. Two clicks away, the team's accepted decision says no more than three. Nobody notices until it ships."),
    (17.26, 27.82, "Tether is a Forge app for Jira and Confluence. It checks a ticket's technical requirements against the decisions your team already recorded, and shows you the exact evidence."),
    (31.54, 45.29, "To make this easy to test, an admin grants access once, then clicks Load demo data. In about a minute, Tether creates a demo project, a decision space and thirty sample tickets. We've sped that part up."),
    (48.66, 56.06, "On PAY-1, I click Check implementation context. The check runs in a background queue, so I've trimmed the wait."),
    (58.10, 70.24, "Conflict. On the left, the sentence from the ticket. On the right, the sentence from the decision, with a link to the page. Both quotes are checked word for word against their source."),
    (72.18, 84.77, "It also tells you what it didn't check: one of two requirements had no matching decision. And it shows why this decision counts. It's accepted, it applies to the payment service, and it replaced an older one."),
    (87.53, 97.64, "Not every different number is a conflict. Four attempts, including the first, is the same as three retries. Tether does that arithmetic in code, not in a prompt."),
    (99.16, 102.81, "When the counting is unclear, it says Needs review instead of guessing."),
    (103.99, 111.10, "And when part of a ticket has no decision behind it, it says so. Insufficient evidence is never shown as a pass."),
    (113.54, 125.23, "Tether never edits the ticket or the decision. If you want to follow up, it drafts a clarification issue. You review it, change what you like, and confirm. It's created as you, linked to both."),
    (129.55, 140.08, "Decisions change. When someone edits the retry decision, the next time anyone opens PAY-1, Tether flags that a decision it relied on has changed, and offers a re-check."),
    (144.56, 157.09, "The same check runs inside Rovo. The Tether agent uses our actions and a skill, so you can ask in chat. Here it reaches the same result for PAY-2: one requirement checked, one with no decision."),
    (161.56, 173.58, "Tether also exposes its tools over MCP. Here, Claude Code calls check issue consistency and gets the same conflict, with the quotes and links. This one is recorded on our development site."),
    (177.46, 188.24, "To find decisions linked to a ticket, Tether asks Teamwork Graph. Everything runs on Forge, and the language model calls use Forge LLMs, so nothing leaves Atlassian."),
    (191.47, 202.81, "On our thirty team-written test scenarios, all thirty pass. That shows it handles the cases we designed, not real-world accuracy. Tether: tickets that stay tethered."),
]

MAX_CUE = 84  # two lines of about 42 characters


def split_even(text: str) -> list[str]:
    """Split a sentence into roughly equal parts of at most MAX_CUE characters."""
    parts = math.ceil(len(text) / MAX_CUE)
    words, out, target = text.split(), [], len(text) / parts
    cur = ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > target and len(out) < parts - 1:
            out.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    out.append(cur)
    return out


def cues(text: str) -> list[str]:
    out = []
    for s in re.split(r"(?<=[.!?])\s+", text):
        out.extend(split_even(s) if len(s) > MAX_CUE else [s])
    # Fold very short cues (like "Conflict.") into the next one only when it still fits.
    merged = []
    for c in out:
        if merged and len(merged[-1]) < 20 and len(merged[-1]) + 1 + len(c) <= MAX_CUE:
            merged[-1] = f"{merged[-1]} {c}"
        else:
            merged.append(c)
    return merged


def wrap(c: str, width: int = 42) -> str:
    if len(c) <= width:
        return c
    mid = len(c) // 2
    left, right = c.rfind(" ", 0, mid + 1), c.find(" ", mid)
    i = left if right == -1 or (left != -1 and mid - left <= right - mid) else right
    return c[:i] + "\n" + c[i + 1:]


def stamp(t: float) -> str:
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def main() -> None:
    blocks, n = [], 0
    for start, end, text in SPANS:
        cs = cues(text)
        total, t = sum(len(c) for c in cs), start
        for c in cs:
            d = (end - start) * len(c) / total
            n += 1
            blocks.append(f"{n}\n{stamp(t)} --> {stamp(min(t + d, end))}\n{wrap(c)}\n")
            t += d
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(blocks), encoding="utf-8")
    print(f"{n} cues -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
