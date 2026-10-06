from flask import Flask, request, jsonify, render_template
from db import init_db, get_db_connection
import pandas as pd

app = Flask(__name__)

init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/expenses", methods=["POST"])
def add_expense():
    data = request.get_json()

    connection = get_db_connection()

    cursor = connection.execute(
        """
        INSERT INTO expenses (title, amount, category, expense_date)
        VALUES (?, ?, ?, ?)
        """,
        (
            data["title"],
            data["amount"],
            data["category"],
            data["expense_date"]
        )
    )

    connection.commit()
    expense_id = cursor.lastrowid
    connection.close()

    return jsonify({
        "message": "Expense added successfully",
        "id": expense_id
    }), 201

@app.route("/api/expenses", methods=["GET"])
def get_expenses():
    connection = get_db_connection()

    expenses = connection.execute(
        "SELECT * FROM expenses ORDER BY expense_date DESC"
    ).fetchall()

    connection.close()

    return jsonify([dict(expense) for expense in expenses])

@app.route("/api/expenses/<int:expense_id>", methods=["DELETE"])
def delete_expense(expense_id):
    connection = get_db_connection()

    cursor = connection.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )

    connection.commit()
    connection.close()

    if cursor.rowcount == 0:
        return jsonify({
            "message": "Expense not found"
        }), 404

    return jsonify({
        "message": "Expense deleted successfully"
    })

@app.route("/api/expenses/import", methods=["POST"])
def import_expenses():
    file = request.files.get("file")

    if not file:
        return jsonify({"message": "CSV file is required"}), 400

    df = pd.read_csv(file)

    required_columns = {
        "title",
        "amount",
        "category",
        "expense_date"
    }

    if not required_columns.issubset(df.columns):
        return jsonify({
            "message": "CSV has missing required columns"
        }), 400

    connection = get_db_connection()

    for _, row in df.iterrows():
        connection.execute(
            """
            INSERT INTO expenses
            (title, amount, category, expense_date)
            VALUES (?, ?, ?, ?)
            """,
            (
                row["title"],
                row["amount"],
                row["category"],
                row["expense_date"]
            )
        )

    connection.commit()
    connection.close()

    return jsonify({
        "message": "CSV imported successfully",
        "rows_imported": len(df)
    }), 201

@app.route("/api/analytics", methods=["GET"])
def get_analytics():
    connection = get_db_connection()

    total = connection.execute(
        "SELECT SUM(amount) AS total FROM expenses"
    ).fetchone()["total"]

    category_data = connection.execute(
        """
        SELECT category, SUM(amount) AS total
        FROM expenses
        GROUP BY category
        ORDER BY total DESC
        """
    ).fetchall()

    monthly_data = connection.execute(
        """
        SELECT substr(expense_date, 1, 7) AS month,
               SUM(amount) AS total
        FROM expenses
        GROUP BY month
        ORDER BY month
        """
    ).fetchall()

    connection.close()

    return jsonify({
        "total_spending": total or 0,
        "by_category": [dict(row) for row in category_data],
        "by_month": [dict(row) for row in monthly_data]
    })


if __name__ == "__main__":
    app.run(debug=True)
