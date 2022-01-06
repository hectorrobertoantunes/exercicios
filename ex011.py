# Calculador de tinta

h = float(input('Coloque aqui a altura da sua parede em metros: '))
w = float(input('Coloque aqui a largura da sua parede em metros: '))
print('As dimensões da sua parede é de {}x{} metros quadrados'.format(h,w))
print('Portanto, você se levarmos em consideração que cada litro de tinta pinta 2 metros, logo você precisará de {} litros'.format((h*w)/2))