import requests


def SampleRecord():
	r = requests.get("http://uinames.com/api?ext&region=United%20States",
                     timeout=2.0)

	json_data = r.json()
	if json_data is None:
		return True

	return f'''My name is {json_data['name']} {json_data['surname']}
		       and the PIN on my card is {json_data['credit_card']['pin']}.'''


if __name__ == '__main__':
    print(SampleRecord())
