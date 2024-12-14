Project-RPS
===========


    · Propuesta
    · Características del entorno
    · Estructura del agente

### Propuesta
Este proyecto trata de crear un programa que ejecute el popular juego de piedra papel o tijera (será referenciado como RPS) y sea capaz de acumular la mayoría de victorias contra un usuario. Si se tratara de un juego de azar la probabilidad de ganar sería una de tres, pero, consciente o inconscientemente, siempre se sigue una estrategia. Una de estas mismas estrategias es la que se pretende descifrar en la propuesta siguiente.

En el contenido de este proyecto se encuentra una tabla resumen de las características del entorno de tareas explicando y argumentando cada sección, un esquema de la estructura del agente escogido y su relación con el código y por último el código python empleado para el desarrollo del proyecto.
### Características del entorno

Entorno | Observable| Agentes | Determinista | Episódico | Estático | Discreto | Conocido | Adverso |
:---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
 RPS | Parcial | Multi-agente | Estocástico | Secuencial | Estático |  Discreto |  Conocido | Adverso |

**· Parcialmente visible:**
	No todos los factores que influyen en el resultado son visibles en el momento de tomar la decisión. El agente no sabe (con exactitud) qué opción va a escoger el usuario cuando tiene que decidir qué sacar.

**· Multi-agente:**
	El número de participantes para que el juego funcione es mayor a uno, en este caso concreto es de dos, la máquina y el usuario.

**· Estocástico:**
	Con los datos que se tienen, el resultado es no predecible. Como en cada ronda el ganador es incierto no se puede tener conocimiento fundado del fin de la partida.

**· Secuencial:**
	Las acciones presentes afectan a las futuras. Según la programación del agente (véase apartado X), este almacena información del rendimiento del usuario y actúa en base a ella en las próximas partidas.

**· Estático:**
	El entorno no cambia mientras se está tomando la decisión, cambia inmediatamente después, en el desenlace de la ronda.

**·Discreto:**
	Las posibles acciones y resultados son concretos y contables. Existen tres opciones (piedra, papel o tijera) y nueve resultados (el agente tiene tres opciones y el usuario tiene tres opciones, entonces 3x3=9).

**· Conocido:**
	El agente domina las reglas del juego y es capaz de aplicarlas sin dificultad.

**· Adverso:**
	El objetivo del agente es directamente contrario al del usuario. El agente es recompensado cuando gana o, que en este caso es lo mismo, cuando el usuario pierde.
