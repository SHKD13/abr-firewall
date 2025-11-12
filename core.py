def abr_score(url: str, metadata: dict = None) -> int:
    """
    Returns Anti-Brain Rot score from -3 to +3
    Input: URL + optional metadata (duration, type, domain, etc.)
    Output: int + explanation
    """
    if metadata is None:
        metadata = fetch_metadata(url)  # your implementation

    # 1. Domain rules (higher priority)
    domain_rules = {
        "arxiv.org":      +1,
        "sciencedirect.com": +1,
        "cyberleninka.ru":  +1
		"stackoverflow.com":  +1
		"journals.plos.org/plosone/":  +1
		"youtube.com/watch": _youtube_handler(metadata),
        "tiktok.com":     -3,
        "twitch.tv":      -3,
        "reddit.com":     -2,
    }
    for domain, score in domain_rules.items():
        if domain in url:
            return _finalize(score, url, "domain_rule")

    # 2. Metadata
    if metadata.get("duration_min", 0) > 40 and metadata.get("is_lecture"):
        return _finalize(+2, url, "long_lecture")
    if metadata.get("content_type") == "short_video":
        return _finalize(-3, url, "short_video")
    if metadata.get("is_gaming"):
        return _finalize(-3, url, "gaming")

    # 3. URL/Title Heuristics
    if any(kw in url.lower() for kw in ["shorts", "reel", "tiktok"]):
        return _finalize(-3, url, "keyword_short")
    if "pdf" in url and ("diss" in url or "thesis" in url):
        return _finalize(+3, url, "dissertation_pdf")

    return _finalize(0, url, "neutral")

def _finalize(score, url, reason):
    return {
        "score": score,
        "url": url,
        "reason": reason,
        "version": "ABRFP-1.3 Final",   
        "name": "Anti-Brain Rot Firewall"
    }
