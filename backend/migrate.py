import asyncio
from config.connect import create_db_pool
from pygem.migrations import main

if __name__ == "__main__":
    # Creamos un bloque de ejecución asíncrono para toda la aplicación.
    async def run_migrations():
        # Creamos el pool de conexiones usando await.
        pool = await create_db_pool()
        if pool:
            # Ejecutamos la función principal y el pool se cerrará
            # automáticamente cuando la función `main` termine.
            await main(pool)
        else:
            print("No se pudo iniciar el proceso de migración. Verifica tu conexión a la BD.")

    # Ejecutamos la función asíncrona principal.
    asyncio.run(run_migrations())
