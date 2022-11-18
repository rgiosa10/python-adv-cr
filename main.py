from faker import Faker

fake = Faker()

colors = []

for item in range(20):
    color = fake.safe_color_name()
    colors.append(color)

print(colors)