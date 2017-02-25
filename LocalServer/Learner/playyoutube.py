import webbrowser
import time
i = 0;

print("It started on : " + time.ctime());
while i < 3:
	time.sleep(2)
	webbrowser.open("http://www.youtube.com/watch?v=-9ceBgWV8io")
	print("It started on : " + time.ctime());

	i = i + 1