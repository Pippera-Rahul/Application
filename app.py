from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    try:
        # Get system info
        name = "Rahul"
        username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown User"
        server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Get top command output
        top_output = subprocess.getoutput("top -b -n 1")

        # Format output
        response = f"""
        <h1>Name: {name}</h1>
        <h2>Username: {username}</h2>
        <h3>Server Time: {server_time} (IST)</h3>
        <pre>{top_output}</pre>
        """
        return response

    except Exception as e:
        return f"<h1>Error: {str(e)}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006)
