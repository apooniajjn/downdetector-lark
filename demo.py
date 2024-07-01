import cloudscraper
from bs4 import BeautifulSoup
import requests

def check_tiktok_status():
    # Create a cloudscraper instance
    scraper = cloudscraper.create_scraper()

    # URL of the Downdetector TikTok status page
    url = "https://downdetector.com/status/tiktok/"

    # Use cloudscraper to get the page content
    response = scraper.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Locate the status element (you need to inspect the actual page to find the correct selector)
        status_element = soup.find("div", class_="entry-title")
        
        if status_element:
            status_text = status_element.get_text(strip=True)
            print(f"TikTok Status: {status_text}")
            return status_text
        else:
            return("Could not find the status element on the page.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return(response.status_code)

def send_to_lark(status_message):
    webhook_url = "https://open.larksuite.com/open-apis/bot/v2/hook/fc92bdf7-2c8e-4e63-8dcf-57065b66f70e"
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "msg_type": "text",
        "content": {
            "text": status_message
        }
    }
    print (data)
    response = requests.post(webhook_url, json=data, headers=headers)
    if response.status_code == 200:
        print("Message sent to Lark successfully!")
    else:
        print(f"Failed to send message to Lark. Status code: {response.status_code}")

if __name__ == "__main__":
    status_message = check_tiktok_status()
    send_to_lark(status_message)
