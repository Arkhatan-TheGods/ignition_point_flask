def query_tables() -> str:

    return """
            BEGIN;
            CREATE TABLE IF NOT EXISTS CUSTOMERS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                NAME TEXT NOT NULL,
                CPF TEXT NOT NULL UNIQUE,
                BIRTH_DATE TEXT NOT NULL,
                ADDRESS TEXT NOT NULL,
                CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS PRODUCTS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                NAME TEXT NOT NULL,
                CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            COMMIT;
            """
