# Prueba_Final_Ciberseguridad
Tratamiento de datos

### Objetivos
Extraer datos de una fuente online para su posterior analisis y almacenado

### Parte 1
Consigue extraer datos de una fuente de datos online
La pagina de donde se extraeran las api sera de la tienda de segunda mano "amigui"
https://amigui.com.ec/collections/masculino
![image](https://github.com/eddieyanez24/Prueba_Final_Ciberseguridad/assets/144464488/55114469-fe49-41fe-846e-476ffeb69f5e)
***
Se logro encontrar las Api de la pagina web 
![image](https://github.com/eddieyanez24/Prueba_Final_Ciberseguridad/assets/144464488/95280e6b-3e63-4159-b8d8-868a798de211)
![image](https://github.com/eddieyanez24/Prueba_Final_Ciberseguridad/assets/144464488/fbd97807-9ca7-4b7a-a54e-f099a8374d3a)
***
Posterior a eso se utilizo python para poder obtener la base de datos. Lo podemos encontrar en el archivo "amigui_data_fetcher.py"
![image](https://github.com/eddieyanez24/Prueba_Final_Ciberseguridad/assets/144464488/b4ca8023-932c-450d-b8ca-30b34da40f42)
![image](https://github.com/eddieyanez24/Prueba_Final_Ciberseguridad/assets/144464488/97e2a20c-f3ba-40a8-98de-af98f8fb4158)


***
### Parte 2
Almacenar esta información de forma estructurada en una base de datos en MongoDB
Para Generar la base de datos de MongoDB utilizamos el archivo "mongo.py"
![image](https://github.com/eddieyanez24/Prueba_Final_Ciberseguridad/assets/144464488/37701117-9c98-4f01-bb7a-54c3be1a7065)
A partiir de ese archivo generamos la base de datos en MongoDB
![image](https://github.com/eddieyanez24/Prueba_Final_Ciberseguridad/assets/144464488/9d787a5d-ccf8-4e28-bd4d-7f36075d21ed)

***
### Parte 3
Se creo un servio web utilizando Python+Flask, lo podemos encontrar en el archivo "api.py" que se encuentra dentro de la carpeta flask
![image](https://github.com/eddieyanez24/Prueba_Final_Ciberseguridad/assets/144464488/d9f0a40f-f01f-4d75-8648-4217ffd9fe75)

![image](https://github.com/eddieyanez24/Prueba_Final_Ciberseguridad/assets/144464488/4dbbde6f-d0af-4cd0-873d-54911fd12c8f)

***
### CONCLUSIONES
- Se llego a completar los objetivos propuestos hay que recalcar que la mayor dificultad que se dio fue al momento de almacenar los datos en MongoDB ya que se producia un error al cargar los datos asi como tambien no se conectaba con el servidor de Mongo
- Otro de los inconvenientes fue encontrar una pagina web que permitiera extraer los datos ya que la gran mayoria de ellos no permitian es decir estaban protegidos


