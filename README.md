# AskSQL 💬

An intelligent SQL query generator that converts natural language questions into executable SQL queries using AI. Built with LangChain, LangGraph, and Groq, AskSQL provides an intuitive interface for querying databases without writing SQL manually.

## Features

- 🤖 **AI-Powered Query Generation** - Convert plain English questions to SQL queries using Groq GPT
- 🔄 **LangGraph Workflow** - Intelligent multi-step processing pipeline for query generation and validation
- ✅ **Query Validation** - Automatic validation of generated SQL before execution
- 📊 **Direct Results** - Execute queries and display results in real-time
- 🎨 **Streamlit UI** - Clean, user-friendly web interface
- 🔐 **Environment Configuration** - Secure API key management with `.env`

## Architecture

The project follows a modular design with the following components:

```
asksql/
├── app.py                    # Streamlit web application
├── requirements.txt          # Project dependencies
├── .env                      # Environment variables (API keys)
├── graph/
│   ├── state.py             # LangGraph state definitions
│   ├── nodes.py             # Graph node implementations
│   └── graph_builder.py      # Graph construction and orchestration
├── db/
│   ├── database.py          # Database connection and operations
│   └── init_db.py           # Database initialization
└── utils/
    ├── prompts.py           # LLM prompt templates
    └── validators.py        # SQL validation logic
```

## Prerequisites

- Python 3.8+
- Groq API key ([get one here](https://console.groq.com/keys))
- SQLite or other compatible database

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd asksql
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env  # Or create .env manually
   ```
   Add your Groq API key to `.env`:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

## Usage

1. **Start the Streamlit app**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**
   Navigate to `http://localhost:8501`

3. **Ask a question**
   - Enter your question in plain English
   - Click "Run Query"
   - View the generated SQL and results

### Example Queries
- "Show me all customers who made purchases in the last month"
- "What are the top 5 products by revenue?"
- "Find users with account balance over $1000"

## Project Structure

### `app.py`
Main Streamlit application that provides the UI for querying. Integrates the LangGraph workflow to process user questions and display results.

### `graph/`
Contains the LangGraph workflow implementation:
- **state.py**: Defines the state schema for the graph
- **nodes.py**: Implements individual processing nodes
- **graph_builder.py**: Constructs and manages the workflow graph

### `db/`
Handles database operations:
- **database.py**: Database connection, query execution, and result handling
- **init_db.py**: Database initialization and schema setup

### `utils/`
Utility modules:
- **prompts.py**: LLM prompt templates for SQL generation
- **validators.py**: Validates generated SQL before execution

## Environment Variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY=sk-...
DATABASE_URL=sqlite:///./asksql.db
```

## Dependencies

- **streamlit** - Web application framework
- **langchain** - LLM orchestration
- **langgraph** - Workflow graph management
- **Groq** - Groq API integration
- **python-dotenv** - Environment variable management
- **sqlalchemy** - Database ORM and operations

## How It Works

1. **User Input** - User asks a question in natural language
2. **Question Processing** - The question is analyzed and contextualized
3. **SQL Generation** - Groq generates an SQL query based on the question
4. **Validation** - The generated SQL is validated for correctness and safety
5. **Execution** - The validated query executes against the database
6. **Results Display** - Results are formatted and displayed to the user

## Development

### Running Tests
```bash
pytest tests/
```

### Code Style
Follow PEP 8 conventions. Run linting:
```bash
flake8 .
black .
```

## Error Handling

The application includes robust error handling:
- Invalid SQL queries are caught and reported
- Database connection errors provide helpful messages
- API failures are gracefully handled with retry logic

## Security Considerations

- Never commit `.env` files with real API keys
- Always validate user input
- Use parameterized queries to prevent SQL injection
- Implement rate limiting in production
- Restrict database user permissions appropriately

## Limitations

- Query generation depends on database schema understanding
- Complex queries may require refinement
- Real-time data accuracy depends on database state
- Supported databases: SQLite, PostgreSQL, MySQL (extensible)

## Future Enhancements

- [ ] Multi-database support
- [ ] Query history and caching
- [ ] Advanced analytics and visualization
- [ ] Custom prompt engineering
- [ ] Cost optimization for API calls
- [ ] Database schema learning from documents

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact the development team
- Check existing documentation

## Acknowledgments

- Built with [LangChain](https://langchain.com)
- Powered by [Groq](https://console.groq.com/home)
- UI framework [Streamlit](https://streamlit.io)

---

**Happy querying! 🚀**
