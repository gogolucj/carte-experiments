"""
프로젝트 전역 경로 설정

모든 노트북에서 이 파일을 import하여 경로를 사용합니다.
경로 변경이 필요하면 이 파일만 수정하세요.
"""
from pathlib import Path


# =============================================================================
# 프로젝트 루트 경로
# =============================================================================
PROJECT_ROOT = Path("/Users/jisoo/projects/thesis/carte_test")


# =============================================================================
# Raw 데이터 경로
# =============================================================================
class RawPaths:
    """원본 데이터 경로"""

    # MovieLens 32M 데이터
    ML_DIR = PROJECT_ROOT / "data/raw/ml-32m"
    RATINGS_CSV = ML_DIR / "ratings.csv"
    MOVIES_CSV = ML_DIR / "movies.csv"
    LINKS_CSV = ML_DIR / "links.csv"

    # TMDB 데이터
    TMDB_DIR = PROJECT_ROOT / "data/raw/tmdb"
    TMDB_MOVIES_JSONL = TMDB_DIR / "tmdb_movies.jsonl"

    # TMDB fetch 중간 결과 (재시작 지원용)
    TMDB_RUN_DIR = PROJECT_ROOT / "data/raw/tmdb_run"


# =============================================================================
# Processed 데이터 경로
# =============================================================================
class ProcessedPaths:
    """전처리된 데이터 경로"""

    DIR = PROJECT_ROOT / "data/processed"

    # filter_ratings.ipynb 출력
    RATINGS_PARQUET = DIR / "ratings_recent_n.parquet"

    # fetch_tmdb_from_movielens.ipynb 출력
    TMDB_FETCH_STATE_PARQUET = DIR / "tmdb_fetch_state.parquet"

    # build_movie_catalog.ipynb 출력
    MOVIE_CATALOG_PARQUET = DIR / "movie_catalog_flat.parquet"

    # apply_carte_movie_embeddings.ipynb 출력
    MOVIE_EMBEDDINGS_PARQUET = DIR / "movie_embeddings.parquet"

    # apply_carte_movie_embeddings_bert.ipynb 출력 (BERT 하이브리드 버전)
    MOVIE_EMBEDDINGS_BERT_PARQUET = DIR / "movie_embeddings_bert.parquet"


# =============================================================================
# 편의 alias
# =============================================================================
RAW = RawPaths
PROCESSED = ProcessedPaths
