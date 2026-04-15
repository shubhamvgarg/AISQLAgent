def validate_sql_query(sql: str):
    sql_lower = sql.lower().strip()

    forbidden = ["drop", "truncate", "alter"]

    if any(cmd in sql_lower for cmd in forbidden):
        return False, "Dangerous query detected"

    if not sql_lower.startswith(("select", "insert", "update", "delete")):
        return False, "Invalid SQL type"

    return True, sql
