import requests
import json
import time
from datetime import datetime
from typing import Dict, List
import os
from dotenv import load_dotenv
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('advent_calendar.log'),
        logging.StreamHandler()
    ]
)

class AdventCalendarChecker:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # Configuration
        self.webhook_url = os.getenv('DISCORD_WEBHOOK_URL')
        self.session_id = os.getenv('LABY_SESSION_ID')
        self.live_token = os.getenv('LABY_LIVE_TOKEN')
        self.calendar_file = Path('calendar.json')
        self.api_url = "https://labymod.net/api/adventcalendar/open-door"
        
        # Validate configuration
        self._validate_config()
        
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "application/json",
            "Content-Type": "multipart/form-data; boundary=---------------------------boundary",
            "Origin": "https://labymod.net",
            "Referer": "https://labymod.net/en/adventcalendar",
            "Cookie": f"LABY_SESSION_ID={self.session_id}; lm_long_live_token={self.live_token}"
        }
        
        self.checked_dates = set()

    def _validate_config(self) -> None:
        """Validate that all required configuration is present."""
        if not all([self.webhook_url, self.session_id, self.live_token]):
            raise ValueError("Missing required environment variables. Please check .env file.")
        
        if not self.calendar_file.exists():
            raise FileNotFoundError(f"Calendar file not found at {self.calendar_file}")

    def load_calendar(self) -> List[Dict]:
        """Load and parse the calendar JSON file."""
        try:
            with open(self.calendar_file, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            logging.error(f"Failed to parse calendar.json: {e}")
            raise
        except Exception as e:
            logging.error(f"Failed to load calendar.json: {e}")
            raise

    def send_webhook(self, content: str) -> None:
        """Send a message to Discord webhook."""
        try:
            response = requests.post(self.webhook_url, json={"content": content})
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to send webhook: {e}")

    def check_day(self, day_number: int) -> bool:
        """Check a specific advent calendar day."""
        try:
            data = (
                f'-----------------------------boundary\r\n'
                f'Content-Disposition: form-data; name="day"\r\n\r\n'
                f'{day_number}\r\n'
                f'-----------------------------boundary--'
            )
            
            response = requests.post(self.api_url, headers=self.headers, data=data)
            response.raise_for_status()
            
            return True
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to check day {day_number}: {e}")
            return False

    def run(self, check_interval: int = 3600) -> None:
        """Main loop to check advent calendar days."""
        logging.info("Starting Advent Calendar Checker")
        
        while True:
            try:
                calendar = self.load_calendar()
                current_time = datetime.now().strftime("%Y-%m-%d")
                
                for entry in calendar:
                    if current_time == entry["day"] and entry["day"] not in self.checked_dates:
                        day_number = entry["number"]
                        
                        if self.check_day(day_number):
                            message = f"🎄 Day {day_number} is available! Go check your advent calendar!"
                            self.send_webhook(message)
                            logging.info(f"Successfully checked day {day_number}")
                            self.checked_dates.add(entry["day"])
                
                time.sleep(check_interval)
                
            except Exception as e:
                logging.error(f"Error in main loop: {e}")
                time.sleep(60)  # Wait a minute before retrying if there's an error

def main():
    # Create .env file template if it doesn't exist
    if not Path('.env').exists():
        with open('.env', 'w') as f:
            f.write("""# Discord Webhook URL
DISCORD_WEBHOOK_URL=your_webhook_url_here
# LabyMod Session ID
LABY_SESSION_ID=your_session_id_here
# LabyMod Live Token
LABY_LIVE_TOKEN=your_live_token_here
""")
        logging.info("Created .env template file. Please fill in your credentials.")
        return

    try:
        checker = AdventCalendarChecker()
        checker.run()
    except KeyboardInterrupt:
        logging.info("Shutting down Advent Calendar Checker")
    except Exception as e:
        logging.error(f"Fatal error: {e}")

if __name__ == "__main__":
    main()