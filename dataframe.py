from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def display_dataframe():
    # Create a sample DataFrame
    data = {'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35],
            'City': ['New York', 'San Francisco', 'Los Angeles']}
    df = pd.DataFrame(data)

    # Convert DataFrame to HTML
    table_html = df.to_html(classes='table table-striped', index=False)

    # Render the template with the DataFrame HTML
    return render_template('dataframe.html', table_html=table_html)


if __name__ == '__main__':
    app.run(debug=True)
