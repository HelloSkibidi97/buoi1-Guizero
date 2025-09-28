# title là tên
# width là chiều rộng
# height là chiều cao
# bg là backgroud
# Nêu ko để cái gì hết thì sẽ để 500 x 500
# size là kích cỡ chữ
# text_color là màu chữ:     noidung.text_color='color'
from guizero import App, Text
ungdung= App (title='Hello World',width=900,height=900,bg='silver')
noidung= Text (master=ungdung, size=17, text='Welcome to the app',bg='white')
noidung.text_color='gray12'
ungdung.display()
