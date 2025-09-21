# title là tên
# width là chiều rộng
# height là chiều cao
# bg là backgroud
# Nêu ko để cái gì hết thì sẽ để 500 x 500
from guizero import App, Text
ungdung= App (title='Hello World',width=900,height=900,bg='white')
noidung= Text (master=ungdung, text='Welcome to the app',bg='black')
ungdung.display()