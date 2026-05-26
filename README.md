
---

```markdown
# ✈️ Registro de Equipaje - VuelosChile

¡Bienvenido al sistema de control y clasificación de equipaje automatizado para **VuelosChile**! Este es un script interactivo en Python desarrollado para agilizar el proceso de embarque, validar los datos de los pasajeros y generar un manifiesto de carga preciso antes del despegue.

---

## 🚀 Características

* **Validación de Entradas Robustas:** El sistema no acepta respuestas vacías, letras en campos numéricos ni datos sin sentido.
* **Filtro Seguros de Tickets:** Verifica que los códigos de ticket tengan una longitud mínima y carezcan de espacios.
* **Clasificación Automática:** Distribuye el equipaje de manera inteligente entre la cabina y la bodega según su peso.
* **Resumen Final:** Genera un manifiesto con el total de bultos por sección de la aeronave.

---

## 📊 Reglas de Clasificación

El sistema evalúa cada pieza de equipaje de forma individual bajo los siguientes criterios de peso:

| Peso del Equipaje | Clasificación | Destino en el Avión |
| :--- | :--- | :--- |
| **Hasta 10 Kg** | Equipaje de Cabina | Compartimento superior / Bajo el asiento |
| **Más de 10 Kg** | Equipaje de Bodega | Zona de carga inferior |

---

## 🛠️ Requisitos e Instalación

Para ejecutar este proyecto solo necesitas tener instalado **Python 3.x** en tu sistema.

1. **Clona este repositorio** en tu máquina local:
   ```bash
   git clone [https://github.com/tu-usuario/registro-equipaje-vueloschile.git](https://github.com/tu-usuario/registro-equipaje-vueloschile.git)

```

2. **Navega al directorio** del proyecto:
```bash
cd registro-equipaje-vueloschile

```


3. **Ejecuta el script**:
```bash
python nombre_de_tu_archivo.py

```



---

## 💻 Ejemplo de Uso

A continuación se muestra cómo interactúa el script en la terminal durante un flujo normal:

```text
=== REGRISTRO DE EQUIPAJE - VUELOSCHILE ===
¿Cuántos equipajes desea registrar? 2

--- Registro del equipaje N° 1 ---
Ingrese código de ticker (Min. 5 carácteres, sin espacios) VCH123
Ingrese el peso del equipaje en Kg. 8
Clasificado como equipo de cabina

--- Registro del equipaje N° 2 ---
Ingrese código de ticker (Min. 5 carácteres, sin espacios) VCH456
Ingrese el peso del equipaje en Kg. 15
Clasificado como equipo de bodega

==============================================
El avión transportará 1 equipajes en Cabina y 1 equipajes en Bodega. Manifiesto de carga listo.
==============================================

```

---

## ⚙️ Estructura del Código

El script está diseñado en base a ciclos de control (`while` y `for`) junto con bloques de manejo de excepciones (`try-except`) para asegurar que el programa no se interrumpa si el usuario comete un error al ingresar los datos.

> 💡 **Nota de desarrollo:** Este proyecto fue creado con fines educativos y de automatización lógica para procesos de aerolíneas.

```

```
