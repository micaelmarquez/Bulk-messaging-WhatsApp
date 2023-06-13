# Bulk-messaging-WhatsApp
Python script for bulk messaging

Consideraciones al utilizar la app:

1) Si se equivocaron y quieren reiniciarlo, continúen todo con normalidad hasta que empiece a mandar mensajes. 
Luego de eso, presionen la tecla shift por 5 segundos.

2) Los contactos deberán ser cargados con el formato que contiene el archivo excel de prueba (solo 2 columnas, con los títulos correspondientes).
Sugiero no borrar el archivo y mantenerlo como recordatorio de cómo es el formato requerido.

3) Deberán crearse un chat propio y fijarlo, de modo que quede primero en la lista de chats de manera permanente.

4) Deberán mandarse un mensaje por el mismo chat ANTES de ejecutar el programa. Esto es importante para que cuando tengan que seleccionar 
las coordenadas en las que se encuentra la línea de mensajes "api.whatsapp", el programa pueda recrearlo.

5) Para enviar imágenes, recuerden que cuando se abra la ventana de whatsapp web, deberán enviarse primeramente a su chat pinneado o a 
cualquier chat la imagen que enviarán a sus clientes. El nombre del archivo que vayan a enviar deberá tener el nombre de 
"foto" (sin comillas). De no ser así, el software no podrá reconocerla. 

6) Aunque llevará algo de tiempo, les insto a leer las ventanas emergentes con las instrucciones sobre qué hacer. Al hacerlo, evitarán 
perder aún más tiempo al repetir tareas debido a errores causados por no leer. Recuerden que el tiempo que les llevará leer las 
instrucciones será menor que el tiempo que perderán al no hacerlo correctamente.

7) Los mensajes de texto que deseen cargar en un archivo .txt (bloc de notas) deben seguir el siguiente formato si desean utilizar emojis:

----- Ejemplo en .txt -----------

Hola chicos :burger
¿Cómo están? ¿Quieren una Frich Burguer?
Porque yo sí quiero una!
---------------------------------


Observen cómo se vería el mensaje en WhatsApp Web:

----- Ejemplo en WhatsApp Web -----------

"Hola chicos (emoji de hamburguesa de WhatsApp) ¿Cómo están? ¿Quieren una Frich Burguer?"
"Porque yo sí quiero una!"
-----------------------------------------

En el ejemplo, es importante notar que para incluir un emoji y continuar escribiendo en la misma línea o mensaje, deben presionar 
"Enter" (es decir, escribir en el renglón de abajo) en su archivo .txt. Esto se debe a la forma en que se insertan los emojis en 
WhatsApp de manera indirecta.

Además, noten que en el ejemplo de cómo se vería en WhatsApp, aparece un segundo renglón que dice "Porque yo sí quiero una!". 
Esto sucede porque cuando escribimos un "Enter" en el archivo .txt (es decir, escribir en un nuevo renglón), se traduce como un 
"Enter" en WhatsApp Web. Por lo tanto, se enviará la misma cantidad de mensajes como "Enters" hayan utilizado en el archivo .txt, 
excepto en el caso de los emojis.
