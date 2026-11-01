"""Stylistic profile of a review (appendix §5.3, §7.6): words, hedges per 1,000 words, nominalizations per 100 words,
Flesch Reading Ease (syllables by a vowel-group heuristic). Usage: python3 style_metrics.py FILE [FILE ...]"""
import re, sys
HEDGES = ["may", "might", "could", "perhaps", "possibly", "arguably", "somewhat", "appears", "appear", "seems", "seem",
          "suggest", "suggests", "likely", "unlikely", "unclear", "potentially", "i wonder", "it is possible", "to some extent"]
NOM = re.compile(r"\b[a-z]{4,}(tion|tions|ment|ments|ness|ity|ities|ance|ances|ence|ences|ism|isms)\b")
def syllables(w):
    w = w.lower(); g = re.findall(r"[aeiouy]+", w); n = len(g)
    if w.endswith("e") and n > 1 and not w.endswith("le"): n -= 1
    return max(n, 1)
def profile(text):
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"\$[^$]*\$", " x ", text)
    words = re.findall(r"[A-Za-z][A-Za-z'-]*", text)
    sents = [s for s in re.split(r"[.!?]+\s|\n\s*\n|\n[-*\d]", text) if re.search(r"[A-Za-z]", s)]
    lw = " ".join(words).lower(); n = len(words)
    hedges = sum(len(re.findall(r"\b" + re.escape(h) + r"\b", lw)) for h in HEDGES)
    noms = len(NOM.findall(lw)); syl = sum(syllables(w) for w in words)
    fre = 206.835 - 1.015 * (n / max(len(sents), 1)) - 84.6 * (syl / max(n, 1))
    return {"words": n, "hedges_per_1000": round(1000 * hedges / n, 1), "nominalizations_per_100": round(100 * noms / n, 1), "flesch": round(fre, 1)}
if __name__ == "__main__":
    for f in sys.argv[1:]: print(f, profile(open(f).read()))
