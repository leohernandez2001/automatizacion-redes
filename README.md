# Mi estación de automatización de redes

## 1. Datos del equipo

**Integrantes:**

* Laura Valeria de la Luz Hernandez
* Leondel de la Luz Hernandez
* Marco Salazar Sanchez
* Monica Vianey Valle Lucio

**Materia:** Administración de Infraestructura Digital 1
**Práctica:** Práctica 01 – Preparación de la estación de automatización
**Fecha:** 23 de septiembre de 2026

---

## 2. Propósito de la práctica

El propósito de esta práctica fue preparar una estación de trabajo para desarrollar actividades de automatización de redes.

Para lograrlo, se instalaron y configuraron herramientas para programación, control de versiones, pruebas, conexión de red, contenedores y simulación de redes. También se preparó un entorno virtual para que el equipo pudiera desarrollar las siguientes prácticas de automatización.

---

## 3. Herramientas instaladas

Durante la práctica se instalaron y configuraron las siguientes herramientas:

* **Python:** utilizado para desarrollar y ejecutar programas.
* **Visual Studio Code:** utilizado para escribir y ejecutar código.
* **Git:** utilizado para administrar las versiones del proyecto.
* **GitHub:** utilizado para almacenar y compartir el proyecto.
* **Postman:** utilizado para trabajar y realizar pruebas de APIs.
* **OpenConnect / OpenConnect GUI:** utilizado para conexiones VPN.
* **Docker:** utilizado para trabajar con contenedores.
* **GNS3 GUI:** utilizado para crear y simular topologías de red.
* **GNS3 VM:** utilizada como máquina virtual para GNS3.
* **VMware Workstation:** utilizado para ejecutar la GNS3 VM.

Además, se utilizó el entorno virtual de Python para mantener aisladas las dependencias del proyecto.

---

## 4. Configuración realizada

Para preparar el entorno de automatización se realizaron las siguientes actividades:

### Python y Visual Studio Code

Primero se instaló Python 3 y se comprobó su funcionamiento desde la terminal.

Después se instaló Visual Studio Code y se configuró la extensión oficial de Python. Se seleccionó el intérprete de Python instalado y se creó la carpeta de trabajo:

```text
automatizacion-redes
```

### Entorno virtual

Dentro de la carpeta del proyecto se creó un entorno virtual de Python y se activó desde la terminal. Posteriormente, se configuró Visual Studio Code para utilizar dicho entorno.

### Programa de prueba

Para comprobar que Python, Visual Studio Code y el entorno virtual funcionaban correctamente, se creó el archivo:

```text
src/hola_mundo.py
```

con un programa sencillo que muestra:

```text
Hola Mundo!
```

El programa se ejecutó desde Visual Studio Code y se comprobó el resultado en la terminal.

### Git y GitHub

Se instaló Git y se configuró la identidad del usuario mediante un nombre y correo electrónico.

Después se utilizó GitHub como repositorio central del proyecto. El equipo acordó trabajar en un solo repositorio denominado:

```text
automatizacion-redes
```

Esto permite que cada integrante pueda realizar cambios y mantener el trabajo del equipo en un mismo lugar.

### Postman, OpenConnect y Docker

Se instalaron Postman, OpenConnect y Docker y se realizaron las comprobaciones correspondientes para verificar su disponibilidad y funcionamiento en el entorno de trabajo.

### GNS3, GNS3 VM y VMware Workstation

Se instaló GNS3 GUI y se descargó la GNS3 VM correspondiente.

Posteriormente, se instaló VMware Workstation y se importó la GNS3 VM mediante el archivo `.ova`.

Finalmente, se configuró GNS3 GUI para utilizar la GNS3 VM y se realizó la integración entre ambos componentes.

---

## 5. Verificación del entorno

La comprobación del entorno se realizó verificando cada una de las herramientas y configuraciones realizadas durante la práctica.

| Elemento           | Verificación                                              | Evidencia                    |
| ------------------ | --------------------------------------------------------- | ---------------------------- |
| Python             | Se comprobó la versión desde la terminal                  | `01-python.png`              |
| VS Code            | Se comprobó que la aplicación inicia correctamente        | `02-vscode.png`              |
| Python en VS Code  | Se verificó el intérprete seleccionado                    | `03-python-vscode.png`       |
| Entorno virtual    | Se comprobó que el entorno estaba activo                  | `04-entorno-virtual.png`     |
| Hola Mundo         | Se ejecutó el programa y se comprobó el resultado         | `05-hola-mundo.png`          |
| Git                | Se comprobó la versión de Git                             | `06-git.png`                 |
| Identidad Git      | Se comprobó el nombre y correo configurados               | `07-git-identidad.png`       |
| GitHub             | Se comprobó la creación del repositorio                   | `08-github.png`              |
| Postman            | Se comprobó que la aplicación funciona                    | `09-postman.png`             |
| OpenConnect        | Se comprobó la instalación                                | `10-openconnect.png`         |
| Docker             | Se comprobó su funcionamiento y ejecución de contenedores | `11-docker.png`              |
| GNS3 GUI           | Se comprobó el funcionamiento de GNS3                     | `12-gns3.png`                |
| GNS3 VM            | Se comprobó la disponibilidad de la máquina virtual       | `13-gns3-vm.png`             |
| VMware Workstation | Se comprobó el funcionamiento de VMware                   | `14-vmware.png`              |
| GNS3 VM en VMware  | Se comprobó la importación de la máquina virtual          | `15-importacion-gns3-vm.png` |
| GNS3 GUI + GNS3 VM | Se comprobó la integración entre ambos componentes        | `16-integracion-gns3.png`    |

