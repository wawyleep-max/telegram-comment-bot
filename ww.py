import time
from playwright.sync_api import sync_playwright

TEXT = "вставить текст" #что пишешь
CHANNELS = ["MOODIYA MEMES","mem moment"] #куда пишешь

def post_comment(page,channel,text):
    search = page.locator("input.input-search-input")
    search.click()
    search.fill(channel)
    time.sleep(2)
    page.locator("#search-container a.chatlist-chat").first.click()
    
    time.sleep(2)
    page.locator("replies-element.replies-footer").last.click()
    time.sleep(2)
    comment = page.locator("div.input-message-input").last
    comment.click()
    time.sleep(3)
    comment.press_sequentially(text,delay=100)
    comment.press("Enter")
    time.sleep(4)

with sync_playwright() as p:
    context = p.chromium.launch_persistent_context(
        user_data_dir="telegram_profile",
        headless=False
    )
    pages = context.pages
    page = pages[0]
    page.goto("https://web.telegram.org/k/")

    for channel in CHANNELS:
        try:
            post_comment(page,channel,text=TEXT)
            print(f"✅ Комментарий отправлен: {channel}")
        except Exception as e:
            print(f"❌ Не удалось отправить в {channel}: {e}")
    context.close()













