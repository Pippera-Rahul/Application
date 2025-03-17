from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Pippera Rahul" 
    username = os.getlogin()
    
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5,minutes=30)
    server_time = ist_time.strftime('%Y-%m-%d %H:%M:%S IST')

    top_output = subprocess.getoutput("top -b -n 1")

    response = f"""
    <h1>Name: {full_name}</h1>
    <h2>Username: {username}</h2>
    <h2>Server Time (IST): {server_time}</h2>
    <pre>{top_output}</pre>
    """
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
