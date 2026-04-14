SQL_PROMPT = """
You are an SQL assistant.

User Question:
{question}

Database Schema:
{schema}

Rules:
- Never guess table names
- Only use schema provided
- Always use correct SQL syntax
- Can generate SELECT, DELETE, UPDATE, INSERT
- Add LIMIT 50
- Return ONLY raw SQL query
- DO NOT use markdown
- DO NOT wrap in ``` or ```sql
"""

NORMALIZE_PROMPT = """
convert the following SQL query to a normalized form that is more likely to be valid against the provided schema.
User Question:
{question}  
Database Schema:
{schema}
and the SQL query is:
{sql_query}
the output should be a normalized SQL query that adheres to the schema and is more likely to be valid.
{result}
"""