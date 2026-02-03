sus_keywords = ["login", "verify", "secure", "update", "account", "password", "bank", "free", "giveaway"]
blacklist_domains = ["bit.ly", "tinyurl.com", "free-gift.com", "click4cash"]

def is_sus_link(url):
    for keyword in sus_keywords:
        if keyword in url.lower():
            return True
    for domain in blacklist_domains:
        if domain in url.lower():
            return True
    return False

while True:
    test_link = input("Paste the link (q to quit): ")
    if test_link.lower() == "q":
        break
    print(f"{test_link} ➤ {'!!!!!!!SUS!!!!!! 😤🚨' if is_sus_link(test_link) else 'SAFE ✅'}")

print("Goodbye <3")
print("Stay safe online!!! 🛡️💖")
