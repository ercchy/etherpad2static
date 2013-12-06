import glob


def run_clean():


	match = '<body>This text pad is synchronized as you type, so that everyone viewing this page sees the same text. This allows you to collaborate seamlessly on documents!<br><br>Thanks for working together with your peers!<br><br></body>'

	files = glob.glob("p/*.html")

	for i, file in enumerate(files):
		f = open(file, 'r')
		content = f.read()
		if match in content:
			print i, '. ', file


def main():
	run_clean()


if __name__ == '__main__':
	main()
