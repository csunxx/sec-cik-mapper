from pathlib import Path

import pytest

from sec_cik_mapper import (
    MutualFundMapper,
    MutualFundRetriever,
    StockMapper,
    StockRetriever,
)


@pytest.fixture(scope="session")
def stock_mapper() -> StockMapper:
    return StockMapper()


@pytest.fixture(scope="session")
def mutual_fund_mapper() -> MutualFundMapper:
    return MutualFundMapper()


@pytest.fixture(scope="session")
def auto_generated_mappings_path() -> Path:
    return Path("auto_generated_mappings")


@pytest.fixture(scope="session")
def stock_retriever() -> StockRetriever:
    return StockRetriever()


@pytest.fixture(scope="session")
def mutual_fund_retriever() -> MutualFundRetriever:
    return MutualFundRetriever()
