Python tool to model user interactions for website performance testing. This tool is FOR PERFOMANCE/ACTIVITY TESTS ONLY, I DO NOT ENCOURAGE NOR CLAIM RESPONSIBILITY FOR ANY OTHER USAGE.

Visits a site under scaped ip proxy confirmed either in CA or US and models user interactions based on a list of partial <a href></a> tag contents. Running the batch file will model sporadic interaction (due to general reliablity of proxy servers) 20-50 times (visit-to-click)

Requires selenium, webdriver-manager, and requests.

In the batch file, place your site link in "LINK-TO-VISIT"

In the python file, the array ['instert partial link text in this list'] can be replaced with an array of partial text contents of the embedded link <a> tags (i.e. ['blueberry', 'apple', 'yellow'] with the strings being partial link text)

Props to TheSpeedX's PROXY-List repo for providing the updating proxy lists

Props to kevinbazira's sleek-web-bot repo for providing an excellent (though outdated) starting point

This is released under the MIT licence, and I hold no responsibility over how one might use it. 

NOTE: in order to make this work correctly you may need to change the submit_button assignment as the two I have are simply the two most common Wordpress cookie notifications, and target site may be using custom popups. Alternatively that try except can be removed as my 'click' should bypass most elements 'covering' the link text
