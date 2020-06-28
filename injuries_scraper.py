import requests
import json
import website
import threading
import time

API_KEY = "tFLMWhfaTXK7"
PROJECT_TOKEN = "tWU6nvGOarc2"
RUN_TOKEN = "t33wTrfmLPF1"


def main():
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

		def get_player_info(self, injuries):
			data = self.data["player"]

			for content in data:
				if content['position'].lower() == injuries.lower():
					return content

			return "0"


		def get_list(self):
			players = []
			for play in self.data['injuries']:
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


	def return_data(injuries):
		injuries_data = data.get_player_info(injuries)
		position = (injuries_data['position'])
		player_name = (injuries_data['name'])
		status = (injuries_data['status'])
		return position, player_name, status





	data = Data(API_KEY, PROJECT_TOKEN)
	data.update_data()



	initial_data = Data(API_KEY, PROJECT_TOKEN)
	all_data = initial_data.get_data()["player"]
	

	
	print_name = []
	print_pos = []
	football_pos2 = ["QB", "RB","WR", "TE", "OT", "DE", "DT", "LB", "CB", "SS", "FS", "PK", "PR", "KR", "LS"]
	football_pos1 = ["G", "C", "P", "H"]
	i = 0

	i=0
	for index in all_data:
		i+=1
		unedited_name = all_data[i-1]["name"]
		if str(unedited_name[-2:]) in football_pos2:
			edited_name = unedited_name[:-2]
			pos = unedited_name[-2:]
			print_name.append(edited_name)
		else:
			if str(unedited_name[-1:]) in football_pos1:
				edited_name = unedited_name[:-1]
				pos = unedited_name[-1:]
				print_name.append(edited_name)
			else:
				edited_name = unedited_name[:-2]
				pos = unedited_name[-2:]
				print_name.append(edited_name)

	
	for i in range(53):
		print_name.append('')

	return print_name
	#return name+space+position+space+status



if __name__ == "__main__":
	main()
