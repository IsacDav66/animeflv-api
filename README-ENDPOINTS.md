Cómo utilizar los nuevos endpoints:

1. **Buscar anime por nombre**:
   - Endpoint: `/search?query=one piece`
   - Descripción: Busca anime con el nombre "one piece".
   - Método: GET
   - Respuesta: Lista de anime que coinciden con la búsqueda.

2. **Obtener información sobre un anime específico**:
   - Endpoint: `/anime/naruto`
   - Descripción: Obtiene información detallada sobre el anime "naruto".
   - Método: GET
   - Respuesta: Detalles del anime, como título, sinopsis, género, etc.

3. **Obtener enlaces de descarga para un episodio específico de un anime**:
   - Endpoint: `/anime/one-piece/episodes/1`
   - Descripción: Obtiene los enlaces de descarga para el episodio 1 del anime "one piece".
   - Método: GET
   - Respuesta: Lista de enlaces de descarga para el episodio.

4. **Obtener los últimos animes lanzados**:
   - Endpoint: `/anime/latest`
   - Descripción: Obtiene una lista de los últimos animes lanzados.
   - Método: GET
   - Respuesta: Lista de los últimos animes, cada uno con su información básica.

5. **Obtener los últimos episodios lanzados**:
   - Endpoint: `/episodes/latest`
   - Descripción: Obtiene una lista de los últimos episodios lanzados.
   - Método: GET
   - Respuesta: Lista de los últimos episodios, cada uno con su información básica.

Puedes enviar estas solicitudes utilizando cualquier cliente HTTP, como Postman o cURL, especificando los endpoints correspondientes y sus métodos.