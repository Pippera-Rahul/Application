from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Your Full Name"  # Replace with your actual full name
    username = os.getlogin()
    
    # Get Current Server Time in IST
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, 30)
    server_time = ist_time.strftime('%Y-%m-%d %H:%M:%S IST')

    # Get Top Command Output
    top_output = subprocess.getoutput("top -b -n 1")

    # Generate HTML Response
    response = f"""
    <h1>Name: {full_name}</h1>
    <h2>Username: {username}</h2>
    <h2>Server Time (IST): {server_time}</h2>
    <pre>{top_output}</pre>
    """
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
