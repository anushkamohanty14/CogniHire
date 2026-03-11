from math import sqrt
from typing import Dict, Iterable, List, Tuple


def collect_cognitive_test_responses(responses: Dict[str, float]) -> Dict[str, float]:
    """Light validation pass for cognitive responses."""
    return {k: float(v) for k, v in responses.items()}


def compute_cognitive_scores(responses: Dict[str, float]) -> Dict[str, float]:
    """Min-max normalize scores into [0, 1]."""
    if not responses:
        return {}
    values = list(responses.values())
    min_v, max_v = min(values), max(values)
    if min_v == max_v:
        return {k: 1.0 for k in responses}
    return {k: (v - min_v) / (max_v - min_v) for k, v in responses.items()}


def build_user_ability_vector(scores: Dict[str, float], ability_order: Iterable[str]) -> List[float]:
    return [float(scores.get(name, 0.0)) for name in ability_order]


def compute_ability_similarity(user_vector: List[float], job_matrix: Dict[str, List[float]]) -> List[Tuple[str, float]]:
    """Compute cosine similarity against each job vector."""

    def cosine(a: List[float], b: List[float]) -> float:
        dot = sum(x * y for x, y in zip(a, b))
        na = sqrt(sum(x * x for x in a))
        nb = sqrt(sum(y * y for y in b))
        if na == 0 or nb == 0:
            return 0.0
        return dot / (na * nb)

    scores = [(job, cosine(user_vector, vector)) for job, vector in job_matrix.items()]
    return sorted(scores, key=lambda x: x[1], reverse=True)


def cluster_careers_by_ability() -> str:
    return "TODO: integrate sklearn KMeans in model-training workflow"


def predict_career_domain(user_vector: List[float]) -> str:
    return "general" if sum(user_vector) / max(len(user_vector), 1) >= 0.5 else "specialized"
