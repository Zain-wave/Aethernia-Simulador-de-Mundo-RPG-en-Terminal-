# 🧠 Proyecto: Aethernia — Simulador de Mundo RPG en Terminal

### 🌍 Descripción general
**Aethernia** es un simulador de mundo RPG totalmente gestionado desde la **terminal**.  
El jugador o administrador controla el paso del tiempo, el clima, la economía, los NPCs y los eventos mediante comandos.  
El objetivo es mantener un mundo coherente y dinámico que evoluciona de forma autónoma.

El proyecto busca desarrollar un **motor de simulación modular**, capaz de persistir datos, generar comportamientos emergentes y reaccionar ante eventos complejos, todo sin interfaz gráfica.

---

## 🎯 Objetivos principales

1. **Motor de Mundo y Tiempo**
   - Control de ciclos de día/noche y estaciones.
   - Sistema climático dinámico (lluvia, sequía, tormentas).
   - Persistencia del estado del mundo (guardado y carga desde archivo JSON).

2. **Economía Viva**
   - Generación de recursos, comercio y precios variables.
   - Influencia del clima y eventos en la producción.
   - Posibilidad de inflación, escasez o quiebras.

3. **NPCs Inteligentes**
   - Personalidades, oficios, y relaciones básicas.
   - Rutinas diarias simuladas por tick (avance de tiempo).
   - Reacciones ante eventos del mundo (enfermedades, guerras, festivales).

4. **Eventos y Misiones**
   - Generación procedural de misiones y catástrofes.
   - Registro histórico de lo ocurrido.
   - Impacto real de los eventos en economía y personajes.

5. **Interfaz de Línea de Comandos (CLI)**
   - Navegación con menús interactivos (usando `Rich` o `Prompt Toolkit`).
   - Comandos para inspeccionar el mundo, avanzar el tiempo, crear NPCs o provocar eventos.
   - Feedback visual con colores, tablas y logs del mundo.

---

## 🧩 Repartición de trabajo

### 👤 Desarrollador 1 – Motor y Economía
- Sistema de tiempo, clima y persistencia del mundo.
- Lógica económica (oferta, demanda, comercio, inflación).
- Módulo de almacenamiento (lectura/escritura JSON o SQLite opcional).

### 👤 Desarrollador 2 – NPCs, Eventos y CLI
- Implementación de NPCs con IA básica y relaciones.
- Generador de eventos aleatorios y misiones dinámicas.
- Menús, comandos y flujo de interacción desde terminal.

---

## ⚙️ Tecnologías y librerías 

| Tipo | Librería | Descripción |
|------|-----------|-------------|
| CLI | `rich` o `prompt_toolkit` | Menús y colores en la terminal |
| Datos | `json` / `sqlite3` | Persistencia del mundo |
| Tests | `pytest` | Pruebas unitarias |
| Utilidades | `random`, `datetime`, `dataclasses` | Simulación y modelado de entidades |


### 🧩 Explicación breve

| Carpeta | Función principal |
|----------|-------------------|
| **world/** | Contiene toda la lógica del entorno: tiempo, economía, simulación y persistencia. |
| **entities/** | Define NPCs, eventos, facciones y estructuras de datos del mundo. |
| **cli/** | Módulo de interacción con el usuario en la terminal. |
| **core/** | Configuración, logging y herramientas globales usadas en todo el proyecto. |
| **data/** | Archivos que guardan el estado del mundo, plantillas y logs históricos. |
| **tests/** | Conjunto de pruebas automatizadas para garantizar la estabilidad del sistema. |
| **logs/** | Carpeta donde se almacenan los registros automáticos de ejecución y errores. |
