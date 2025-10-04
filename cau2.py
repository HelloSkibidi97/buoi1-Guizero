from guizero import App, Text, Picture
app=App(title='Giới thiệu đặc sản', width=1000, height=800, bg='lightblue')
text=Text(app, text='\n BÚN CÁ', font='Courier new bold', size=41, color='green')
text1=Text(app, text='\nBún cá là một món ăn Việt Nam có nhiều phiên bản,\n' \
                     ' nổi tiếng nhất là bún chả cá Nha Trang với nước dùng ngọt thanh\n' \
                     ' từ xương cá và topping chả cá dai ngon, hoặc bún cá\n' \
                     ' Châu Đốc đậm đà hương vị đặc trưng Campuchia.', size=28, color='red', font='Times new roman')
hinhanh=Picture(app,'tải-xuống.png',width=500,height=500)
app.display()
