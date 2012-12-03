import sqlite3
from bm_dal import BMDAL

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
	
	def save(self):
		dal = BMDAL();
		params = {}
		params["hobbies"] = self.hobbies
		params["interests"] = self.interests
		params["favorite_cuisine"] = self.favorite_cuisine
		params["favorite_music"] = self.favorite_music
		params["preferred_dress_style"] = self.preferred_dress_style
		params["preferred_movies"] = self.preferred_movies
		params["spoken_languages"] = self.spoken_languages
		return dal.insert_hobby_info(params)


class ReligionInfo(object):
	def __init__(self):
		"""docstring for __init__"""
		self.religion = ""
		self.caste = ""
		self.subcaste = ""
		self.gothram = ""
		self.star = ""
		self.kuja_dosham = ""
	
	def save(self):
		dal = BMDAL();
		params = {}
		params["religion"] = self.religion
		params["caste"] = self.caste
		params["subcaste"] = self.subcaste
		params["gothram"] = self.gothram
		params["star"] = self.star
		params["kuja_dosham"] = self.kuja_dosham
		return dal.insert_religion_info(params)


class LocationInfo(object):
	def __init__(self):
		"""docstring for __init__"""
		self.country = ""
		self.state = ""
		self.city = ""
		self.resident_status = ""
		self.citizenship = ""
	
	def save(self):
		dal = BMDAL();
		params = {}
		params["country"] = self.country
		params["state"] = self.state
		params["city"] = self.city
		params["resident_status"] = self.resident_status
		params["citizenship"] = self.citizenship
		return dal.insert_location_info(params)
	


class ProfessionalInformation(object):
	def __init__(self):
		"""docstring for __init__"""
		self.education = ""
		self.occupation = ""
		self.education_in_detail = ""
		self.occupation_in_detail = ""
		self.employed_in = ""
		self.annual_income = ""
	
	def save(self):
		dal = BMDAL()
		params = {}
		params["education"] = self.education
		params["occupation"] = self.occupation
		params["education_in_detail"] = self.education_in_detail
		params["occupation_in_detail"] = self.occupation_in_detail
		params["employed_in"] = self["employed_in"]
		params["annual_income"] = self["annual_income"]
		return dal.insert_professional_information(params)
	

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
	
	def save(self):
		dal = BMDAL()
		params = {}
		params["family_values"] = self.family_values
		params["family_type"] = self.family_type
		params["family_status"] =  self.family_status
		params["ancestral_origin"] = self.ancestral_origin
		params["fathers_occupation"] = self.fathers_occupation
		params["mothers_occupation"] = self.mothers_occupation
		params["number_of_sisters"] = self.number_of_sisters
		params["number_of_brothers"] = self.number_of_brothers
		params["about_our_family"] = self.about_our_family
		return dal.insert_family_info(params)
	

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
	
	def save(self):
		dal = BMDAL()
		params = {}
		params["groom_age"] = self.groom_age
		params["height"] = self.height
		params["marital_status"] = self.marital_status
		params["mother_tongue"] = self.mother_tongue
		params["physical_status"] = self.physical_status
		params["eating_habits"] = self.eating_habits
		params["smoking_habits"] = self.smoking_habits
		params["drinking_habits"] = self.drinking_habits
		params["looking_for"] = self.looking_for
		params["religion_info_id"] = self.religion_info.save()
		params["location_info_id"] = self.location_info.save()
		params["professional_info_id"] = self.professional_info.save()
		return dal.insert_partner_preference(params)
	


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
		self.religion_info = None
		self.location_info = None
		self.professional_info = None
		self.family_info = None
		self.hobby_info = None
		self.partner_preference = None
	
	def save(self):
		dal = BMDAL()
		params = {}
		params["religion_info_id"] = self.religion_info.save()
		params["location_info_id"] = self.location_info.save()
		params["professional_info_id"] = self.professional_info.save()
		params["family_info_id"] = self.family_info.save()
		params["hobby_info_id"] = self.hobby_info.save()
		params["partner_preference_id"] = self.partner_preference.save()
		params["name"] = self.name
		params["age"] = self.age
		params["height"] = self.height
		params["mother_tongue"] = self.mother_tongue
		params["eating_habits"] = self.eating_habits
		params["smoking_habits"] = self.smoking_habits
		params["complexion"] = self.complexion
		params["physical_status"] = self.physical_status
		params["weight"] = self.weight
		params["marital_status"] = self.marital_status
		params["drinking_habits"] = self.drinking_habits
		return dal.insert_profile(params)
	
