## Interfaz Gráfica para el Proyecto de Transformación de Gestión de Consultas Académicas

¡Bienvenido a la interfaz gráfica de nuestro emocionante proyecto de transformación de gestión de consultas académicas mediante la integración de LLM y la API de OpenAI en un Asistente Académico! En esta interfaz, hemos desarrollado una solución que utiliza tecnologías avanzadas de procesamiento de lenguaje natural para mejorar la búsqueda y gestión de información académica.

### Características Destacadas de la Interfaz
- **Asistente Académico Potenciado por AI:** Nuestra interfaz incluye un asistente académico impulsado por inteligencia artificial que ayuda a los usuarios a encontrar de manera eficiente la información académica relevante. Esto simplifica el proceso de búsqueda y gestión de documentos académicos.
- **Integración de LLM y OpenAI API:** Hemos integrado el modelo de lenguaje de largo plazo (LLM) junto con la API de OpenAI para mejorar la capacidad de comprensión y respuesta del asistente académico. Esto permite respuestas más precisas y contextualmente relevantes a las consultas de los usuarios.
- **Gestión Eficiente de Consultas:** La interfaz ofrece herramientas intuitivas para gestionar consultas académicas, lo que permite a los usuarios realizar búsquedas avanzadas, organizar y acceder fácilmente a documentos relevantes.

### Instrucciones de Uso de la Interfaz
1. **Clonar el Repositorio:** Comienza por clonar el repositorio de la interfaz en tu máquina local utilizando el siguiente comando:

```bash
git clone https://github.com/xr-lab-ucacue/Academic-Assistant.git
```

2. **Instalar Dependencias:** Una vez clonado el repositorio, navega al directorio del proyecto y ejecuta el siguiente comando para instalar las dependencias necesarias:

```bash
pip install -r requirements.txt
```

3. **Configurar el Entorno Python:** Asegúrate de tener instalado Python v3.11.4 y pip correctamente configurado en tu sistema. Agrega el path de Python si es necesario.

4. **Instalar Bibliotecas Específicas:**
   - Para instalar Streamlit v1.18.1, ejecuta:
     ```bash
     pip install streamlit==1.18.1
     ```
   - Para instalar la biblioteca OpenAI, ejecuta:
     ```bash
     pip install openai
     ```
   - Si se produce un error relacionado con "altair", instala la versión 4.0 específicamente con el siguiente comando:
     ```bash
     pip install altair==4.0
     ```

5. **Ejecutar la Aplicación:** Utiliza el siguiente comando para ejecutar la interfaz en tu navegador:
```bash
streamlit run app.py
```

6. **Acceder a la Interfaz:** Abre tu navegador web y navega a http://localhost:8501 para acceder a la interfaz gráfica. Utiliza el asistente académico para realizar consultas y gestionar información académica de manera eficiente.

¡Esperamos que esta interfaz simplifique la gestión de consultas académicas y mejore la experiencia de los usuarios al interactuar con documentos académicos! Si tienes alguna pregunta o sugerencia, no dudes en comunicarte con nosotros.

El Equipo de Desarrollo:
Pedro Alvarez
Sebastian Quevedo
