for i in {1..10}; do
	echo "Looping..."
	curl https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt -L -o http.txt &
	wait
	(echo "LINK-TO-VISIT") | python webBot2.py
done