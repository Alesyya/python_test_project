test_chrome:
	pytest --reruns 3 -n 3 --browser=chrome --headless=False
test_chrome_headless:
	pytest --reruns 3 -n 3 --browser=chrome --headless=True
test_firefox:
	pytest --reruns 3 -n 3 --browser=firefox --headless=False
test_firefox_headless:
	pytest --reruns 3 -n 3 --browser=firefox --headless=True