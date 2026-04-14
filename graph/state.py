from typing import TypedDict, Optional, List

class SQLState(TypedDict):
    question: str
    tables: Optional[List[str]]
    schema: Optional[str]
    sql_query: Optional[str]
    validated_sql: Optional[str]
    result: Optional[str]
    error: Optional[str]