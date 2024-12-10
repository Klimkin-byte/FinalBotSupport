from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")
db_path = os.getenv("DATABASE_PATH")
DATABASE_URL=os.getenv("DATABASE_URL")
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config'))