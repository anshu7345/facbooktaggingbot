import tkinter as tk
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def run_facebook_automation():
    message_file_path = message_entry.get()
    link_file_path = link_entry.get()

    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    import time
    # Create a ChromeService instance
    chrome_service = Service(ChromeDriverManager().install())

    # Create ChromeOptions to disable notifications
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")

    # Initialize the webdriver using the service and options
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # Open Facebook
    driver.get("https://www.facebook.com")

    # Find username and password fields and enter credentials
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='password']")))

    # Enter username and password
    username.clear()
    username.send_keys("")
    password.clear()
    password.send_keys("")

    # Target the login button and click it
    button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    # Continue with the rest of your automation code

    time.sleep(1)

    # # Navigate to the posting area
    # search=driver.find_element_by_xpath("//div[@aria-label='Create']").click()
    # post=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div[2]/span").click()
    create_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Create']")))
    create_button.click()

    # Wait for the "Post" button and then click it
    post_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div[2]/span")))
    post_button.click()

    time.sleep(1)


    # Read post content from file
    with open('message.txt', 'r') as post_file:
        post_text = post_file.read()


        post_aerea = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.__fb-light-mode.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > form > div > div.x9f619.x1ja2u2z.x1k90msu.x6o7n8i.x1qfuztq.x10l6tqk.x17qophe.x13vifvy.x1hc1fzr.x71s49j > div > div > div > div.xb57i2i.x1q594ok.x5lxg6s.x6ikm8r.x1ja2u2z.x1pq812k.x1rohswg.xfk6m8.x1yqm8si.xjx87ck.xx8ngbg.xwo3gff.x1n2onr6.x1oyok0e.x1odjw0f.x1e4zzel.x78zum5.xdt5ytf.x1iyjqo2 > div.x78zum5.xdt5ytf.x1iyjqo2.x1n2onr6 > div.x1ed109x.x1iyjqo2.x5yr21d.x1n2onr6.xh8yej3 > div.x9f619.x1iyjqo2.xg7h5cd.x1pi30zi.x1swvt13.x1n2onr6.xh8yej3.x1ja2u2z.x1t1ogtf > div > div > div.xzsf02u.x1a2a7pz.x1n2onr6.x14wi4xw.x9f619.x1lliihq.x5yr21d.xh8yej3.notranslate > p")))
        post_aerea.send_keys(post_text)
    #tagging

        with open('link.txt', 'r') as tag_file:
            user_tag = tag_file.read().splitlines()

        for i in range(len(user_tag)):
            post_aerea.send_keys(user_tag[i])
            time.sleep(0.5)
            post_aerea.send_keys(Keys.ENTER)
            time.sleep(0.0005)

        #post_aerea.send_keys(Keys.DOWN)  # Select the first suggestion
        #post_aerea.send_keys(Keys.RETURN)  

        time.sleep(2)  # Wait for tagging suggestions to appear
    post_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.__fb-light-mode.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > form > div > div.x9f619.x1ja2u2z.x1k90msu.x6o7n8i.x1qfuztq.x10l6tqk.x17qophe.x13vifvy.x1hc1fzr.x71s49j > div > div > div > div.x1l90r2v.xyamay9.x1n2onr6 > div.x6s0dn4.x9f619.x78zum5.x1qughib.x1pi30zi.x1swvt13.xyamay9.xh8yej3 > div > div"))).click()
    time.sleep(1)
    driver.get("https://www.facebook.com/profile.php?id=100012792497212")
    time.sleep(10)
   

    driver.close()

def browse_message_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    message_entry.delete(0, tk.END)
    message_entry.insert(0, file_path)

def browse_link_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    link_entry.delete(0, tk.END)
    link_entry.insert(0, file_path)

app = tk.Tk()
app.title("Tittle")

# Configure the app window
app.geometry("400x250")
app.resizable(False, False)
app.configure(bg="#f0f0f0")

# Header label
header_label = tk.Label(app, text="Facebook Automation", font=("Helvetica", 16), bg="#f0f0f0")
header_label.pack(pady=10)

# Message file entry
message_label = tk.Label(app, text="Message File:", font=("Helvetica", 12), bg="#f0f0f0")
message_label.pack(anchor='w', padx=20)
message_entry = tk.Entry(app, width=30)
message_entry.pack(anchor='w', padx=20)
browse_message_button = tk.Button(app, text="Browse", command=browse_message_file)
browse_message_button.pack(anchor='w', padx=20)

# Link file entry
link_label = tk.Label(app, text="Link File:", font=("Helvetica", 12), bg="#f0f0f0")
link_label.pack(anchor='w', padx=20)
link_entry = tk.Entry(app, width=30)
link_entry.pack(anchor='w', padx=20)
browse_link_button = tk.Button(app, text="Browse", command=browse_link_file)
browse_link_button.pack(anchor='w', padx=20)

# Run button
run_button = tk.Button(app, text="Run Automation", font=("Helvetica", 12), command=run_facebook_automation, bg="#4285F4", fg="white")
run_button.pack(pady=15)

app.mainloop()
