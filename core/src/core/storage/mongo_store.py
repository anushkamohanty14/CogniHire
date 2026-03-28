"""MongoDB-backed user profile store.

Reads connection details from environment variables (loaded from .env):
    MONGODB_URI  — Atlas connection string
    MONGODB_DB   — database name (default: career_recommender)

Implements the same interface as JsonUserStore so it can be swapped in
anywhere JsonUserStore is used.
"""
from __future__ import annotations

import os
from typing import Any, Dict, Optional

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.collection import Collection

load_dotenv()


def _get_collection() -> Collection:
    uri = os.environ.get("MONGODB_URI")
    if not uri:
        raise EnvironmentError("MONGODB_URI is not set. Add it to your .env file.")
    db_name = os.environ.get("MONGODB_DB", "career_recommender")
    client = MongoClient(uri)
    return client[db_name]["user_profiles"]


class MongoUserStore:
    """MongoDB-backed profile store (production).

    Usage
    -----
    >>> store = MongoUserStore()
    >>> store.upsert_profile({"user_id": "u1", "manual_skills": ["python"]})
    >>> store.get_profile("u1")
    """

    def __init__(self) -> None:
        self._col: Collection = _get_collection()

    def upsert_profile(self, profile: Dict[str, Any]) -> Dict[str, Any]:
        """Insert or replace a user profile keyed by user_id."""
        self._col.replace_one(
            {"user_id": profile["user_id"]},
            profile,
            upsert=True,
        )
        return profile

    def get_profile(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Return the stored profile or None if not found."""
        doc = self._col.find_one({"user_id": user_id}, {"_id": 0})
        return doc or None
