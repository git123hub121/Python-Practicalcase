from faker import Faker

fake = Faker()
fake.name()
# Danny Clarke
print(fake.address())
# 909 Nichols Ferry
# Abigailfort, MA 69479

fake.building_number() # 楼栋名称
# 'U座'

fake.postcode() # 邮政编码
# 257897

fake.street_address() # 街道地址
# 吴路e座

fake.street_name()  # 街道名称
# 嘉禾路

fake.ean(length=13)  # EAN条形码
# '5427745056706'

fake.ean13()  # EAN13条形码
# '0937312282094'

fake.ean8()  # EAN8条形码
# '52227936'