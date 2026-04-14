from langchain_groq import ChatGroq
from db.database import get_connection
from utils.prompts import SQL_PROMPT, NORMALIZE_PROMPT
from utils.validators import validate_sql_query
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

def retrieve_tables(state):
    return {**state, "tables": ["users", "orders", 'categories', 'order_items','products']}


# 2. Get schema
def get_schema(state):
    #print("Getting database schema...")
    conn = get_connection()
    cursor = conn.cursor()

    schema = ""
    for table in state["tables"]:
        cursor.execute(f"PRAGMA table_info({table})")
        columns = cursor.fetchall()
        schema += f"\nTable {table}:\n"
        for col in columns:
            schema += f"{col[1]} ({col[2]})\n"

    conn.close()

    return {**state, "schema": schema}


# 3. Generate SQL
def generate_sql(state):
    prompt = SQL_PROMPT.format(
        question=state["question"],
        schema=state["schema"]
    )

    response = llm.invoke(prompt)
    return {**state, "sql_query": response.content.strip()}


# 4. Validate SQL
def validate_sql(state):
    is_valid, result = validate_sql_query(state["sql_query"])

    if not is_valid:
        return {**state, "error": result}
    
    return {**state, "validated_sql": result}


# 5. Execute SQL
def execute_sql(state):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(state["validated_sql"])
        rows = cursor.fetchall()

        conn.close()

        return {**state, "result": str(rows)}

    except Exception as e:
        return {**state, "error": str(e)}
    

def update_db(state):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(state["validated_sql"])
        conn.commit()
        conn.close()

        return {**state, "result": "Update successful"}

    except Exception as e:
        return {**state, "error": str(e)}
    
def normalize_output(state):
     prompt = NORMALIZE_PROMPT.format(
        question=state["question"],
        schema=state["schema"],
        sql_query=state["sql_query"],
        result=state["result"]
    )
     response = llm.invoke(prompt)
     return {**state, "result": response.content.strip()}