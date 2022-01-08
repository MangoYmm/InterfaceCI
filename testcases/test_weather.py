import json

import allure

from RecordedVideoPrac.InterfaceCI.library.base import Base
from RecordedVideoPrac.InterfaceCI.library.httpclient import HttpClient

@allure.feature("weather api")
class TestWenther:
	def setup_class(self):
		self.base = Base()
	@allure.story('城市为北京')
	def test_beijing(self):
		# url = self.host+self.ep_path+'101010100.html'
		# response = self.client.get(url)
		# city = json.loads(response).get('weatherinfo').get('city')
		city =self.base.get_cityname('101010100')
		assert  city=='北京'

	@allure.story('城市为上海')
	def test_shanghai(self):
		# url = self.host+self.ep_path+'101020100.html'
		# response = self.client.get(url)
		# city = json.loads(response).get('weatherinfo').get('city')
		city = self.base.get_cityname('101020100')
		assert  city=='上海'