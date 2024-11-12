from django.shortcuts import render
from django.http import HttpResponse
import subprocess
import datetime
import os

def htop(request):
    name = "Lakshya Sharma" 
    username = os.getenv("USER", "default_user")  
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    top_output = subprocess.getoutput("top -b -n 1")

    response = f"""
    Name: {name}<br>
    User: {username}<br>
    Server Time (IST): {server_time}<br>
    <pre>TOP output:\n{top_output}</pre>
    """
    return HttpResponse(response)
