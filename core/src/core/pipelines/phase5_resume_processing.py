"""Phase 5 — Resume text extraction and rule-based skill identification.

Pipeline
--------
1. extract_text(file_path)    →  raw string from PDF / DOCX / TXT
2. extract_skills_rules(text) →  skills matched against the built-in taxonomy
3. process_resume(file_path)  →  SkillExtractionResult (end-to-end)

Extracted skills are stored separately from manual_skills in the user profile
under the key "resume_skills" so the two sources remain distinguishable.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional


# ── Data model ────────────────────────────────────────────────────────────────

@dataclass
class SkillExtractionResult:
    """Output of the resume skill extraction pipeline.

    Attributes
    ----------
    skills : list[str]
        Deduplicated, normalised skill strings.
    method : str
        ``"rules"`` for regex taxonomy matching, ``"error"`` when extraction failed.
    raw_text_length : int
        Character count of the extracted resume text.
    error : str | None
        Non-None only when method == "error".
    """
    skills: List[str]
    method: str
    raw_text_length: int
    error: Optional[str] = None


# ── Text extraction ───────────────────────────────────────────────────────────

def extract_text(file_path: str) -> str:
    """Return the plain-text content of a resume file.

    Supported formats: ``.pdf``, ``.docx`` / ``.doc``, and any plain-text
    extension (``.txt``, ``.md``, etc.).
    """
    path = Path(file_path)
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return _extract_pdf(path)
    if suffix in (".docx", ".doc"):
        return _extract_docx(path)
    return path.read_text(encoding="utf-8", errors="replace")


def _extract_pdf(path: Path) -> str:
    from pypdf import PdfReader
    reader = PdfReader(str(path))
    pages = [page.extract_text() or "" for page in reader.pages]
    return "\n".join(pages)


def _extract_docx(path: Path) -> str:
    import docx  # python-docx
    doc = docx.Document(str(path))
    return "\n".join(p.text for p in doc.paragraphs)


# ── Rule-based extraction ─────────────────────────────────────────────────────

_SKILL_TAXONOMY: List[str] = [
    # Programming languages
    "Python", "Java", "JavaScript", "TypeScript", "C", "C++", "C#", "Go",
    "Rust", "Ruby", "PHP", "Swift", "Kotlin", "R", "MATLAB", "Scala", "Perl",
    "Bash", "Shell", "SQL", "HTML", "CSS", "SASS", "LESS", "Dart", "Lua",
    "Haskell", "Erlang", "Elixir", "Clojure", "F#",

    # Web frameworks & libraries
    "React", "Angular", "Vue", "Vue.js", "Next.js", "Nuxt.js", "Svelte",
    "Node.js", "Express", "Django", "Flask", "FastAPI", "Spring", "Spring Boot",
    "Laravel", "Rails", "Ruby on Rails", "ASP.NET", ".NET", "jQuery",
    "Tailwind CSS", "Bootstrap", "GraphQL", "REST", "gRPC", "WebSocket",

    # Data science & ML
    "TensorFlow", "PyTorch", "Keras", "scikit-learn", "Pandas", "NumPy",
    "SciPy", "Matplotlib", "Seaborn", "Plotly", "Hugging Face", "spaCy",
    "NLTK", "OpenCV", "LangChain", "LlamaIndex", "BERT", "GPT",
    "Machine Learning", "Deep Learning", "NLP", "Natural Language Processing",
    "Computer Vision", "Data Science", "Data Analysis", "Data Engineering",
    "Feature Engineering", "A/B Testing", "Statistics", "ETL",
    "Data Warehousing", "Neural Networks", "Transformers", "RAG",
    "Reinforcement Learning", "Time Series", "Forecasting",

    # Databases
    "MySQL", "PostgreSQL", "MongoDB", "SQLite", "Oracle", "SQL Server",
    "Redis", "Elasticsearch", "Cassandra", "DynamoDB", "Firebase", "Firestore",
    "Neo4j", "InfluxDB", "Snowflake", "BigQuery", "Redshift",
    "Pinecone", "Weaviate", "ChromaDB",

    # Cloud & infrastructure
    "AWS", "Azure", "GCP", "Google Cloud", "Docker", "Kubernetes",
    "Terraform", "Ansible", "Puppet", "Chef", "Helm", "Istio",
    "CI/CD", "Jenkins", "GitHub Actions", "CircleCI", "Travis CI", "GitLab CI",
    "Nginx", "Apache", "Linux", "Unix",

    # Tools & platforms
    "Git", "GitHub", "GitLab", "Bitbucket", "Jira", "Confluence",
    "Tableau", "Power BI", "Looker", "dbt", "Airflow", "Prefect", "Dagster",
    "Spark", "Hadoop", "Kafka", "Flink", "Celery", "RabbitMQ",
    "VS Code", "IntelliJ", "PyCharm", "Eclipse", "Xcode",
    "npm", "Yarn", "Webpack", "Vite", "Babel",
    "Postman", "Swagger", "OpenAPI",

    # Security
    "OAuth", "JWT", "SSL", "TLS", "Cybersecurity", "OWASP",
    "Penetration Testing", "Encryption",

    # Mobile
    "iOS", "Android", "React Native", "Flutter", "Xamarin",

    # Methodologies
    "Agile", "Scrum", "Kanban", "DevOps", "TDD", "BDD",
    "Microservices", "Domain-Driven Design", "SOLID",
    "Design Patterns", "System Design",

    # BI / Office
    "Excel", "Google Sheets", "PowerPoint", "Word",
]

# Pre-compile patterns: sort by length descending to prefer longer matches
_PATTERNS = sorted(
    [(skill, re.compile(r"\b" + re.escape(skill) + r"\b", re.IGNORECASE))
     for skill in _SKILL_TAXONOMY],
    key=lambda x: -len(x[0]),
)


def extract_skills_rules(text: str) -> List[str]:
    """Return all skills from the taxonomy that appear in *text*."""
    found: List[str] = []
    for skill, pattern in _PATTERNS:
        if pattern.search(text):
            found.append(skill)
    return found


# ── Combined pipeline ─────────────────────────────────────────────────────────

def extract_skills(text: str) -> SkillExtractionResult:
    """Extract skills from resume text using rule-based matching."""
    skills = extract_skills_rules(text)
    return SkillExtractionResult(
        skills=_normalise(skills),
        method="rules",
        raw_text_length=len(text),
    )


def process_resume(file_path: str) -> SkillExtractionResult:
    """End-to-end: extract text from *file_path* then extract skills."""
    try:
        text = extract_text(file_path)
    except Exception as exc:
        return SkillExtractionResult(
            skills=[], method="error", raw_text_length=0,
            error=f"Text extraction failed: {exc}",
        )

    if not text.strip():
        return SkillExtractionResult(
            skills=[], method="error", raw_text_length=0,
            error="No readable text found in the file.",
        )

    return extract_skills(text)


# ── Helpers ───────────────────────────────────────────────────────────────────

def _normalise(skills: List[str]) -> List[str]:
    """Deduplicate (case-insensitive) and sort."""
    seen: dict[str, str] = {}
    for s in skills:
        key = s.strip().lower()
        if key and key not in seen:
            seen[key] = s.strip()
    return sorted(seen.values(), key=str.lower)
