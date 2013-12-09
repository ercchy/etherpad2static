import time
from glob import glob
import errno
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from etherpad2static import get_file_list
from webdriver import CustomWebDriver


def get_empty_pads():
	match = '<body>This text pad is synchronized as you type, so that everyone viewing this page sees the same text. This allows you to collaborate seamlessly on documents!<br><br>Thanks for working together with your peers!<br><br></body>'
	useless = []

	files = glob("etherpad_static/p/*.html")

	for i, doc in enumerate(files):
		f = open(doc, 'r')
		content = f.read()
		if match in content:
			#print i, doc
			useless.append(doc)
	return useless


def parse_pad_name(name):
	name_arr = name.split('/')

	return name_arr[-1:][0].split('.')[0]


def test_pads_functional():

	useless_confirm = []
	false_confirm = []
	pads = get_file_list()

	driver = CustomWebDriver()

	for i, pad in enumerate(pads):
		permisson = True
		driver.get('http://pad.p2pu.org/p/%s/timeslider' % pad)

		wait = WebDriverWait(driver, 10)
		for attempt in range(3):
			try:
				wait.until(lambda driver: driver.find_element_by_id('timer').text != "")
			except TimeoutException:
				body = driver.find_element_by_tag_name('body').text
				if 'You do not have permission to access this pad' in body:
					false_confirm.append(pad)
					print pad
					permisson = False
					break
				time.sleep(10)
			else:
				break
		if permisson:
			revision_label = driver.find_element_by_id('revision_label').text

			if revision_label == u'Version 0':
				useless_confirm.append(pad)
			else:
				false_confirm.append(pad)
				print i, pad

	f = open('empty_pads.txt', 'w')
	f.write('\n'.join(useless_confirm))
	f.close()
	print useless_confirm
	print false_confirm


def main():
	test_pads_functional()


if __name__ == '__main__':
	main()