Todas las capturas se encuentran almacenadas en:

```text
docs/practica-01/evidencias/
```

---

## 6. Estructura del proyecto

El repositorio se organizó de la siguiente manera:

```text
automatizacion-redes/
│
├── README.md
├── requirements.txt
│
├── src/
│   └── hola_mundo.py
│
├── tests/
│
├── data/
│
└── docs/
    └── practica-01/
        ├── evidencias/
        │   ├── 01-python.png
        │   ├── 02-vscode.png
        │   ├── 03-python-vscode.png
        │   ├── 04-entorno-virtual.png
        │   ├── 05-hola-mundo.png
        │   ├── 06-git.png
        │   ├── 07-git-identidad.png
        │   ├── 08-github.png
        │   ├── 09-postman.png
        │   ├── 10-openconnect.png
        │   ├── 11-docker.png
        │   ├── 12-gns3.png
        │   ├── 13-gns3-vm.png
        │   ├── 14-vmware.png
        │   ├── 15-importacion-gns3-vm.png
        │   └── 16-integracion-gns3.png
        │
        ├── instalacion.md
        ├── configuracion.md
        └── verificacion.md
```

### Función de los archivos y carpetas

* **README.md:** contiene la documentación principal de la práctica.
* **requirements.txt:** registra las bibliotecas de Python utilizadas en el proyecto.
* **src/:** contiene los programas y scripts desarrollados.
* **tests/:** contiene las pruebas de los programas.
* **data/:** contiene los datos utilizados por los programas.
* **docs/:** contiene la documentación y las evidencias de la práctica.

Durante esta práctica no se utilizaron bibliotecas externas de Python, por lo que `requirements.txt` puede permanecer vacío hasta que el proyecto utilice alguna dependencia.

---

## 7. Problemas encontrados y soluciones

Durante la práctica se presentó una dificultad con OpenConnect en Windows.

### Problema

La instalación de OpenConnect no funcionó de la manera esperada en Windows y fue necesario buscar una alternativa que pudiera utilizarse en este sistema operativo.

### Solución

Se utilizó **OpenConnect GUI**, una interfaz gráfica de OpenConnect para Windows. Esta alternativa permitió continuar con la preparación del entorno y realizar el paso correspondiente de la práctica.

También se acordó que todos los integrantes trabajarían en un mismo repositorio de GitHub, en lugar de crear repositorios separados, para mantener el proyecto centralizado y poder identificar los cambios realizados por cada integrante.

---

## 8. Conclusiones

Durante esta práctica se preparó una estación de trabajo para desarrollar actividades de automatización de redes. Se instalaron y configuraron Python, Visual Studio Code, Git, GitHub, Postman, OpenConnect, Docker, GNS3, GNS3 VM y VMware Workstation.

La práctica permitió comprobar el funcionamiento de las herramientas mediante diferentes pruebas. Python se verificó mediante la ejecución del programa `Hola Mundo`, mientras que Visual Studio Code se configuró para trabajar con Python y con un entorno virtual. Git y GitHub se utilizaron para administrar y centralizar el proyecto. Por otra parte, GNS3, GNS3 VM y VMware Workstation se configuraron para preparar un entorno de simulación de redes.

La principal dificultad encontrada fue la utilización de OpenConnect en Windows, por lo que se recurrió a OpenConnect GUI como alternativa. También se estableció el uso de un repositorio único para que todos los integrantes pudieran trabajar en el mismo proyecto y registrar sus cambios.

Las herramientas utilizadas cumplen funciones diferentes, pero forman parte del mismo entorno de trabajo. Algunas permiten desarrollar los programas, otras administrar el proyecto y otras preparar los entornos necesarios para realizar pruebas de redes.

Preparar correctamente el entorno antes de comenzar a desarrollar programas de automatización es importante porque permite verificar desde el inicio que las herramientas necesarias funcionan correctamente. Esto ayuda a evitar problemas durante las siguientes prácticas, facilita el trabajo en equipo y proporciona una base organizada para el desarrollo de proyectos de automatización de redes.
