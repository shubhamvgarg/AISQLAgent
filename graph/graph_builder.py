from langgraph.graph import StateGraph, START, END
from graph.state import SQLState
from graph.nodes import (
    retrieve_tables,
    get_schema,
    generate_sql,
    validate_sql,
    execute_sql,
    normalize_output,
    update_db
)

def route_after_validation(state: SQLState):
    """
    Decide next step based on SQL type.
    Assumes state has something like `state.sql_query`
    """
    query = state["sql_query"].lower()

    if query.startswith(("insert", "update", "delete", "create", "drop", "alter")):
        return "update_db"
    return "execute_sql"


def build_graph():
    builder = StateGraph(SQLState)

    builder.add_node("retrieve_tables", retrieve_tables)
    builder.add_node("get_schema", get_schema)
    builder.add_node("generate_sql", generate_sql)
    builder.add_node("validate_sql", validate_sql)
    builder.add_node("execute_sql", execute_sql)
    builder.add_node("normalize_output", normalize_output)
    builder.add_node("update_db", update_db)

    builder.add_edge(START, "retrieve_tables")
    builder.add_edge("retrieve_tables", "get_schema")
    builder.add_edge("get_schema", "generate_sql")
    builder.add_edge("generate_sql", "validate_sql")

    builder.add_conditional_edges("validate_sql", route_after_validation)

    builder.add_edge("execute_sql", "normalize_output")
    builder.add_edge("normalize_output", END)
    builder.add_edge("update_db", END)



    return builder.compile()