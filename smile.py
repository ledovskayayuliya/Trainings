Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import simple_draw as sd

def smile_draw(x, y, color):
    radius = 80
    sd.circle(center_position=sd.get_point(x, y), color=color, radius=radius, width=2)

    for step in (-25, 25):
        eye = sd.get_point(x + step, y + 15)
        sd.circle(center_position=eye, color=color, radius=5, width=2)

    for i in range(45, 140):
        start_point = sd.get_point(x - 90 + i, y + 50 - 100 * sd.sin(i))
        end_point = sd.get_point(x - 90 + i, y + 50 - 100 * sd.sin(i))
        sd.line(start_point=start_point, end_point=end_point, color=color, width=2)

for _ in range(10):
    smile_draw(x=sd.random_point().x, y=sd.random_point().y, color=sd.random_color())

sd.pause()
