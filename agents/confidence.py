def score_facts(facts):
    domain_weight = {
        ".gov": 0.9,
        ".edu": 0.85,
        ".org": 0.75
    }

    scored = []
    for f in facts:
        score = 0.5

        for d, w in domain_weight.items():
            if d in f["source"]:
                score += w * 0.3

        if len(f["claim"]) > 120:
            score += 0.1

        if any(w in f["claim"].lower() for w in ["may", "might", "could"]):
            score -= 0.1

        scored.append({
            **f,
            "confidence": round(min(score, 1.0), 2)
        })

    return scored