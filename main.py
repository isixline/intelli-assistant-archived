from dotenv import load_dotenv
from src.interactions.user_interaction import interaction_handle

load_dotenv()

if __name__ == "__main__":
    interaction_handle()
