% Fichero de Filtrado de Datos y de Separaci�n de los Datos en Variables 
% de Inter�s.

load('insolight_data_complete_may.txt')

% Filtrado de Datos.
SMR_tm=insolight_data_complete_may(:,12);
DNI=insolight_data_complete_may(:,2);
WindSpeed=insolight_data_complete_may(:,8);
Airmass = insolight_data_complete_may(:,18);
Isc = insolight_data_complete_may(:,13);
Azimuth = insolight_data_complete_may(:,20);

insolight_filtered_measurements=zeros(3000, 20);
j=1; 
for i=1:7926
    if (SMR_tm(i,1) < 1.3)&&(SMR_tm(i,1) > 0.96)&&(DNI(i,1) > 600)&&(WindSpeed(i,1) < 10)&&(Airmass(i,1) < 10)&&(Isc(i,1) > 0.1)&&(Azimuth(i,1) > 150)
        insolight_filtered_measurements(j,:)=insolight_data_complete_may(i,:);
        j=j+1;
    end
end

% Se representan los datos filtrados.
Isc_DII_filtered = insolight_filtered_measurements(:,13)./insolight_filtered_measurements(:,10);
AirTemp_filtered = insolight_filtered_measurements(:,7);
SMRtop_mid_filtered = insolight_filtered_measurements(:,12);
Airmass_filtered = insolight_filtered_measurements(:,18);

plot(AirTemp_filtered.',Isc_DII_filtered.', 'r+');
title('Isc/DII en funci�n de la Temperatura Ambiente')
xlabel('Temperatura Ambiente (�C)')
ylabel('Isc/DII (A/(W/m2))')
figure;

plot(SMRtop_mid_filtered.',Isc_DII_filtered.', 'r+');
title('Isc/DII en funci�n de SMR (top-middle)')
xlabel('SMR (top-middle) (-)')
ylabel('Isc/DII (A/(W/m2))')
figure;

plot(Airmass_filtered.',Isc_DII_filtered.', 'gx');
title('Isc/DII en funci�n de la Masa de Aire')
xlabel('Masa de Aire Relativa (-)')
ylabel('Isc/DII (A/(W/m2))')
figure;
