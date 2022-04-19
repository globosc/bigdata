# Trabajo realizado sobre nube Microsoft Azure en un cluster hdInsight

## Introducción
En ese repositorio se utilizan herramientas basadas en el framework spark a través de un cluster hdInsight de la nube de microsoft en donde se analizan los archivos generados por la iniciativa GDELT. En primera instancia consistió en todo un desafío ya que primero el investigador tuvo que entender que era GDELT, como funcionaba, y como integrarlo a la nube azure. 
Para lo cual y haciendo gala de su pasado como ingeniero en sistemas, el investigador optó por realizar un script en bash para descargar las direcciones web de los arhivos publicados en GDELT, para posteriormente descargarlos, descomprimirlos y subirlos al sistema de almacenamiento distribuido de microsoft para ser analizados. Es por esto que se incluyen el script.
Posterior a esto, se responden todas las consultas del desafío utilizando:
1. PIG
2. HIVE
3. PySpark
4. Spark SQL



## About GDELT
El proyecto de la base de datos global de eventos, lenguaje y tono (GDELT por sus siglas en inglés) es una base datos abierta global en tiempo real de la sociedad humana según los medios informativos del mundo, que profundiza en los acontecimientos, las reacciones y emociones de cada parte del mundo en tiempo casi real. Toda esta información está disponible de forma gratuita para investigar, analizar, visualizar e incluso predecir la sociedad humana de acuerdo con la cobertura de noticias globales. También incluye un catálogo completo y de alta resolución de los eventos sociopolíticos geo-referenciados desde 1979 hasta la actualidad. El proyecto GDELT hace un seguimiento de cada boletín de noticias impreso y digital accesible en todo el mundo cada 15 minutos en más de 100 idiomas. La información se procesa utilizando una gran variedad de algoritmos para identificar cientos de categorías de eventos (desde protestas hasta llamamientos por la paz), miles de emociones (desde la ansiedad hasta la felicidad), millones de temas narrativos (desde los derechos de las mujeres hasta el acceso al agua potable), así como ubicaciones, personas, organizaciones y otros indicadores.
Link: https://www.gdeltproject.org/
![image](https://user-images.githubusercontent.com/71105387/164109598-4a71c355-54e9-40bb-b426-a23a15b20e5c.png)
