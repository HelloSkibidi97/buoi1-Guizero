# title là tên
# width là chiều rộng
# height là chiều cao
# bg là backgroud
# Nêu ko để cái gì hết thì sẽ để 500 x 500
# size là kích cỡ chữ
# color để đổi màu chữ
# master có hay ko cũng dc nhưng phải đứng đầu tiên (nằm trong Text, Picture, ...)
# font là phông chữ
# bold để in đậm chữ, đứng sau tên phông chữ
from guizero import App, Text
ungdung= App (title='Hello World',width=900,height=900,bg='silver')
noidung= Text (ungdung, size=17, text='Welcome to the app',bg='white', font='Courier New bold', color='blue')
ungdung.display()