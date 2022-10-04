# importing libraries
import os
from dotenv import load_dotenv

load_dotenv()

# Set API endpoint URL
if "API_HOSTNAME" in os.environ and "API_PORT" in os.environ:
    api_endpoint = f"http://{os.environ['API_HOSTNAME']}:{os.environ['API_PORT']}/api/asteroids"
    
    print(f"\nConnecting to host : {os.environ['API_HOSTNAME']} on port: {os.environ['API_PORT']}\n")
else:
    print(f"\n INFO : Missing environment variables:\n")
    print(f"\n API_HOSTNAME\nAPI_PORT\n")
    print(f"\n Using default: http://host.docker.internal:8088\n")
    api_endpoint = f"http://{os.getenv['API_HOSTNAME']}:{os.getenv['API_PORT']}/api/asteroids"
    


