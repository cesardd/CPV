# Carga y Procesado de Datos sin influencia de la Temperatura Ambiente

nontemp_data = np.loadtxt('C:\\Users\\Marcos\\Desktop\\datos modelado\\nontemp_measurements.txt', 
                          delimiter = ',')

nontemp_IscDNI = nontemp_data[:, 25]
nontemp_airmass = nontemp_data[:, 33]

import statistics as stats

IscDNI_medians = []
Airmass_aux = []
for i in np.arange(1,2.8,0.1):
    array_aux1 = []
    for j in range(len(nontemp_IscDNI)):
        if nontemp_airmass[j] > i-0.05 and nontemp_airmass[j] < i+0.05:
            array_aux1.append(nontemp_IscDNI[j])
    if len(array_aux1) > 0:
        IscDNI_medians.append(stats.median(array_aux1))
        Airmass_aux.append(i)

m_low, n_low, m_high, n_high, thld = calc_uf_lines(Airmass_aux, IscDNI_medians)

x1 = np.arange(1,2.3,0.1)
y1 = m_low * x1 + n_low
x2 = np.arange(1.8,5,0.1)
y2 = m_high * x2 + n_high

import matplotlib.pyplot as plt
plt.plot(nontemp_airmass, nontemp_IscDNI, 'b.', Airmass_aux, IscDNI_medians, 
         'g.', x1, y1, 'g', x2, y2, 'r')
plt.xlabel('Masa de Aire (-)')
plt.ylabel('Isc/DNI (A/(W/m2))')
plt.title('Análisis de Isc/DNI en función de la Masa de Aire')
plt.savefig("grafica1.png", dpi=300)

IscDNI_ast = 3.346/1000
uf_am = get_simple_util_factor(airmass_array, thld, m_low/IscDNI_ast, 
                               m_high/IscDNI_ast)

# Carga y Procesado de Datos sin influencia de la Masa de Aire

nonairmass_data = np.loadtxt('C:\\Users\\Marcos\\Desktop\\datos modelado\\nonairmass_measurements.txt', 
                             delimiter = ',')

nonairmass_IscDNI = nonairmass_data[:, 25]
nonairmass_temp = nonairmass_data[:, 10]
m_low, n_low, m_high, n_high, thld = calc_uf_lines(nonairmass_temp, 
                                                   nonairmass_IscDNI,
                                                   'temp_air')

AmbientTemp = data[:,10]

uf_at = get_simple_util_factor(AmbientTemp, thld, m_low/IscDNI_ast, 
                               m_high/IscDNI_ast)
