chilloxManue = {
    'BBQ Chicken Cheese Burger':250,
    'Beef Burger':170,
    'Naga Drums':200
}
def totalPrice(burger,place='Mohakhali'):
    if place=='Mohakhali':
        delivery=40
    else:
        delivery=60
    print((chilloxManue[burger]+delivery)+((chilloxManue[burger])*.08))
totalPrice('Beef Burger')