# за день машина проезжает n километров
# Сколько дней потребуется для того чтобы проехать m километров?

a = input('введите количество пройденных километров в день >')
b = input('введите количество километров в маршурте >')

c = (int(a) + int(b) - 1) // int(a)


print(c)