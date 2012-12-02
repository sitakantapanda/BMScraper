import sqlite3

class HobbyInfo(object):
	def __init__(self):
		"""docstring for __init__"""
		self.hobbies = ""
		self.interests = ""
		self.favorite_music = ""
		self.preferred_movies = ""
		self.favorite_cuisine = ""
		self.preferred_dress_style = ""
		self.spoken_languages = ""
	


class ReligionInfo(object):
	def __init__(self):
		"""docstring for __init__"""
		self.religion = ""
		self.caste = ""
		self.subcaste = ""
		self.gothram = ""
		self.star = ""
		self.kuja_dosham = ""
	


class LocationInfo(object):
	def __init__(self):
		"""docstring for __init__"""
		self.country = ""
		self.state = ""
		self.city = ""
		self.resident_status = ""
		self.citizenship = ""
	


class ProfessionalInformation(object):
	def __init__(self):
		"""docstring for __init__"""
		self.education = ""
		self.occupation = ""
		self.education_in_detail = ""
		self.occupation_in_detail = ""
		self.employed_in = ""
		self.annual_income = ""
	

class FamilyInfo(object):
	def __init__(self):
		"""docstring for __init__"""
		self.family_values = ""
		self.family_type = ""
		self.family_status = ""
		self.ancestral_origin = ""
		self.fathers_occupation = ""
		self.mothers_occupation = ""
		self.number_of_brothers = ""
		self.number_of_sisters = ""
		self.about_our_family = ""
	

class PartnerPreference(object):
	def __init__(self):
		"""docstring for __init__"""
		self.groom_age = ""
		self.height = ""
		self.marital_status = ""
		self.mother_tongue = ""
		self.physical_status = ""
		self.eating_habits = ""
		self.smoking_habits = ""
		self.drinking_habits = ""
		self.looking_for = ""
		self.religion_info = ReligionInfo()
		self.location_info = LocationInfo()
		self.professional_info = ProfessionalInformation()
	


class Profile(object):
	def __init__(self):
		"""docstring for __init__"""
		self.name = ""
		self.age = 0
		self.height = ""
		self.mother_tongue = ""
		self.eating_habits = ""
		self.smoking_habits = ""
		self.complexion = ""
		self.physical_status = ""
		self.weight = ""
		self.marital_status = ""
		self.drinking_habits = ""
		self.religion_info = ReligionInfo()
		self.location_info = LocationInfo()
		self.professional_info = ProfessionalInformation()
		self.family_info = FamilyInfo()
		self.hobby_info = HobbyInfo()
		self.partner_preference = PartnerPreference()
	
	def save(self):
		sqlite3.connect('./db/bharat_matrimony.db')
	
