✈️ Registro de Equipaje - VuelosChileUn script de consola en Python diseñado para automatizar el registro y clasificación del equipaje de los pasajeros de la aerolínea VuelosChile. El sistema solicita los datos de cada maleta y determina automáticamente si debe ser asignada a la cabina o a la bodega del avión según su peso.🚀 CaracterísticasValidación de entradas: Asegura que el número total de equipajes sea un número entero positivo, evitando caídas del programa por errores tipográficos.Comprobación de Tickets: Exige que los códigos de ticket tengan un mínimo de 5 caracteres y no contengan espacios en blanco.Clasificación Automática: * Equipaje $\le$ 10 Kg: CabinaEquipaje > 10 Kg: BodegaManifiesto de Carga: Genera un resumen final detallando la cantidad total de maletas asignadas a cada sección del avión.🛠️ RequisitosPara ejecutar este script, solo necesitas tener instalado Python en tu sistema.Python 3.x💻 Instrucciones de UsoClona este repositorio o descarga el archivo .py (por ejemplo, registro_equipaje.py).Abre una terminal o línea de comandos.Navega hasta el directorio donde se encuentra el archivo.Ejecuta el script con el siguiente comando:Bashpython registro_equipaje.py
📋 Ejemplo de EjecuciónAl iniciar el programa, la consola te guiará paso a paso:Plaintext=== REGISTRO DE EQUIPAJE - VUELOSCHILE ===
¿Cuántos equipajes desea registrar? 2

--- Registro del equipaje N° 1 ---
Ingrese código de ticker (Min. 5 carácteres, sin espacios): TCK99
Ingrese el peso del equipaje en Kg.: 8
Clasificado como equipo de cabina

--- Registro del equipaje N° 2 ---
Ingrese código de ticker (Min. 5 carácteres, sin espacios): TCK44
Ingrese el peso del equipaje en Kg.: 15
Clasificado como equipo de bodega

==============================================
El avión transportará 1 equipajes en Cabina y 1 equipajes en Bodega. Manifiesto de carga listo.

==============================================
