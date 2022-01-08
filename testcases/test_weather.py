import allure
from InterfaceCI.library.base import Base


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

	@allure.story('城市为深圳')
	def test_shenzhen(self):
		# url = self.host+self.ep_path+'101020100.html'
		# response = self.client.get(url)
		# city = json.loads(response).get('weatherinfo').get('city')
		city = self.base.get_cityname('101280601')
		assert  city=='深圳'

	@allure.story('城市为广州')
	def test_guangzhou(self):
		# url = self.host+self.ep_path+'101020100.html'
		# response = self.client.get(url)
		# city = json.loads(response).get('weatherinfo').get('city')
		city = self.base.get_cityname('101280101')
		assert  city=='广州'