import requests
import json
import app
import threading
import time

API_KEY = "tFLMWhfaTXK7"
PROJECT_TOKEN = "tWU6nvGOarc2"
RUN_TOKEN = "t33wTrfmLPF1"


def main(text):
	class Data:
		def __init__(self, api_key, project_token):
			self.API_Key = api_key
			self.Project_Token = project_token
			self.params = {
				"api_key": self.API_Key,
			}
			self.data = self.get_data()

		def get_data(self):
			response = requests.get(f'https://www.parsehub.com/api/v2/projects/{self.Project_Token}/last_ready_run/data', params=self.params)
			data = json.loads(response.text)
			return data

		def get_player_info(self, depth_chart):
			data = self.data["depth_chart"]

			for content in data:
				if content['position'].lower() == depth_chart.lower():
					return content

			return "0"


		def get_list(self):
			players = []
			for player in self.data['depth_chart']:
				players.append(player['position'].lower())

			return players

		def update_data(self):
			response = requests.post(f'https://www.parsehub.com/api/v2/projects/{self.Project_Token}/run', params=self.params)

			def poll():
				old_data = self.data
				while True:
					new_data = self.get_data()
					if new_data != old_data:
						self.data = new_data
						print("Data updated")
						break


				t = threading.Thread(target=poll)
				t.start()


	data = Data(API_KEY, PROJECT_TOKEN)


	def return_data(depth_chart):
		depth_chart_data = data.get_player_info(depth_chart)
		position = (depth_chart_data['position'])
		player_name = (depth_chart_data['name'])
		return position, player_name





	data = Data(API_KEY, PROJECT_TOKEN)
	data.update_data()

	niners_player = text


	all_data = return_data(niners_player)
	all_data[1].append({'name':'N/A'})
	all_data[1].append({'name':'N/A'})
	all_data[1].append({'name':'N/A'})
	all_data[1].append({'name':'N/A'})

	return all_data[1]



if __name__ == "__main__":
	main()
