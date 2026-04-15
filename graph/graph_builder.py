from langgraph.graph import StateGraph, START, END
from graph.state import SQLState
from graph.nodes import (
    retrieve_tables,
    get_schema,
    generate_sql,
    validate_sql,
    execute_sql,
    normalize_output,
    update_db,
    init_state,
    fix_sql,
    route_after_execution
)

def route_after_validation(state):
    if "error" in state and state["error"]:
        if state["attempts"] >= state["max_attempts"]:
            return END
        return "fix_sql"

    query = state["validated_sql"].lower()

    if query.startswith(("insert", "update", "delete")):
        return "update_db"

    return "execute_sql"


def build_agent():
    builder = StateGraph(SQLState)

    builder.add_node("init_state", init_state)
    builder.add_node("retrieve_tables", retrieve_tables)
    builder.add_node("get_schema", get_schema)
    builder.add_node("generate_sql", generate_sql)
    builder.add_node("validate_sql", validate_sql)
    builder.add_node("fix_sql", fix_sql)
    builder.add_node("execute_sql", execute_sql)
    builder.add_node("update_db", update_db)
    builder.add_node("normalize_output", normalize_output)

    builder.add_edge(START, "init_state")
    builder.add_edge("init_state", "retrieve_tables")
    builder.add_edge("retrieve_tables", "get_schema")
    builder.add_edge("get_schema", "generate_sql")
    builder.add_edge("generate_sql", "validate_sql")

    builder.add_conditional_edges("validate_sql", route_after_validation)
    builder.add_conditional_edges("execute_sql", route_after_execution)

    builder.add_edge("fix_sql", "generate_sql")
    builder.add_edge("normalize_output", END)
    builder.add_edge("update_db", END)

    return builder.compile()
