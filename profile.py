
class ReligionInfo(object):
	religion = ""
	caste = ""
	subcaste = ""
	gothram = ""
	star = ""
	kuja_dosham = ""


class LocationInfo(object):
	country = ""
	state = ""
	city = ""
	resident_status = ""
	citizenship = ""


class ProfessionalInformation(object):
	education = ""
	occupation = ""
	education_in_detail = ""
	occupation_in_detail = ""
	employed_in = ""
	annual_income = ""

class FamilyInfo(object):
	family_values = ""
	family_type = ""
	family_status = ""
	ancestral_origin = ""
	fathers_occupation = ""
	mothers_occupation = ""
	number_of_brothers = ""
	number_of_sisters = ""
	about_our_family = ""


class Profile(object):
	name = ""
	age = 0
	height = ""
	mother_tongue = ""
	eating_habits = ""
	smoking_habits = ""
	complexion = ""
	physical_status = ""
	weight = ""
	marital_status = ""
	drinking_habits = ""
	religion_info = ReligionInfo()
	location_info = LocationInfo()
	professional_info = ProfessionalInformation()
	family_info = FamilyInfo()
	hobby_info = ""
	
	def __init__(self):
		"""docstring for __init__"""
	
	def save(self):
		
	
