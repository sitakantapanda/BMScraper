import sqlite3
import yaml

class BMDAL(object):
	def __init__(self):
		"""docstring for __init__"""
		with open('./config.yml', 'r') as config_file:
			self.config = yaml.load(config_file.read())
		if self.config == None:
			raise Exception('Config', 'File Not Found')
		self.connection = sqlite3.connect(self.config["db_name"])
		self.cursor = self.connection.cursor()
	
	def insert_family_info(self, params):		
		query = "INSERT INTO FamilyInfo(family_values, ancestral_origin, fathers_occupation, mothers_occupation, number_of_brothers, number_of_sisters, about_our_family) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (params["family_values"], params["ancestral_origin"], params["fathers_occupation"], params["mothers_occupation"], params["number_of_brothers"], params["number_of_sisters"], params["about_our_family"])
		self.execute_query(query)
		return self.last_inserted_row()
	
	def insert_hobby_info(self, params):
		query = "INSERT INTO HobbyInfo(hobbies, interests, favorite_music, favorite_cuisine, preferred_dress_style, spoken_languages) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (params["hobbies"], params["interests"], params["favorite_music"], params["favorite_cuisine"], params["preferred_dress_style"], params["spoken_languages"])
		self.execute(query)
		return self.last_inserted_row()
	
	def insert_location_info(self, params):
		query = "INSERT INTO LocationInfo(country, state, city, resident_status) VALUES ('%s', '%s', '%s', '%s')" % (params["country"], params["state"], params["city"], params["resident_status"])
		self.execute(query)
		return self.last_inserted_row()
	
	def insert_professional_info(self, params):
		query = "INSERT INTO ProfessionalInfo(education, occupation, education_in_detail, occupation_in_detail, employed_in, annual_incom) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (params["education"], params["occupation"], params["education_in_detail"], params["occupation_in_detail"], params["employed_in"], params["annual_incom"])
		self.execute(query)
		return self.last_inserted_row()
	
	def insert_profile(self, params):
		query = "INSERT INTO Profile(hobby_info_id, religion_info_id, location_info_id, professional_info_id, family_info_id, partner_preference_id, name, age, height, mother_tongue, eating_habits, smoking_habits, drinking_habits, complexion, physical_status, weight, marital_status) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (params["hobby_info_if"], params["religion_info_id"], params["location_info_id"], params["professional_info_id"], params["family_info_id"], params["partner_preference_id"], params["name"], params["age"], params["height"], params["mother_tongue"], params["eating_habits"], params["drinking_habits"], params["complexion"], params["physical_status"], params["weight"], params["marital_status"])
		self.execute(query)
		return self.last_inserted_row()
	
	def insert_religion_info(self, params):
		query = "INSERT INTO(religion, caste, subcaste, gothram, star, kuja_dosham) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (params["religion"], params["caste"], params["subcaste"], params["gothram"], params["star"], params["kuja_dosham"])
		self.execute(query)
		return self.last_inserted_row()
	
	def execute_query(self, query):
		self.cursor.execute(query)
		self.connection.commit()
	
	def last_inserted_row(self):
		self.cursor.execute("SELECT last_insert_rowid()")
		return self.cursor.fetchone()


if __name__ == '__main__':
	dal = BMDAL()
	params = { "family_values" : "moderate", "ancestral_origin" : "guntur", "fathers_occupation" : "doctor", "mothers_occupation" : "doctor", "number_of_brothers" : "0", "number_of_sisters" : "1", "about_our_family" : "blah" }
	print dal.insert_family_info(params)