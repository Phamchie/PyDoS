
#bin/bash
echo "[+] Starting Setup Tools"
echo ""

function setup_tools() {
	pip install aiohttp
	echo ""
	echo "[+] Finished [ aiohttp ] "
	echo ""
	sleep 1

	pip install threading
	echo ""
	echo "[+] Finished [ threading ] "
	echo ""
	sleep 1

	pip install colorama
	echo ""
	echo "[+] Finished [ colorama ] "
	echo ""
	sleep 1

	pip install requests
	echo ""
	echo "[+] Finished [ requests ] "
	echo ""
	sleep 1

	echo ""
	echo "[+] Setup done"
	echo ""

}

setup_tools
